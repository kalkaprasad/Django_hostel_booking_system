# Generated by Django 3.0.2 on 2020-02-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookservice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('cphone', models.CharField(max_length=12)),
                ('cemail', models.EmailField(max_length=254)),
                ('caddress', models.CharField(max_length=60)),
                ('ctime', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'bookservice',
            },
        ),
        migrations.CreateModel(
            name='mylogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'mylogin',
            },
        ),
        migrations.CreateModel(
            name='upload_data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('files', models.CharField(max_length=200)),
                ('hostelname', models.CharField(max_length=50)),
                ('hostelad', models.CharField(max_length=100)),
                ('hosterate', models.CharField(max_length=20)),
                ('hosteldes', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'upload',
            },
        ),
        migrations.CreateModel(
            name='useraccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'useraccount',
            },
        ),
    ]