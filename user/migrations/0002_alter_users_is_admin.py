# Generated by Django 3.2.8 on 2022-04-22 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_admin',
            field=models.IntegerField(choices=[(1, '管理员'), (2, '普通用户')], default=1, verbose_name='is_admin'),
        ),
    ]
