# Generated by Django 2.2.1 on 2019-06-13 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=200)),
                ('room_adress', models.CharField(max_length=200)),
                ('room_pass', models.CharField(max_length=200)),
                ('room_add', models.DateTimeField(verbose_name='Date Posted')),
            ],
        ),
    ]