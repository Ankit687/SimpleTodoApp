from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todolist_items = TodoItem.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todolist_items})


def addtodolist(request):
    c = request.POST['content']  # create a new todolist all_items
    new_item = TodoItem(content=c)
    new_item.save()
    return HttpResponseRedirect('/todolist/')  # redirect to browser to /todolist/


def deletetodolist(request, todolist_id):
    item_to_delete = TodoItem.objects.get(id=todolist_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todolist/')