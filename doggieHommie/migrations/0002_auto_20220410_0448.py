# Generated by Django 3.1.2 on 2022-04-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggieHommie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holi', models.CharField(max_length=40)),
                ('prueba', models.CharField(max_length=40)),
                ('kk', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
