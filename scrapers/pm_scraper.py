import requests
import time
import random
import re
import psycopg2
import json
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
env = os.getenv('ENV')

db_address = os.getenv(f'DB_HOST_{env}')
db_port = 5432
db_user = os.getenv(f'DB_USER_{env}')
db_password = os.getenv(f'DB_PASSWORD_{env}')
db_name = os.getenv(f'DB_NAME_{env}')
page_limit = int(os.getenv('SCRAPER_PAGE_LIMIT'))
postgres_str = (f'postgresql://{db_user}:{db_password}@{db_address}:{db_port}/{db_name}')


# Create the connection
cnx = create_engine(postgres_str)

    

def request_get_html(url):
    html = requests.get(url)
    return html.text


def format_string_result(string):
    result = ' '.join(string.split())
    return result.upper()


def calculate_wait_time(lower_limit, upper_limit):
    return random.uniform(lower_limit, upper_limit)


def get_value_from_html(html, tag_type, class_name, tag_attrib=None, str_replace=None):

    try:
        if tag_attrib is not None:
            value = html.find(tag_type, {"class": class_name})[tag_attrib]
        
        else: 
            value = html.find(tag_type, {"class": class_name}).text
    
    except:
        return "N/A"
    
    if str_replace:
        for repl in str_replace:
            value = value.replace(repl, "")
    
    return format_string_result(value)


# URL Variables
base_url = "https://poshmark.com"
gender = "women"
query_filter = "?availability=sold_out"


def scrape_data(brand, category):

    for i in range(page_limit):
            
        url = base_url + "/brand/" + brand + "-" + gender + "-" + category + query_filter + "&max_id=" + str(i+1)
        print(url)
        soup = BeautifulSoup(request_get_html(url), 'html.parser')
        
    #   Wait to pull the next page for a few seconds   
        time.sleep(calculate_wait_time(5, 10))
        
        for html_details in soup.find_all("div", {"class": "card card--small"}):
            try:
                #   Get Item Name 
                name = get_value_from_html(html_details, "img", "ovf--h", tag_attrib="alt").replace("'", "")
                
                #   Get Item Link
                link = base_url + get_value_from_html(html_details, "a", "tile__title tc--b", tag_attrib="href").lower().replace("'", "")

                #   Get the property listing ID     
                item_id = get_value_from_html(html_details, "a", "tile__title tc--b", tag_attrib="data-et-prop-listing_id")
                
                #   Get the date added (need to regex a cloudfront url)
                date_added = get_value_from_html(html_details, "img", "ovf--h", tag_attrib="src")

                if date_added == 'N/A':
                    date_added = get_value_from_html(html_details, "img", "ovf--h", tag_attrib="data-src")

                date_added = re.search('\d{4}\/\d{2}\/\d{2}', date_added)
                date_added = date_added.group(0)

                #   Get List Price
                list_price = get_value_from_html(html_details, "span", "p--l--1 tc--lg td--lt", str_replace=["$", ","])  

                #   Get Sale Price
                sale_price = get_value_from_html(html_details, "span", "p--t--1 fw--bold", str_replace=["$", ","])        

                #   Get Condition - Not always known
                condition = get_value_from_html(html_details, "span", "condition-tag all-caps tr--uppercase condition-tag--small")

                #   Get Size - Not always known
                size = get_value_from_html(html_details, "a", "tile__details__pipe__size ellipses", str_replace=["Size: "])

                #   Get Brand - Not always known
                brand_name = get_value_from_html(html_details, "a", "tile__details__pipe__brand ellipses")

                #   Get the amount of likes the picture recieved 
                likes_div = html_details.find('div', {"class": 'social-action-bar tile__social-actions'})

                
                try:
                    likes = likes_div.find('span').text
                except:
                    likes = 0

                #   Get the amount of comments the picture recieved 
                comments_div = html_details.find('div', {"class": 'd--fl ai--c jc--sb'})

                try:
                    comments = comments_div.find('span').text
                except:
                    comments = 0
                
                with cnx.connect() as conn:
                    conn.execute(
                    text(f"INSERT INTO sold_items_women (item_id,gender,category,size,name,list_price,sale_price,condition,link,date_added,likes,comments,brand_name) "
                        f"VALUES ('{item_id}','{gender}','{category}','{size}','{name}','{list_price}','{sale_price}','{condition}','{link}','{date_added}','{likes}','{comments}','{brand_name}')")
                    )

            except Exception as e: 
                print(e)
                continue


if __name__ == "__main__":

    with open("pm_data.json", "r") as data: 
        data = json.load(data)
    
    for brand in data[gender]['brands']:
        for category in data[gender]['brands'][brand]:
            scrape_data(brand, category)