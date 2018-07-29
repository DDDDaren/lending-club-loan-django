from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from overview.models import LoanStats, BrowseNotes
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from loan.csv into our LoanStats model"

    def handle(self, *args, **options):
        if LoanStats.objects.exists() or BrowseNotes.objects.exists():
            print('Loan data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating loan data")
        print("Loading Loan data")
        for row in DictReader(open('./loan.csv')):
            loan = LoanStats()
            loan.loan_id = row['id']
            loan.title = row['title']
            loan.description = row['desc']
            loan.funded_amount = row['funded_amnt']
            loan.purpose = row['purpose']
            loan.save()
