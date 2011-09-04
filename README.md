A simple demo using GeoDjango, vectorformats, and OpenLayers
to do simple editing of PostGIS tables on a webserver.

To setup:

1. Install GeoDjango
2. Install vectorformats (easy_install vectorformats)
3. git clone https://github.com/crschmidt/olhttp.git
4. cd olhttp
5. python manage.py syncdb
6. python manage.py runserver
7. Go to http://localhost:8000/ui/

You can sketch, edit, and save to your heart's content.

UI is easily configurable for more/different layers, using
LAYER_CONFIG in javascript and MODELS in main/views.py.
