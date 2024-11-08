from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_upload_view, name='file_upload'),
    path('progress/<int:file_id>/', views.get_progress, name='get_progress'),
    path('query/builder', views.QueryBuilderView.as_view(), name='query_builder'),
    path('api/query/', views.CsvDataListView.as_view(), name='query_builder_api'),
]
