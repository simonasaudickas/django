# Generated by Django 4.2 on 2023-07-18 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_createarticleform_alter_article_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='id',
            new_name='auto_increment_id',
        ),
    ]
