# Generated by Django 5.1.3 on 2024-12-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('vendor', 'Vendor'), ('user', 'User')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
