# views.py
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from users.models import FileUploadDetails
from users.tasks import process_file
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CSVData
from users.serializers import CsvDataSerializer
from django.views.generic.base import TemplateView


@login_required(login_url='/accounts/login')
def file_upload_view(request):
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES['file']
        # Read the CSV file into a pandas DataFrame object
        df = pd.read_csv(file, header=None)
        # Get the number of rows in the DataFrame, which is equal to the number of lines in the CSV file
        file_size = df.shape[0]
        file_upload = FileUploadDetails.objects.create(
            file=file,
            file_size=file_size
        )
        
        # Start processing the file asynchronously
        process_file.delay(file_upload.id)

        return JsonResponse({'status': 'success', 'file_id': file_upload.id})
    
    return render(request, 'upload.html')

def get_progress(request, file_id):
    file_upload = FileUploadDetails.objects.get(id=file_id)
    processed = file_upload.data.count()  # Count how many rows are processed
    total = file_upload.file_size  # or you can calculate total rows in CSV
    return JsonResponse({'processed': processed, 'total': total})


class QueryBuilderView(LoginRequiredMixin, TemplateView):
	template_name = 'query_builder.html'



class CsvDataListView(APIView):

    def get(self, request, *args, **kwargs):
        # Get query parameters
        name = request.GET.get('name', None)
        address = request.GET.get('address', None)
        
        # Start with the base queryset
        queryset = CSVData.objects.all()
        
        # Apply filters based on query parameters
        if name:
            queryset = queryset.filter(name__icontains=name)  # Case-insensitive partial match
        if address:
            queryset = queryset.filter(address__icontains=address)  # Case-insensitive partial match
        
        # Get the count of filtered records
        person_count = queryset.count()

        # Serialize the filtered queryset
        serializer = CsvDataSerializer(queryset, many=True)
        
        # Return the filtered data and count
        return Response({
            'count': person_count,
            'results': serializer.data
        })

