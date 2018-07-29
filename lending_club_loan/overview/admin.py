from django.contrib import admin

# Register your models here.
from .models import LoanStats


@admin.register(LoanStats)
class LoanAdmin(admin.ModelAdmin):
	list_display = ['loan_id', 'title', 'funded_amount', 'purpose', 'description']