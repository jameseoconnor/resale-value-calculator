from django.db import models

class SoldItemsWomen(models.Model):
    item_id = models.TextField(db_column='item_id', primary_key=True)  # Field name made lowercase.
    gender = models.TextField()
    category = models.CharField(blank=True, null=True, max_length=100)
    name = models.CharField(blank=True, null=True, max_length=300)
    list_price = models.CharField(blank=True, null=True, max_length=20)
    sale_price = models.CharField(blank=True, null=True, max_length=20)
    condition = models.CharField(blank=True, null=True, max_length=20)
    link = models.CharField(blank=True, null=True, max_length=300)
    likes = models.CharField(blank=True, null=True, max_length=4)
    comments = models.CharField(blank=True, null=True, max_length=4)
    date_added = models.CharField(blank=True, null=True, max_length=20)
    brand_name = models.CharField(blank=True, null=True, max_length=100)
    size = models.CharField(blank=True, null=True, max_length=20)

    class Meta: 
        db_table = 'sold_items_women'   