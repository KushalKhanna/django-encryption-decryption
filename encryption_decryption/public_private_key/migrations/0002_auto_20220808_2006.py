# Generated by Django 3.1.1 on 2022-08-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_private_key', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=5000),
        ),
    ]