
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
# is text is white restart vs code editor

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', TokenObtainPairView.as_view(), # for jwTtoken
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),  # for jwTtoken
         name='token_refresh'),
    
    path('api/', include('crud.urls')),
]
