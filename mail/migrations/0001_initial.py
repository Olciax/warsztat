# Generated by Django 2.0.3 on 2018-09-11 11:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('numofhouse', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('type', models.IntegerField(choices=[(0, 'Nie określono'), (1, 'Służbowy'), (2, 'Prywatny')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mail.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Numer powinien składać się z 9 cyfr.', regex='^\\d{9}$')])),
                ('type', models.IntegerField(choices=[(0, 'Nie określono'), (1, 'Służbowy'), (2, 'Prywatny')], default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Person')),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Person'),
        ),
    ]
