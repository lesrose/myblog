from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from notes.models import Notes
from datetime import datetime
from utils.mydecorators import confirm_login


# Create your views here.
@confirm_login
def mynotes(request):
    notes = Notes.objects.all()
    completed = Notes.objects.filter(n_is_done=1)
    no_completed = Notes.objects.filter(n_is_done=0)
    return render(request, 'notes/notes.html', {"notes": notes, "completed": completed, "no_completed": no_completed})


@csrf_exempt
def add(request):
    params = request.POST.dict()
    content = params['content']
    c_time = datetime.now()
    note = Notes(n_create_time=c_time, n_content=content)
    note.save()
    data = {"status": 1}
    return JsonResponse(data=data)


@csrf_exempt
def modify(request):
    params = request.POST.dict()
    pk = params['pk']
    is_done = params['is_done']
    note = Notes.objects.filter(pk=pk)
    note = note[0]
    if is_done == "true":
        note.n_is_done = 1
    else:
        note.n_is_done = 0
    note.save()
    data = {"status": 1}
    return JsonResponse(data=data)


def delete(request, pk):
    pk=int(pk)
    Notes.objects.filter(pk=pk).delete()
    # note = Notes.objects.filter(pk=pk)
    # note = note[0]
    # note.delete()
    data = {"status": 1}
    return JsonResponse(data=data)
