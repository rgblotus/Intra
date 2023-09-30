# Generated by Django 4.2.4 on 2023-09-02 14:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indent_Reference', models.IntegerField(unique=True)),
                ('indent_Creation_Date', models.DateField()),
                ('indent_HoD_Release_Date', models.DateField()),
                ('indent_CnP_Release_Date', models.DateField()),
                ('indent_Job', models.CharField(max_length=256)),
                ('indent_Plant', models.CharField(max_length=10)),
                ('indent_Cost', models.FloatField()),
                ('indent_Mode_Of_Tendering', models.CharField(max_length=20)),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Indentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indentor_CPF', models.IntegerField(unique=True)),
                ('indentor_First_name', models.CharField(max_length=20)),
                ('indentor_Last_name', models.CharField(max_length=20)),
                ('indentor_Dept', models.CharField(max_length=20)),
                ('indentor_Designation', models.CharField(max_length=50)),
                ('indentor_Email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_Reference', models.IntegerField(unique=True)),
                ('vendor_Name', models.CharField(max_length=50)),
                ('vendor_Address', models.CharField(max_length=100)),
                ('vendor_Contact', models.IntegerField()),
                ('vendor_Email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_Reference', models.IntegerField(unique=True)),
                ('order_Date', models.DateField()),
                ('order_Value', models.FloatField()),
                ('order_Contract_Agreement_Submitted', models.BooleanField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], default='n', max_length=1)),
                ('order_Deposit_Submitted', models.BooleanField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], default='n', max_length=1)),
                ('order_Security_Deposit_Value', models.FloatField()),
                ('order_Contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnp.vendor')),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='IndentInstance',
            fields=[
                ('indent_Instance_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular indent', primary_key=True, serialize=False)),
                ('indent_Instance_Progress_Status', models.CharField(max_length=20)),
                ('indent_Instance_Status', models.CharField(max_length=20)),
                ('indent_Instance_Indent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnp.indent')),
                ('indent_Instance_Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnp.order')),
                ('indent_Instance_Vendor_List', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnp.vendor')),
            ],
            options={
                'ordering': [],
            },
        ),
        migrations.AddField(
            model_name='indent',
            name='indent_User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnp.indentor'),
        ),
        migrations.AddField(
            model_name='indent',
            name='indent_Vendor_List',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='cnp.vendor'),
        ),
    ]
