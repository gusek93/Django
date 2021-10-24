from . import views
from django.urls import path, register_converter


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(YearConverter, 'year')

app_name = 'instagram'  # URL Reverse 에서 namespace 역할


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    #path('archives/<year:year>/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
]
