# Generated by Django 4.0.1 on 2022-01-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Received', 'Received'), ('Scheduled', 'Scheduled'), ('Shipped', 'Shipped'), ('In Progress', 'In Progress')], max_length=100, null=True),
        ),
    ]
