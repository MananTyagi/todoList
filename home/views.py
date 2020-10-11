from django.shortcuts import render, HttpResponse
from home.models import Tasks

# Create your views here.
def home(request):
    context={'success':False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        ins= Tasks(title=title, desc=desc)
        ins.save()
        context={'success':True}
        
    return render(request,'index.html', context)
def tasks(request):
    alltasks=Tasks.objects.all()
    print(alltasks)
    for item in alltasks:
        print(item.title)
    context={'tasks':alltasks}
    return render(request,'tasks.html', context)