# Generated by Django 3.2.16 on 2022-12-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=512)),
                ('price', models.IntegerField()),
            ],
        ),
    ]