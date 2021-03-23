from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('GetImagefileDetails/', views.GetImagefileDetails.as_view()),
    path('GetImagefileDetails/<pk>', views.GetImagefileDetails.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)