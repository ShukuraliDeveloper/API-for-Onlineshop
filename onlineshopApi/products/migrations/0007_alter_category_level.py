# Generated by Django 4.0.1 on 2022-01-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=200, null=True),
        ),
    ]
