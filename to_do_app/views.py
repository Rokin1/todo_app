from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    todo_items = Todo.objects.all().order_by("-date_added")
    return render(request, 'to_do_app/index.html', {"todo_items": todo_items})


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(date_added=current_date, text=content)

    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")













