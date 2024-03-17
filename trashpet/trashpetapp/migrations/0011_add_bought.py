
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('trashpetapp', '0010_rename_code_leavescode_name_and_more'),
    ]

    operations = [
        migrations.AddField(
                    model_name="userprofile",
                    name="bought",
                    field=models.CharField(
                        default='{"Cap": false, "Crown": false, "Socks": false, "Bottle": false}',
                        max_length=200,
                    ),
                ),
    ]