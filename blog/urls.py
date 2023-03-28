from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('user_account/', include('django.contrib.auth.urls')),
    path('', include('core.urls'))
]

admin.site.site_header = "Blog Admin"
admin.site.index_title = "Blog administration"

