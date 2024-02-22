# Generated by Django 4.2.10 on 2024-02-07 11:34

from django.db import migrations, models
from trashpetapp.models import Accessory

'''
def initialize_accessories(apps, schema_editor):
    Accessory.objects.bulk_create([
        Accessory(name='Accessory 1', type='Type 1', locked=False, code="", price=10, link='link1'),
        Accessory(name='Accessory 2', type='Type 2', locked=False, code="", price=20, link='link2'),
        # Add more accessories as needed
    ])
'''


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                ("petname", models.CharField(max_length=255)),
            ],
        ),
    ]
