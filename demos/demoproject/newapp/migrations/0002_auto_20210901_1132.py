# Generated by Django 3.2.6 on 2021-09-01 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='image',
            field=models.ImageField(default=5.497828357798669e-05, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='name',
            field=models.CharField(default=5.497828357798669e-05, max_length=250),
            preserve_default=False,
        ),
    ]