# Generated by Django 4.1.10 on 2023-09-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0003_cores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='info_complementares',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
