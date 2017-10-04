# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode
import datetime

# Create your models here.
class TipoEquipo(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    comentario = models.TextField('Comentario', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Equipos" 
        ordering = ('nombre',)

class Especialidad(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    comentario = models.TextField('Comentario', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Especialidades" 
        ordering = ('nombre',)

class Equipo(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    tipo_equipo = models.ForeignKey(TipoEquipo)
    caracteristicas = models.TextField('Características', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


    class Meta:
        verbose_name_plural = "Equipos" 
        ordering = ('nombre',)

class Empleado(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    dni = models.CharField('Documento', max_length=30)
    nacimiento = models.DateField('Nacimiento', default=datetime.date.today)
    domicilio = models.CharField('Domicilio', max_length=100, null=True, blank=True)
    mail = models.CharField('Mail', max_length=100, null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, null=True, blank=True)    
    comentario = models.TextField('Comentario', null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Empleados" 
        ordering = ('nombre',)


class Show(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    lugar = models.CharField('Lugar', max_length=100)
    duracion = models.CharField('Duración', max_length=100, null=True, blank=True)
    comentario = models.TextField('Comentario', null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
        
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Shows" 
        ordering = ('nombre',)
        

class DetalleShow(models.Model):
	show = models.ForeignKey(Show)
	equipo = models.ForeignKey(Equipo)
	empleado = models.ForeignKey(Empleado)

	def __str__(self):
		return self.show.nombre

	def __unicode__(self):
		return self.show.nombre

	class Meta:
		verbose_name_plural = "Detalle Shows"
		ordering = ('show',)