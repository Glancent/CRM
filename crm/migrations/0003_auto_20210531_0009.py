# Generated by Django 3.2.3 on 2021-05-30 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_userprofile_stu_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='menus',
        ),
        migrations.AlterModelOptions(
            name='courserecord',
            options={'verbose_name': '上课记录', 'verbose_name_plural': '上课记录'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': '报名表', 'verbose_name_plural': '报名表'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': '缴费记录', 'verbose_name_plural': '缴费记录'},
        ),
        migrations.AlterModelOptions(
            name='studyrecord',
            options={'verbose_name': '学生学习记录', 'verbose_name_plural': '学生学习记录'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stu_account',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]