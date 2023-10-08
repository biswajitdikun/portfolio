from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("This is my HomePage(/)")
    context = {'name':'Biswa','job':'Software Developer'}
    return render(request,'home.html',context)
def about(request):
    # return HttpResponse("This is my about(/)")
    return render(request,'about.html')
def projects(request):
    # return HttpResponse("This is my projects(/)")
    return render(request,'projects.html')
def contact(request):
    # return HttpResponse("This is my contact(/)")
    if request.method == "POST":
        form = request.POST
        name = form['name']
        email = form['email']
        phone = form['phone']
        desc = form['desc']
        # print(form)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print("data has been written")
    return render(request,'contact.html')