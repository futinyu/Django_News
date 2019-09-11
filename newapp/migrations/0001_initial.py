# Generated by Django 2.2.3 on 2019-07-29 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advertis',
            fields=[
                ('priority', models.IntegerField(default=0)),
                ('advImageurl', models.URLField()),
                ('advPageurl', models.URLField()),
                ('advID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('categoryID', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=20, unique=True)),
                ('categoryDes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('nameID', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('passWord', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=12, null=True)),
                ('isAdmin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('newID', models.AutoField(primary_key=True, serialize=False)),
                ('newTitle', models.CharField(max_length=50)),
                ('newOrigin', models.CharField(max_length=20)),
                ('newDate', models.CharField(max_length=20)),
                ('newView', models.IntegerField(default=0)),
                ('newContent', models.TextField()),
                ('newImage', models.URLField()),
                ('newLabel', models.CharField(max_length=40)),
                ('newDes', models.TextField(null=True)),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('commentID', models.AutoField(primary_key=True, serialize=False)),
                ('commentContent', models.TextField()),
                ('commentDate', models.DateTimeField(auto_now_add=True)),
                ('commentFavorite', models.IntegerField(default=0)),
                ('nameID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.users')),
                ('newID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.news')),
            ],
        ),
    ]
