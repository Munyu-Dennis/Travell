# Generated by Django 2.2.6 on 2019-11-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllDestinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('hoteltype', models.CharField(max_length=255)),
                ('inclusive', models.BooleanField(default=False)),
            ],
        ),
    ]
