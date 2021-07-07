from django.shortcuts import redirect, render
from .models import Plataforma, Series
from .forms import SeriesForm

# Create your views here.

def home (request):
    return render (request, "core/home.html")

def contactanos (request):
    return render (request, "core/contactanos.html")

def iniciar_sesion (request):
    return render (request, "core/iniciar_sesion.html")

def registro (request):
    return render (request, "core/registro.html")

def nosotros (request):
    return render (request, "core/nosotros.html")

def series_netflix(request):
    data = {"list": Series.objects.filter(plataforma ="1").order_by('nombre')}
    return render(request, "core/series_netflix.html", data)

def series_disney(request):
    data = {"list": Series.objects.filter(plataforma ="2").order_by('nombre')}
    return render(request, "core/series_disney.html", data)

def series_amazon(request):
    data = {"list": Series.objects.filter(plataforma ="3").order_by('nombre')}
    return render(request, "core/series_amazon.html", data)


def serie_ficha(request, id):
    series = Series.objects.get(nombre=id)
    data ={"series":series}
    return render (request, "core/serie_ficha.html", data) 
  
def series(request, action, id):
    data = {"mesg": "", "form": SeriesForm, "action": action, "id": id}
 
    if action == 'ins':
        if request.method == "POST":
            form = SeriesForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡La serie fue creada correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos series con el mismo nombre!"
 
    elif action == 'upd':
        objeto = Series.objects.get(nombre=id)
        if request.method == "POST":
            form = SeriesForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡La serie fue actualizada correctamente!"
        data["form"] = SeriesForm(instance=objeto)
 
    elif action == 'del':
        try:
            Series.objects.get(nombre=id).delete()
            data["mesg"] = "¡La serie fue eliminada correctamente!"
            return redirect(series, action='ins', id = '-1')
        except:
            data["mesg"] = "¡La serie ya estaba eliminado!"
 
    data["list"] = Series.objects.all().order_by('nombre')
    return render(request, "core/series.html", data)





