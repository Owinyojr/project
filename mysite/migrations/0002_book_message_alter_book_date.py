# Generated by Django 4.2.7 on 2023-11-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='message',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
