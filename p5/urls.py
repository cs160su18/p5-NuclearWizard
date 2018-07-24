from django.contrib import admin
from django.urls import include, path
from life import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('life/', include('life.urls'))
]
