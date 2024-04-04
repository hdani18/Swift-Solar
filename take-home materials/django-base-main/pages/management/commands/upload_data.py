import csv
from datetime import datetime
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.conf import settings
from pages import models

class Command(BaseCommand):
    def upload_data(self):
        csv_file_path = '/Users/harshil/Desktop/take-home materials/events_data.csv'
        if not models.Event.objects.exists():
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    event_date_str = row[0]
                    event_date = datetime.strptime(event_date_str, '%B %d, %Y').date()
                    event_name = row[1]
                    event_description = row[2]
                    tags = [tag.strip() for tag in row[3].split(',')]
                    link_to_info = row[4]

                    event = models.Event.objects.create(
                        event_date=event_date,
                        event_name=event_name,
                        event_description=event_description,
                        additional_info_link=link_to_info
                    )

                    for tag_name in tags:
                        tag, created = models.Tag.objects.get_or_create(name=tag_name)
                        
                        event_tag = models.EventTag.objects.create(event=event, tag=tag)

            self.stdout.write(self.style.SUCCESS('CSV data successfully uploaded to the database.'))
        else:
            self.stdout.write(self.style.WARNING('Database already populated with CSV data.'))
    def handle(self, *args: Any, **options: Any) -> str | None:
        return self.upload_data()
        
