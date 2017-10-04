# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Especialidad, Show, DetalleShow, Empleado, TipoEquipo, Equipo
# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_max_show_all = 1000
    list_per_page = 400

    list_display = ('nombre', 'tipo_equipo', 'caracteristicas','activo')
    fieldsets = (
        ('Principal', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('nombre', 'tipo_equipo', 'caracteristicas','activo')
        }),
    )

class DetalleShowInline(admin.TabularInline):
    model = DetalleShow
    extra = 0

class ShowAdmin(admin.ModelAdmin):
    inlines = [
        DetalleShowInline
    ]
    list_max_show_all = 1000
    list_per_page = 400

    list_display = ('nombre', 'lugar', 'duracion', 'comentario', 'activo')
    fieldsets = (
        ('Principal', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('nombre', 'lugar', 'duracion', 'comentario','activo')
        }),
    )

class EmpleadoAdmin(admin.ModelAdmin):
    list_max_show_all = 1000
    list_per_page = 400

    list_display = ('nombre', 'apellido', 'dni', 'nacimiento', 'domicilio', 'mail', 'especialidad', 'comentario','activo')
    fieldsets = (
        ('Principal', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('nombre', 'apellido', 'dni', 'nacimiento', 'domicilio', 'mail', 'especialidad', 'comentario','activo')
        }),
    )


admin.site.register(TipoEquipo)
admin.site.register(Especialidad)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(DetalleShow)