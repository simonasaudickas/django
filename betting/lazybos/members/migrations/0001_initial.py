# Generated by Django 4.2 on 2023-06-07 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('categories', models.ManyToManyField(to='members.category')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('pavadinimas', models.CharField(max_length=100)),
                ('pareigos', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('straipsnis', models.TextField()),
                ('pub_dt', models.DateTimeField(auto_now=True)),
                ('edit_dt', models.DateTimeField()),
                ('foto', models.ImageField(upload_to='static/images/')),
                ('autorius', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.author')),
                ('kategorija', models.ManyToManyField(to='members.category')),
            ],
        ),
    ]
