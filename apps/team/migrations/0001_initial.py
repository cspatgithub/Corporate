# Generated by Django 3.0.5 on 2020-08-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='staff_images')),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
