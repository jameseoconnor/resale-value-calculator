# Generated by Django 3.2.8 on 2021-10-30 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resale_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solditemswomen',
            old_name='id',
            new_name='item_id',
        ),
    ]
