from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is my HomePage(/)")
    context = {'name':'Biswa','job':'Software Developer','ctc':12.5}
    return render(request,'home.html',context)
def about(request):
    # return HttpResponse("This is my about(/)")
    return render(request,'about.html')
def projects(request):
    # return HttpResponse("This is my projects(/)")
    return render(request,'projects.html')
def contact(request):
    # return HttpResponse("This is my contact(/)")
    return render(request,'contact.html')