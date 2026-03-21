from django.core.management.base import BaseCommand, CommandError
from bagsearch.models import VacuumBags

from bagsearch.pushdata import push_new_data

class Command(BaseCommand):
    help="Pushing newly processed image text into database."

    def handle(self, *args, **kwargs):
        push_new_data()
        print("Inserted new data.")





    # Subclassing BaseCommand. Requires implementation of handle()
