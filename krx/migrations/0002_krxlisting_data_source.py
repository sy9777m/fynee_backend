# Generated by Django 3.1.3 on 2020-11-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='krxlisting',
            name='data_source',
            field=models.CharField(default='none', max_length=32),
            preserve_default=False,
        ),
    ]
