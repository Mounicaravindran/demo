# Generated by Django 4.2 on 2023-04-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
