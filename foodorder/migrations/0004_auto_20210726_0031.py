# Generated by Django 3.1 on 2021-07-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0003_auto_20210713_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ddcard',
            old_name='foodorder',
            new_name='orderid',
        ),
        migrations.RemoveField(
            model_name='orderhist',
            name='ubillno',
        ),
        migrations.RemoveField(
            model_name='orderhist',
            name='udate',
        ),
    ]