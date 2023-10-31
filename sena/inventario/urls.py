from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("saludar/<str:nombre>/<str:apellido>/", views.saludar, name="saludar"),
	path("calculadora/<int:num1>/<int:num2>/<str:oper>", views.calculadora, name="calculadora"),

	path("formulario_calc/", views.formulario_calc, name="formulario_calc"),
	path("suma/", views.suma, name="suma"),
]