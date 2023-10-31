from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, "inventario/index.html")


def saludar(request, nombre, apellido):
	return HttpResponse(f"Hola <strong style='color:red;'>{nombre} {apellido}</strong>")


def calculadora(request, num1, num2, oper):
	if oper == "mas":
		r = num1 + num2
	elif oper == "menos":
		r = num1 - num2
	elif oper == "por":
		r = num1 * num2
	elif oper == "entre":
		if num2 != 0:
			r = num1 / num2
		else:
			r = "Error"
	else:
		return HttpResponse("Operador no válido..")

	return HttpResponse(f"{num1} {oper} {num2} = <strong style='color:red;'>{r}</strong>")


def formulario_calc(request):
	return render(request, "inventario/formulario_calc.html")

def suma(request):
	n1 = int(request.POST.get("num1"))
	n2 = int(request.POST.get("num2"))
	r = n1 + n2
	return HttpResponse(f"= <strong style='color:red;'>{r}</strong>")