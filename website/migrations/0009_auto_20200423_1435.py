# Generated by Django 3.0.5 on 2020-04-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200423_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
