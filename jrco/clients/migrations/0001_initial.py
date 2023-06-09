# Generated by Django 4.2 on 2023-04-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='clients/')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
