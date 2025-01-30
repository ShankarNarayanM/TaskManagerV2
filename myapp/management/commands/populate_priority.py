from myapp.models import PriorityModel
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts priority in database"

    def handle(self, *args, **options):
        list_of_priority = [
            'Low',
            'Medium',
            'High'
        ]

        for priority in list_of_priority:
            PriorityModel.objects.create(priority=priority)

        self.stdout.write(self.style.SUCCESS("Completed"))