# Generated by Django 3.2.15 on 2022-10-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('tracking_id', models.AutoField(primary_key=True, serialize=False)),
                ('tracking_number', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'tracking',
                'managed': False,
            },
        ),
    ]
