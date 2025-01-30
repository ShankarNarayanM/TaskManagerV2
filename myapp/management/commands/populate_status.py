from myapp.models import StatusModel
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts status in database"

    def handle(self, *args, **options):
        list_of_status = [
            'Not completed',
            'In Progress',
            'On hold',
            'Completed',
        ]

        for status in list_of_status:
            StatusModel.objects.create(status=status)

        self.stdout.write(self.style.SUCCESS("Completed"))