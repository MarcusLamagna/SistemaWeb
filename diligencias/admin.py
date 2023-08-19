from django.contrib import admin

from diligencias.models import Diligencia


# Cruiando a classe DiligenciaAdmin
class DiligenciaAfmin(admin.ModelAdmin):
    # quais campso da classe serão exibidos
    list_display = ['nome', 'data_realizacao', 'dinheiro_apreendido']
    search_fields = ['nome']
    list_filter = ['data_realizacao']


# Register your models here.
admin.site.register(Diligencia, DiligenciaAfmin)
