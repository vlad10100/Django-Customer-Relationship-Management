# Generated by Django 4.0.1 on 2022-01-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]