# Generated by Django 3.0.5 on 2020-05-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20200511_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='compaign_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]