# Generated by Django 5.0.3 on 2024-03-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
