# Generated by Django 3.0.7 on 2020-09-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0040_auto_20200924_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Teacher/')),
            ],
        ),
    ]