# Generated by Django 2.0 on 2019-12-20 06:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogarticles',
            options={'ordering': ('-publish',), 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 20, 6, 35, 18, 108329, tzinfo=utc)),
        ),
    ]