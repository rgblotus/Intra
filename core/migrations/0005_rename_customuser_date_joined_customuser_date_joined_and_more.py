# Generated by Django 4.2.4 on 2023-09-18 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_customuser_customuser_dept_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_Date_Joined',
            new_name='date_joined',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_Dept',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_is_Active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_is_Staff',
            new_name='is_staff',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_First_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_Mobile_Number',
            new_name='mobile_number',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='CustomUser_User_Name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='CustomUser_Designation',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='CustomUser_Last_name',
        ),
    ]
