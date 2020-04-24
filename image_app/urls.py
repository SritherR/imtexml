from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
  
urlpatterns = [ 
    path('', hotel_image_view, name = 'image'), 
    path('Image_details', success, name = 'success'), 
 
] 
  
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 