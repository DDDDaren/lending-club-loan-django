from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import LoanStats

def home(request):
	loans = LoanStats.objects.all()

	return render(request, 'home.html', {'loans': loans})


def loan_detail(request, loan_id):
	try:
		loan = LoanStats.objects.get(loan_id=loan_id)
	except LoanStats.DoesNotExist:
		raise Http404('Loan not found')
	return render(request, 'loan_detail.html', {'loan': loan})
