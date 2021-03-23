from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('TASK.urls')),
    path('TASK_API/', include('TASK_API.urls')),
    path('admin/', admin.site.urls),

]
