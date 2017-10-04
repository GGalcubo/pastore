# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponse
from django.utils.translation import ugettext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Empleado, Show, Especialidad, Equipo, TipoEquipo
import json
import datetime

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    mensaje = 'INDEX'
    
    context = {'mensaje': mensaje,}
    return render(request, 'index.html', context)

@login_required    
def dashboard(request):
    mensaje = ''
    context = {'mensaje': mensaje,}
    return render(request, 'dashboard.html', context)


@login_required
def empleados(request):
    mensaje = ''
    empleados = Empleado.objects.filter(activo=True)
    especialidades = Especialidad.objects.all()
    context = {'mensaje': mensaje, 'empleados': empleados, 'especialidades': especialidades, }
    return render(request, 'empleados.html', context)

@login_required    
def dame_empleado(request):
    id_empleado = request.GET.get('id_empleado')
    empleado = Empleado.objects.get(id=id_empleado)
    if empleado.especialidad:
        id_espe = empleado.especialidad.id
    else:
        id_espe = 0
    nac = empleado.nacimiento.strftime('%d-%m-%Y')
    dict = {'id_empleado': empleado.id, 'nombre': empleado.nombre, 'apellido': empleado.apellido, 'nacimiento': nac, 'email': empleado.mail, 'domicilio': empleado.domicilio,'comentario': empleado.comentario, 'dni': empleado.dni, 'id_especialidad':id_espe }
    return HttpResponse(json.dumps(dict), content_type="application/json")

@login_required    
def eliminar_empleado(request):
    id_empleado = request.POST.get('id_empleado')
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.activo = False
    empleado.save()

    dict = {'id_empleado': empleado.id }
    return HttpResponse(json.dumps(dict), content_type="application/json")

@login_required    
def guardar_empleado(request):
    mensaje = ''
    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            id_empleado = request.POST.get('id_empleado')
            nombre      = request.POST.get('nombre')
            apellido    = request.POST.get('apellido')
            email       = request.POST.get('email')
            domicilio   = request.POST.get('domicilio')
            nacimiento  = request.POST.get('nacimiento')
            comentario  = request.POST.get('comentario')
            dni  		= request.POST.get('dni')
            id_especialidad = request.POST.get('especialidad')

            if id_empleado == "":
                empleado = Empleado()
            else:
                empleado = Empleado.objects.get(id=id_empleado)
                
            empleado.nombre = nombre
            empleado.apellido = apellido
            empleado.mail = email
            empleado.domicilio = domicilio

            if nacimiento == '':
                nacimiento = '1900-01-01'
            else:
                nacimiento = nacimiento[6:] +'-'+ nacimiento[3:5] +'-'+ nacimiento[0:2]
                
            empleado.nacimiento = nacimiento
            empleado.comentario = comentario
            empleado.dni = dni
            empleado.especialidad = Especialidad.objects.get(id=id_especialidad)
            empleado.save()
            

        except Exception as e:
            mensaje = str(e)
            
    dict = {'error': mensaje}
    return HttpResponse(json.dumps(dict), content_type="application/json")
    
@login_required    
def shows(request):
    mensaje = ''
    id_show = ''
    shows = Show.objects.filter(activo=True)
    context = {'mensaje': mensaje, 'shows': shows, 'id_show': id_show}
    return render(request, 'shows.html', context)

@login_required    
def dame_show(request):
    id_show = request.GET.get('id_show')
    show = Show.objects.get(id=id_show)
    nac = show.nacimiento.strftime('%d-%m-%Y')
    dict = {'id_show': show.id, 'nombre': show.nombre, 'lugar': show.lugar, 'duracion': show.duracion, 'comentario': show.comentario,}
    return HttpResponse(json.dumps(dict), content_type="application/json")
    
@login_required    
def eliminar_show(request):
    id_show = request.POST.get('id_show')
    show = Show.objects.get(id=id_show)
    show.activo = False
    show.save()

    dict = {'id_show': show.id }
    return HttpResponse(json.dumps(dict), content_type="application/json")

@login_required    
def guardar_show(request):
    mensaje = ''
    
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            id_show  = request.POST.get('id_show')
            nombre      = request.POST.get('nombre')
            lugar    = request.POST.get('lugar')
            duracion    = request.POST.get('duracion')
            comentario  = request.POST.get('comentario')

            if id_show == "":
                show = Show()
            else:
                show = Show.objects.get(id=id_show)
                
            show.nombre = nombre
            show.lugar = lugar
            show.duracion = duracion
            show.comentario = comentario
            show.save()

        except Exception as e:
            mensaje = str(e)
            
    dict = {'error': mensaje}
    return HttpResponse(json.dumps(dict), content_type="application/json")

@login_required    
def equipos(request):
    mensaje = ''
    id_equipo = ''
    equipos = Equipo.objects.filter(activo=True)
    tipos_equipo = TipoEquipo.objects.all()
    context = {'mensaje': mensaje, 'equipos': equipos, 'id_equipo': id_equipo, 'tipos_equipo': tipos_equipo}
    return render(request, 'equipos.html', context)

@login_required    
def guardar_equipo(request):
    mensaje = ''

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            id_equipo         = request.POST.get('id_equipo')
            nombre              = request.POST.get('nombre')
            comentario              = request.POST.get('comentario')
            tipo_equipo           = request.POST.get('tipo_equipo')

            if id_equipo == "":
                equipo = Equipo()
            else:
                equipo = Equipo.objects.get(id=id_equipo)
                
            equipo.equipo = nombre
            equipo.tipo_equipo = TipoEquipo.objects.get(id=tipo_equipo)
            equipo.save()

        except Exception as e:
            mensaje = str(e)

    dict = {'error': mensaje}
    return HttpResponse(json.dumps(dict), content_type="application/json")

@login_required    
def dame_equipo(request):
    id_equipo = request.GET.get('id_equipo')
    equipo = Equipo.objects.get(id=id_equipo)

    dict = {'id_equipo': equipo.id, 'nombre': equipo.equipo, 'tipo_equipo': equipo.tipo_equipo.id, 'comentario': equipo.comentario,}
    return HttpResponse(json.dumps(dict), content_type="application/json")

@login_required    
def eliminar_equipo(request):
    id_equipo = request.POST.get('id_equipo')
    equipo = Equipo.objects.get(id=id_equipo)
    equipo.activo = False
    equipo.save()

    dict = {'id_equipo': equipo.id }
    return HttpResponse(json.dumps(dict), content_type="application/json")

