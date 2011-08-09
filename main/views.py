# Create your views here.
from django.http import HttpResponse
import django.contrib.gis.geos as geos
from vectorformats.Formats import Django, GeoJSON
from main.models import Data
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

import json

def ui(request):
    return render_to_response("ui.html")

def serialize(features):
    djf = Django.Django(geodjango="geometry", properties=['title', 'description']) 
    geoj = GeoJSON.GeoJSON()
    jsonstring = geoj.encode(djf.decode(features))
    return jsonstring

def apply(obj, feature):
    geomcls = getattr(geos, feature.geometry['type'])
    geom = geomcls(*feature.geometry['coordinates'])
    obj.geometry = geom
    for key, value in feature.properties.items():
        setattr(obj, key, value)
    obj.save()    
    return obj

@csrf_exempt
def data(request, id=None):
    geoj = GeoJSON.GeoJSON()
    if id != None:
        obj = Data.objects.get(pk=id)
        if request.method != "GET":
            features = geoj.decode(request.raw_post_data)
            obj = apply(obj, features[0])
        return HttpResponse(serialize([obj]))
    if request.method == "GET":
        features = Data.objects.all()
    else:
        features = geoj.decode(request.raw_post_data)
        created_features = []
        for feature in features:
            obj = Data()
            obj = apply(obj, feature)
            obj.save()
            created_features.append(obj)
        features = created_features
    return HttpResponse(serialize(features))
        
