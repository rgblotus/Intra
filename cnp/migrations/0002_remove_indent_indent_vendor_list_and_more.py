# Generated by Django 4.2.4 on 2023-09-02 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indent',
            name='indent_Vendor_List',
        ),
        migrations.AddField(
            model_name='indent',
            name='indent_Vendor_List',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnp.vendor'),
        ),
    ]
