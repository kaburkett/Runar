# Generated by Django 3.0.8 on 2020-07-31 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0004_auto_20200731_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='encryption',
        ),
        migrations.DeleteModel(
            name='Encryption',
        ),
    ]