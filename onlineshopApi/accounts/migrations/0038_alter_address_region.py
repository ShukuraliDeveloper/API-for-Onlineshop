# Generated by Django 4.0.1 on 2022-01-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_alter_address_region_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Jizzax', 'Jizzax'), ('Xorazm', 'Xorazm'), ('Buxoro', 'Buxoro'), ('Surxondaryo', 'Surxondaryo'), ('Qashqadaryo', 'Qashqadaryo'), ('Toshkent vil', 'Toshkent vil'), ('Navoi', 'Navoi'), ('Toshkent', 'Toshkent:'), ('Andijon', 'Andijon'), ('Fargona', 'Fargona'), ('Samarqand', 'Samarqand'), ('Namangan', 'Namangan')], default='empty', max_length=100),
        ),
    ]
