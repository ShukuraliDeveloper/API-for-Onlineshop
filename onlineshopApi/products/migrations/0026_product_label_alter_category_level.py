# Generated by Django 4.0.1 on 2022-01-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_product_available_alter_category_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'Secondary'), ('D', 'danger')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('3', '3'), ('2', '2'), ('1', '1')], max_length=200, null=True),
        ),
    ]
