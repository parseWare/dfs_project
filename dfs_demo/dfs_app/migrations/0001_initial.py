# Generated by Django 4.0.3 on 2022-04-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dfs_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('roll_no', models.IntegerField(default=0)),
                ('image', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('contact', models.IntegerField(default=0)),
            ],
        ),
    ]
