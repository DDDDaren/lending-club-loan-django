from django.contrib import admin

# Register your models here.
from .models import LoanStats


class LoanAdmin(admin.ModelAdmin):
	pass