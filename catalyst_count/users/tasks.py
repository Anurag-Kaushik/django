# tasks.py
import csv
from celery import shared_task
from .models import FileUploadDetails, CSVData
from celery import current_task


@shared_task
def process_file(file_upload_id):
    file_upload = FileUploadDetails.objects.get(id=file_upload_id)
    
    # Get total rows in CSV
    with open(file_upload.file.path, 'r') as file:
        reader = csv.reader(file)
        total_rows = sum(1 for row in reader)
    
    # Process the file
    with open(file_upload.file.path, 'r') as file:
        reader = csv.reader(file)
        processed_rows = 0
        for row in reader:
            if row:  # Ensure the row is not empty
                process_row(file_upload, row)
                processed_rows += 1
                current_task.update_state(state='PROGRESS', meta={'processed': processed_rows, 'total': total_rows})
    
    file_upload.processed = True
    file_upload.save()

def process_row(file_upload, row):
    CSVData.objects.create(
        file_upload=file_upload,
        name=row[0],
        address=row[1],
    )
