# Generated by Django 5.1 on 2024-09-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='kavi@gmail.com', max_length=254),
        ),
    ]
