# Generated by Django 4.2.4 on 2023-09-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customuser_customuser_dept_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='CustomUser_Dept',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='CustomUser_Designation',
            field=models.CharField(max_length=50),
        ),
    ]