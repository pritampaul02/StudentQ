# Generated by Django 4.1.7 on 2023-03-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0010_tutorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='topic',
            field=models.CharField(default='public', max_length=500),
        ),
    ]
