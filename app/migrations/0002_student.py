# Generated by Django 5.0.7 on 2024-12-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('date_of_enrollment', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
