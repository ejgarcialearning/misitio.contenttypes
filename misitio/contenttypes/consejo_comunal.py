# -*- coding: utf-8 -*-

from zope import schema
from plone.directives import form

class IConsejoComunal(form.Schema):

    ubicacion = schema.Text(
        title = u"Ubicacion",
        description = u"Direccion",
        required = True,
        )

    persona_de_contacto = schema.TextLine(
        title = u"Persona de Contacto",
        description = u"Contacto",
        required = True,
        )

    correo = schema.TextLine(
        title = u"correo",
        description = u"correo electronico",
        required = False
        )

    telefono = schema.TextLine(
        title = u"Telefono",
        description = u"telefono",
        required = False
        )

