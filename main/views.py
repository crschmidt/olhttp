# Create your views here.
from django.http import HttpResponse
import django.contrib.gis.geos as geos
from vectorformats.Formats import Django, GeoJSON
from main.models import Data, Other
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

import json

MODELS = {
    'data': {
        'modelclass': Data,
        'fields': ['title', 'description']
    },
    'other': {
        'modelclass': Other,
        'fields': ['title', 'description']
    }
}    

def ui(request):
    return render_to_response("ui.html")

def serialize(features, properties=None):
    if not properties:
        properties = ['title', 'description']
    djf = Django.Django(geodjango="geometry", properties=properties) 
    geoj = GeoJSON.GeoJSON()
    jsonstring = geoj.encode(djf.decode(features))
    return jsonstring

def apply(obj, feature):
    type = feature.geometry['type']
    if type.startswith("Multi"):
        geomcls = getattr(geos, feature.geometry['type'].replace("Multi", ""))
        geoms = []
        for item in feature.geometry['coordinates']:
            geoms.append(geomcls(*item))
        geom = getattr(geos,feateature.geometry['type'])(geoms)    
    else:
        geomcls = getattr(geos, feature.geometry['type'])
        geom = geomcls(*feature.geometry['coordinates'])
    obj.geometry = geom
    for key, value in feature.properties.items():
        setattr(obj, key, value)
    obj.save()    
    return obj


@csrf_exempt
def data(request, type, id=None):
    
    geoj = GeoJSON.GeoJSON()
    modelclass = MODELS[type]['modelclass']
    if id != None:
        obj = modelclass.objects.get(pk=id)
        if request.method != "GET":
            features = geoj.decode(request.raw_post_data)
            obj = apply(obj, features[0])
        return HttpResponse(serialize([obj], MODELS[type]['fields']))
    if request.method == "GET":
        features = modelclass.objects.all()
    else:
        features = geoj.decode(request.raw_post_data)
        created_features = []
        for feature in features:
            obj = modelclass()
            obj = apply(obj, feature)
            obj.save()
            created_features.append(obj)
        features = created_features
    return HttpResponse(serialize(features, MODELS[type]['fields']))
        
