from django.contrib import admin
from documento.models import Requisito, Asunto, Tipo_Documento, Estado_Documento, Area, Remitente, Documento,Documento_generado, Usuario
from django import forms
from django.contrib.auth.models import User

class RemitenteAdmin(admin.ModelAdmin):
    list_display = ('mom_pernat','documento','nro_documento')
    search_fields = ('documento','mom_pernat')
    fieldsets = (
        ('Datos del remitenet', {
            'fields': ('mom_pernat',('documento','nro_documento'),'dir_perjurd'),
        }),
    )
    list_filter = ['documento']
    valid_lookups = ('documento')
admin.site.register(Remitente, RemitenteAdmin)


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('remitente','area','tipodoc','asunto','estado','ver_seguimiento','ver_historial','archivo')
    search_fields = ('asunto__nom_asunto','remitente__mom_pernat')
    fieldsets = (
        ('Datos del Documento', {
            'fields': ('area','remitente','tipodoc','asunto','archivo','folios','observacion'),
        }),
    )
    raw_id_fields = ('remitente',)
    list_filter = ['asunto__nom_asunto','tipodoc__nom_tipo_doc']
    valid_lookups = ('asunto')

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()

    def queryset(self, request):
        qs = super(DocumentoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
admin.site.register(Documento, DocumentoAdmin)

admin.site.register(Requisito)
admin.site.register(Asunto)
admin.site.register(Tipo_Documento)
admin.site.register(Estado_Documento)
admin.site.register(Area)
admin.site.register(Usuario)
admin.site.register(Documento_generado)
