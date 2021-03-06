# Generated by Django 3.1 on 2020-11-06 16:44

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=120)),
                ('number', models.CharField(max_length=20)),
                ('message', djrichtextfield.models.RichTextField()),
            ],
        ),
    ]
