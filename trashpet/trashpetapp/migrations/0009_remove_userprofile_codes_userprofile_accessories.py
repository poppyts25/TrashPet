# Generated by Django 4.2.9 on 2024-02-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trashpetapp', '0008_merge_0007_accessory_0007_userprofile_codes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='codes',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='accessories',
            field=models.CharField(default='{"cap":False, "crown":False, "socks":False, "bottle":True }', max_length=200),
        ),
    ]
