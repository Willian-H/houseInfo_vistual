# Generated by Django 2.2 on 2021-07-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseaddress', models.CharField(max_length=255)),
                ('houseprice', models.CharField(max_length=255)),
                ('housearea', models.CharField(max_length=255)),
                ('housedescription', models.CharField(max_length=255)),
                ('linkman', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
    ]
