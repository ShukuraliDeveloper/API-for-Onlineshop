# Generated by Django 3.2 on 2022-01-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_address_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Xorazm', 'Xorazm'), ('Toshkent', 'Toshkent:'), ('Qashqadaryo', 'Qashqadaryo'), ('Andijon', 'Andijon'), ('Navoi', 'Navoi'), ('Namangan', 'Namangan'), ('Surxondaryo', 'Surxondaryo'), ('Samarqand', 'Samarqand')], default='empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True),
        ),
    ]
