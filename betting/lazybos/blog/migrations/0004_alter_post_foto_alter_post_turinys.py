# Generated by Django 4.2 on 2023-07-24 10:19

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_kategorija_post_foto_post_kategorija'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='turinys',
            field=tinymce.models.HTMLField(),
        ),
    ]
