# Generated by Django 4.2.9 on 2024-03-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trashpetapp', '0008_userprofile_accessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeavesCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('leaves', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='used_codes',
            field=models.CharField(default='', max_length=2000),
        ),


        
    ]