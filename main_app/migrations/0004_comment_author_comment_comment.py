# Generated by Django 4.1.3 on 2022-11-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_comment_author_remove_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='', max_length=500),
        ),
    ]
