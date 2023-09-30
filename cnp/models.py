from django.db import models
import uuid # Required for unique indent instances
# Create your models here.

# Indent
class Indent(models.Model):
    indent_Reference = models.IntegerField(unique=True)
    indent_Creation_Date = models.DateField()
    indent_HoD_Release_Date = models.DateField()
    indent_CnP_Release_Date = models.DateField()
    indent_Job = models.CharField(max_length=256)
    indent_Plant = models.CharField(max_length=10)
    indent_Vendor_List = models.ForeignKey('Vendor', on_delete=models.RESTRICT, null=True)
    indent_Cost = models.FloatField()
    indent_Mode_Of_Tendering = models.CharField(max_length=20)
    indent_User = models.ForeignKey('Indentor', on_delete=models.RESTRICT, null=True)
    
    # To control the default ordering of records
    class Meta:
        ordering = []

    def __str__(self):
        return f'{self.indent_Reference}'

# Indentor
class Indentor(models.Model):
    indentor_CPF = models.IntegerField(unique=True)
    indentor_First_name = models.CharField(max_length=20)
    indentor_Last_name = models.CharField(max_length=20)
    indentor_Dept = models.CharField(max_length=20)
    indentor_Designation = models.CharField(max_length=50)
    indentor_Email = models.EmailField()

    # To control the default ordering of records
    class Meta:
        ordering = []
    
    # Represent the record.
    def __str__(self):
        return f'{self.indentor_CPF}'

# Vendor List
class Vendor(models.Model):
    vendor_Reference = models.IntegerField(unique=True)
    vendor_Name = models.CharField(max_length=50)
    vendor_Address = models.CharField(max_length=100)
    vendor_Contact = models.IntegerField()
    vendor_Email = models.EmailField()
    
    # To control the default ordering of records
    class Meta:
        ordering = []

    # Represent the record.
    def __str__(self):
        return f'{self.vendor_Reference}'

# Purchase Order
class Order(models.Model):
    CHOICE = (
        ('y', 'Yes'),
        ('n', 'No'),
    )
    order_Reference = models.IntegerField(unique=True)
    order_Date = models.DateField()
    order_Contractor = models.ForeignKey('Vendor', on_delete=models.RESTRICT, null=True)
    order_Value = models.FloatField()
    order_Contract_Agreement_Submitted = models.BooleanField(max_length=1,choices=CHOICE,blank=True,default='n')
    order_Deposit_Submitted = models.BooleanField(max_length=1,choices=CHOICE,blank=True,default='n')
    order_Security_Deposit_Value = models.FloatField()

    # To control the default ordering of records
    class Meta:
        ordering = []

    # Represent the record.
    def __str__(self):
        return f'{self.order_Reference}'

# IndenstInstance
class IndentInstance(models.Model):
    indent_Instance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular indent')
    indent_Instance_Indent = models.ForeignKey('Indent', on_delete=models.RESTRICT, null=True)
    indent_Instance_Progress_Status = models.CharField(max_length=20)
    indent_Instance_Status = models.CharField(max_length=20)
    indent_Instance_Vendor_List = models.ForeignKey('Vendor', on_delete=models.RESTRICT, null=True)
    indent_Instance_Order = models.ForeignKey('Order', on_delete=models.RESTRICT, null=True)

    # To control the default ordering of records
    class Meta:
        ordering = []

    # Represent the record.
    def __str__(self):
        return f'{self.indent_Instance_id}'
