# Generated by Django 4.1.6 on 2023-04-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chq_app', '0039_alter_new_order_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_order',
            name='status',
            field=models.CharField(choices=[('New Order', 'New Order'), ('Pending Order', 'Pending Order'), ('Billed', 'Billed'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=20),
        ),
    ]
