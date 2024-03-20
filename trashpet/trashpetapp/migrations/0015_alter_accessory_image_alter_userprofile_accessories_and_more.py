# Generated by Django 5.0.3 on 2024-03-19 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trashpetapp", "0014_accessory_link_alter_accessory_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessory",
            name="image",
            field=models.ImageField(default="cap.png", upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="accessories",
            field=models.CharField(default="{}", max_length=200),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="bought",
            field=models.CharField(default="{}", max_length=200),
        ),
    ]
