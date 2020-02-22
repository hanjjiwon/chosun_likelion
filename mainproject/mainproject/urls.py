
from django.contrib import admin
from django.urls import path, include
import mainapp.views
import account.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.home, name="home"),
    path('account/', include('account.urls')),

]

