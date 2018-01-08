from django.contrib import admin
from django import forms
# Register your models here.
from caps.models import *

from input_mask.widgets import InputMask
from django.http import HttpResponse
from django.core import serializers


#
# class Telefone(InputMask):
#     mask = {
#         'mask': '(99) 99999-9999',
#     }
#
class Cpf(InputMask):
    mask = {
        'mask': '999.999.999-99',
    }


from django import forms


#from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput
#from localflavor.br.forms import BRPhoneNumberField



from reportlab.pdfgen import canvas



def teste(modeladmin, request, queryset):
    c = canvas.Canvas("hello.pdf")

    step=750
    for qs in queryset:
        c.drawString(30, step, qs.nome)
        step -= 100

    c.save()

