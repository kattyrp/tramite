from django.utils import simplejson
from django.core import serializers
from documento.models import Requisito, Asunto, Tipo_Documento, Estado_Documento, Area, Remitente, Documento, Documento_generado, Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from documento.forms import DocumentoForm
from django.db.models import Q
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

def list_historial(request, documento_id):
    try:
        detalle_documento=Documento_generado.objects.get(id=documento_id)
        ctx = {'documento_detalle':detalle_documento}
        return render_to_response('historiales.html',ctx,context_instance=RequestContext(request))
    except:
        return render_to_response('notificacion.html',context_instance=RequestContext(request))

def list_usuario(request, area_id):
    usuario=Usuario.objects.filter(Area_id=area_id)    
    data = serializers.serialize('json',usuario)
    return HttpResponse(data,mimetype='application/json')

def guardar_documento(request, documento_id):
    area=Area.objects.all()
    usuario=Usuario.objects.all()
    detalle_documento=Documento.objects.get(id=documento_id)
    if request.method == 'POST':
        post = request.POST
        documentoId = post['id_documento']
        usuarioRemitente = post['usuario']
        areaRemitente = post['area_remitente']
        observacion = post['observacion']                 
        area_derivada = post['areas']
        opciones = post['opciones']
        try:
            remitente_derivado = post['usuarios']   
        except:
            remitente_derivado = post['usuario']        
        dg=Documento_generado()
        dg.usuario_id = usuarioRemitente
        dg.documento_id = documentoId
        dg.destinatario_id = remitente_derivado
        try:
            a = Area.objects.get(pk = area_derivada)
            dg.area= a
        except:
            a = Area.objects.get(pk = areaRemitente)
        dg.estado = opciones
        dg.observacion = observacion
        dg.save()
        return HttpResponseRedirect('/admin/documento/documento/')

    else:
        try:
            Documento_generado.objects.get(documento_id=documento_id)
            ctx = {'documento_detalle':detalle_documento,'area':area,'usuario':usuario}
            return render_to_response('documento.html',ctx,context_instance=RequestContext(request))
        except :    
            ctx = {'documento_detalle':detalle_documento,'area':area,'usuario':usuario}
            return render_to_response('documentos.html',ctx,context_instance=RequestContext(request))