# Generated by Django 4.0.3 on 2022-05-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0018_user_number_banned'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.TextField(null=True),
        ),
    ]
