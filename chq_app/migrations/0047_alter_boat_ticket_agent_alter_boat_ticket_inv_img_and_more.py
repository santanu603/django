# Generated by Django 4.1.6 on 2023-09-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chq_app', '0046_boat_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat_ticket',
            name='agent',
            field=models.CharField(blank=True, choices=[('Tinku Das', 'Tinku Das'), ('Biswajit Sanyal', 'Biswajit Sanyal'), ('Rituraj Saran', 'Rituraj Saran'), ('Jeet Roy', 'Jeet Roy'), ('Raju Barui', 'Raju Barui')], max_length=25),
        ),
        migrations.AlterField(
            model_name='boat_ticket',
            name='inv_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='boat_ticket',
            name='retailer_ph',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
