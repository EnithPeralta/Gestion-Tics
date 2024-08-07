from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appService import views

urlpatterns = [
    path('', views.inicio),
    path('login/', views.login),
    path('inicioAdministrador/', views.inicioAdministrador),
    path('inicioTecnico/', views.inicioTecnico),
    path('inicioEmpleado/', views.inicioEmpleado),
    path('vistaSolicitud/', views.vistaSolicitud),
    path('registroSolicitud/', views.registroSolicitud),
    path('listarCasosAsignar/', views.listarCasos),
    path('asignarTecnico/', views.asignarTecnico),
    path('listarCasosAsignados/', views.listarCasosAsignados),
    path('solucionarCaso/', views.solucionarCaso),
    path('listarSolicitud/', views.listarSolicitudes),
    path('vistaGestionarUsuarios/',views.vistaGestionarUsuarios),
    path('vistaRegistrarUsuario/', views.vistaRegistrarUsuario),
    path('registrarUsuario/', views.registrarUsuario),
    path('recuperarClave/', views.recuperarClave),
    path('generarGrafica/',views.generarGrafica),
    path('pdfSolicitud/',views.generarPdfSolicitd),
    path('salir/', views.salir)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
