# Generated by Django 2.2.1 on 2019-06-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volai', '0003_auto_20190619_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_viewers',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
