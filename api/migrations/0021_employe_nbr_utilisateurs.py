# Generated by Django 4.1.3 on 2023-01-02 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_rename_conversationi_message_historique_historiquei'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='nbr_utilisateurs',
            field=models.IntegerField(default=0),
        ),
    ]
