from django.shortcuts import render
from .models import Events
from django.urls import reverse
from django.http import  HttpResponseRedirect, JsonResponse


# Create your views here.

def calendar(request ):
    context = { "events": Events.objects.all()}
    return render(request,'calendar.html',context)

def eventoformulario(request,msn):
    contexto = {'msn': msn}
    return render(request, 'Calendario/calendar', contexto)


from Apps.Muelitas.models import Usuario

def add_event(request):
    try:
        event = Events(
            name=request.POST['name'],
            start=request.POST['start'],
            end=request.POST['end'],
            documento=Usuario.objects.get(id=int(request.POST['documento'])),
            valor=request.POST['valor'],

        )
        event.save()
        return HttpResponseRedirect(reverse('calendario:calendar', args=('')))
    except Exception as e:
        return HttpResponseRedirect(reverse('calendario:calendar', args=(e,)))



def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)