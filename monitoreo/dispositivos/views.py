from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def inicio(request):
    return HttpResponse("Hola desde Django")


def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]

    # Límite de consumo permitido
    consumo_maximo = 100

    # Agregar un campo para indicar si está dentro o fuera del límite
    for d in dispositivos:
        d["estado"] = "Dentro del límite" if d["consumo"] <= consumo_maximo else "Excede el límite"

    return render(request, "dispositivos/panel.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })
    