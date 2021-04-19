# Generated by Django 3.1.6 on 2021-03-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listvehicle', '0005_easysafe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]