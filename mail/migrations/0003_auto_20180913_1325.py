# Generated by Django 2.0.3 on 2018-09-13 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_address_numofstreet'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='person',
            order_with_respect_to='surname',
        ),
    ]