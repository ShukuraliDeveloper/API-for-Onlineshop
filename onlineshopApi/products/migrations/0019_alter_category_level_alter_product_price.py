# Generated by Django 4.0.1 on 2022-01-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_category_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('3', '3')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='price'),
        ),
    ]