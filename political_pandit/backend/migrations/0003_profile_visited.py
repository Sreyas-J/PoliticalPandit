# Generated by Django 4.2.2 on 2023-08-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_tweet_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='visited',
            field=models.ManyToManyField(related_name='profileName', to='backend.tweet'),
        ),
    ]
