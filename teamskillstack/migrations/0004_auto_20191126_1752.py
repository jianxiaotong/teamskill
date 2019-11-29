# Generated by Django 2.1.4 on 2019-11-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamskillstack', '0003_auto_20191121_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='验证码')),
                ('email', models.EmailField(max_length=100, verbose_name='验证码')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=50, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(auto_now=True, verbose_name='发送时间')),
            ],
            options={
                'db_table': 'emailRecord',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='邮箱'),
        ),
    ]
