# Generated by Django 3.2.16 on 2023-01-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy_meters', '0002_auto_20230113_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='id',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='ID del medidor'),
        ),
    ]
