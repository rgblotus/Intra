from django.contrib import admin

from cnp.models import Indent, IndentInstance, Indentor, Order, Vendor
# Register your models here.

admin.site.register(Indent)

admin.site.register(Indentor)

admin.site.register(Vendor)

admin.site.register(Order)

admin.site.register(IndentInstance)