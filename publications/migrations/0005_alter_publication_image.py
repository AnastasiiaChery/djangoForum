# Generated by Django 4.1.3 on 2022-11-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_remove_comment_coment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
