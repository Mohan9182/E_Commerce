# Generated by Django 3.1.7 on 2021-06-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210621_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('pic', models.CharField(max_length=15)),
            ],
        ),
    ]
