# Generated by Django 5.0.6 on 2024-05-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='related',
            field=models.ManyToManyField(blank=True, null=True, to='articles.article'),
        ),
    ]
