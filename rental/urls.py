from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # API urls
    path('api/auth/', include('rental.apps.users.api.urls', namespace='users')),
    path('api/profiles', include('rental.apps.profiles.api.urls', namespace='profiles'))
]

