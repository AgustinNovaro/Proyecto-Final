from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime as datetime
from django.shortcuts import render, redirect
from recetas.forms import RecetaForm
# import tkinter as tk

# def pantalla_inicial(request):
#     if request.method == 'GET':
#         # Crear la ventana principal
#         ventana = tk.Tk()

#         # Crear los botones
#         crear_receta = tk.Button(ventana, text="Crear Receta", command=crear_receta)
#         actualizar_receta = tk.Button(ventana, text="Actualizar Receta", command=actualizar_receta)
#         detalle_receta = tk.Button(ventana, text="Detalle Receta", command=detalle_receta)
#         listar_recetas = tk.Button(ventana, text="Listar Recetas", command=listar_recetas)

#         # Posicionar los botones en la ventana
#         crear_receta.pack()
#         actualizar_receta.pack()
#         detalle_receta.pack()
#         listar_recetas.pack()

#         # Iniciar el bucle principal de la ventana
#         ventana.mainloop()

#     return render(request, './recetas/plantillas/crear_receta.html')

def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')  # Redirigir a la lista de recetas
    else:
        form = RecetaForm()
    
    return render(request, 'crear_receta.html', {'form': form})

from django.shortcuts import render, get_object_or_404

def lista_recetas(request):
    recetas = RecetaForm.objects.all()
    return render(request, './recetas/plantillas/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(RecetaForm, pk=receta_id)
    return render(request, './recetas/plantillas/detalle_receta.html', {'receta': receta})

from django.shortcuts import render, get_object_or_404

def actualizar_receta(request, receta_id):
    receta = get_object_or_404(RecetaForm, pk=receta_id)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('detalle_receta', receta_id=receta_id)  # Redirigir al detalle de la receta actualizada
    else:
        form = RecetaForm(instance=receta)
    
    return render(request, './recetas/plantillas/actualizar_receta.html', {'form': form})

# def recetas(request):
#     dic = {"Titulo": "Torta", "Sabor": "Limón"}

#     mi_html = open('./recetas/plantillas/index.html')

#     plantilla = Template(mi_html.read())

#     mi_html.close()

#     contexto = Context(dic)

#     docu = plantilla.render(contexto)

#     return HttpResponse(docu)