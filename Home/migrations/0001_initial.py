# Generated by Django 3.2.2 on 2021-05-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_ID', models.IntegerField()),
                ('GRP_ID', models.IntegerField()),
            ],
        ),
    ]