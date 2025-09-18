from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse("<h1>Django API is running!</h1><p>API endpoints available at <a href='/api/v1/tracks/'>/api/v1/tracks/</a></p>")




def health_check(request):
    return JsonResponse({"status": "ok"})



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('health/', health_check),
    path('api/v1/', include(("apps.routers", "apps"), namespace="core-api"))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)