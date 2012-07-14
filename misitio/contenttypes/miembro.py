# -*- coding: utf-8 -*-

from zope import schema
from plone.directives import form

class IMiembro(form.Schema):

    nombre = schema.TextLine(
        title = u"Nombre",
        description = u"Nombre",
        required = True,
        )
    apellido = schema.TextLine(
        title = u"Apellido",
        description = u"Apellido",
        required = True,
        )
    cedula_de_indentidad = schema.TextLine(
        title = u"cedula de indentidad",
        description = u"Cédula de indentidad",
        required = True,
        )
    direcci_n_f_sica = schema.TextLine(
        title = u"Dirección Física",
        description = u"Dirección Fisica",
        required = True,
        )
    direccion_electronica = schema.TextLine(
        title = u"Direccion Electronica",
        description = u"Dirección Electrónica",
        required = False,
        )
    twitter = schema.TextLine(
        title = u"Twitter",
        description = u"Twitter",
        required = False,
        )
