# Generated by Django 3.0.5 on 2020-05-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_auto_20200516_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='compaign_name',
            field=models.CharField(max_length=100),
        ),
    ]