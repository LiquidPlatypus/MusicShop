# Generated by Django 5.1.5 on 2025-01-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_alter_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(default='/static/img/default.jpg', upload_to='photos/'),
        ),
    ]
