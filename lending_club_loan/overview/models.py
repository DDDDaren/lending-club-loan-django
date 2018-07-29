from django.db import models

# Create your models here.
class LoanStats(models.Model):
	loan_id = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	funded_amount = models.IntegerField()
	purpose = models.models.TextField()

class BrowseNotes(models.Model):
	GRADE_CHOCIES = ['A', 'B', 'C', 'D', 'E', 'F']
	loan_id  = models.CharField(max_length==100)
	title = models.CharField(max_length=100)
	grade = models.CharField(choices=GRADE_CHOCIES, max_length=1, blank=True)
	purpose = models.models.TextField()
	term = models.IntegerField()
