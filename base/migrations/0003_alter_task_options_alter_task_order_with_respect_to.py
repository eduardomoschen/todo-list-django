# Generated by Django 4.2.3 on 2023-07-29 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_taks_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]