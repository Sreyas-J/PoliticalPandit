# Generated by Django 4.2.2 on 2023-08-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_option_alter_profile_points_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='users',
            field=models.ManyToManyField(related_name='questions', to='backend.profile'),
        ),
    ]