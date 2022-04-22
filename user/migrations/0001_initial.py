# Generated by Django 3.2.8 on 2022-04-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('is_admin', models.CharField(default=0, max_length=1, verbose_name='是否为管理员，1：是，0：不是')),
            ],
            options={
                'verbose_name': '用户登录表',
                'verbose_name_plural': '用户登录表',
                'db_table': 'user_login',
            },
        ),
    ]
