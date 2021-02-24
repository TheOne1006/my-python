# Generated by Django 3.1.6 on 2021-02-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_Id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief', models.TextField()),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]