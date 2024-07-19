from django.urls import path
from .apiViews import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('oficina/', OficinaList.as_view()),
    path('oficina/<int:pk>/', OficinaDetail.as_view()),
    path('usuario/', UserList.as_view()),
    path('usuario/<int:pk>/', UserDetail.as_view()),
    path('userApi/', UserApi.as_view()),
    path('oficina/', Oficina_APIView.as_view()),
    path('docs/', include_docs_urls(title='Documentación API')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)