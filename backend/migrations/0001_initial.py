# Generated by Django 3.2.7 on 2022-03-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=400)),
                ('isbn', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('pubdate', models.DateField()),
                ('genre', models.IntegerField()),
                ('intro', models.TextField()),
                ('desc', models.TextField()),
                ('desc_pub', models.TextField()),
                ('desc_index', models.TextField()),
            ],
        ),
    ]
