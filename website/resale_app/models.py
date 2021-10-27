from django.db import models

class SoldItemsWomen(models.Model):
    id = models.TextField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gender = models.TextField()
    category = models.IntegerField()
    name = models.CharField(blank=True, null=True, max_length=100)
    list_price = models.CharField(blank=True, null=True, max_length=10)
    sale_price = models.CharField(blank=True, null=True, max_length=10)
    condition = models.CharField(blank=True, null=True, max_length=10)
    link = models.CharField(blank=True, null=True, max_length=100)
    likes = models.CharField(blank=True, null=True, max_length=4)
    comments = models.CharField(blank=True, null=True, max_length=4)
    date_added = models.CharField(blank=True, null=True, max_length=10)

    class Meta:
        db_table = 'sold_items_women'
