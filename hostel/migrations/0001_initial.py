# Generated by Django 2.2 on 2019-07-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('facilities', models.CharField(max_length=100)),
                ('meals', models.CharField(max_length=100)),
                ('name', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('roompic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('passwd', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]