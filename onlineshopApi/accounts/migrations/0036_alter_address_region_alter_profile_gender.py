# Generated by Django 4.0.1 on 2022-01-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_alter_address_region_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Navoi', 'Navoi'), ('Qashqadaryo', 'Qashqadaryo'), ('Fargona', 'Fargona'), ('Samarqand', 'Samarqand'), ('Jizzax', 'Jizzax'), ('Andijon', 'Andijon'), ('Toshkent', 'Toshkent:'), ('Namangan', 'Namangan'), ('Toshkent vil', 'Toshkent vil'), ('Surxondaryo', 'Surxondaryo'), ('Buxoro', 'Buxoro'), ('Xorazm', 'Xorazm')], default='empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True),
        ),
    ]
