# Generated by Django 3.1.2 on 2020-10-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='id',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='name',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
