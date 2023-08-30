from atexit import register
from django.contrib import admin

from website.models import enquiry_table

# Register your models here.

admin.site.register(enquiry_table)

