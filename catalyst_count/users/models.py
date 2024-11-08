from django.db import models

# Create your models here.


class Company(models.Model):
    '''Model to store company data'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=True)
    domain = models.CharField(max_length=250, null=True)
    year_founded = models.FloatField(null=True)
    industry = models.CharField(max_length=500, null=True)
    size_range = models.CharField(max_length=250, null=True)
    locality = models.CharField(max_length=500, null=True)
    country = models.CharField(max_length=150, null=True)
    linkedin_url = models.URLField(null=True)
    current_employee_estimate = models.IntegerField(null=True)
    total_employee_estimate = models.IntegerField(null=True)


class FileUploadDetails(models.Model):
    '''Model to store details of the uploaded file'''
    file = models.FileField(upload_to='uploads/', max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"File {self.id} - {self.file.name}"


class CSVData(models.Model):
    '''Model to store actual csv data'''
    file_upload = models.ForeignKey(FileUploadDetails, related_name='data', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Row from {self.file_upload}"




