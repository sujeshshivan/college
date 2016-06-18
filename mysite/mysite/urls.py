
from django.conf.urls import url,include 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import index
from .views import contact

urlpatterns = [
	url(r'^$', index ),
	url(r'^index.html/$',index),
    url(r'^contact.html/$',contact),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
