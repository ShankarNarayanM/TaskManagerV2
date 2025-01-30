from myapp.models import TaskBoard
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts task in database"

    def handle(self, *args, **options):
        list_of_task =[
            'Task 1',
            'Task 2',
            'Task 3',
            'Task 4',
            'Task 5',
            'Task 6'
        ]

        list_of_end_date = [
            '2025-06-12',
            '2025-05-07',
            '2025-02-15',
            '2025-04-13',
            '2025-03-21',
            '2025-04-30'
        ]

        list_of_status = [
            'Not completed',
            'In Progress',
            'On hold',
            'In Progress',
            'Completed',
            'In Progress'
        ]

        list_of_priority = [
            'High',
            'Medium',
            'Low',
            'High',
            'Low',
            'Medium'
        ]

        list_of_progress = [
            20,50,70,40,100,25
        ]

        for task, end_date, status, priority, progress in zip(list_of_task,list_of_end_date,list_of_status,list_of_priority,list_of_progress):
            TaskBoard.objects.create(task=task, endDate=end_date,status=status,priority=priority,progress=progress)

        self.stdout.write(self.style.SUCCESS("Completed"))