# Generated by Django 3.2.8 on 2021-10-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoldItemsWomen',
            fields=[
                ('id', models.TextField(db_column='ID', primary_key=True, serialize=False)),
                ('gender', models.TextField()),
                ('category', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('list_price', models.CharField(blank=True, max_length=10, null=True)),
                ('sale_price', models.CharField(blank=True, max_length=10, null=True)),
                ('condition', models.CharField(blank=True, max_length=10, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('likes', models.CharField(blank=True, max_length=4, null=True)),
                ('comments', models.CharField(blank=True, max_length=4, null=True)),
                ('date_added', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'sold_items_women',
            },
        ),
    ]
