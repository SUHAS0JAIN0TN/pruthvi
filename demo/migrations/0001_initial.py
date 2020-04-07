# Generated by Django 3.0.5 on 2020-04-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_preference_and_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64, unique=True)),
                ('service_appointments', models.IntegerField(default=2)),
                ('finance', models.CharField(default='010', max_length=3)),
                ('smart_home_care', models.CharField(default='010', max_length=3)),
                ('smart_car_care', models.CharField(default='010', max_length=3)),
                ('vacation_planning', models.CharField(default='010', max_length=3)),
            ],
        ),
    ]
