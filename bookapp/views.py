from django.shortcuts import render,redirect
from .models import Book
from .forms import Bookcreateform,BookUpdateForm,UserRegistrationForm,Loginform
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_required(func):
    def wrapper(request,id=None):
        if not request.user.is_authenticated:
            return redirect("loginview")
        else:
            return func(request,id)
    return wrapper


def create_book(request):
    if request.user.is_authenticated:
      context={}
      form=Bookcreateform()
      context["form"]=form
      if request.method=="POST":
         form=Bookcreateform(request.POST)
         if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            author=form.cleaned_data.get("author")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            book=Book(book_name=book_name,author=author,price=price,pages=pages)
            book.save()
            print("created books are saved")
         return redirect("listbook")
      return render(request,"bookapp/createbook.html",context)
    else:
        return redirect("loginview")

def list_all_book(request):
    if request.user.is_authenticated:
        books=Book.objects.all()
        context={}
        context["books"]=books
        return render(request,"bookapp/listallbooks.html",context)
    else:
        return redirect("loginview")

@login_required
def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("listbook")

@login_required
def update_book(request,id):
    book=Book.objects.get(id=id)
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbook")
    return render(request,"bookapp/editbook.html",context)

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginview")
        else:
            context["form"]=form
        return render(request,"bookapp/registration.html",context)
    return render(request,"bookapp/registration.html",context)

def django_login(request):
    form=Loginform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"bookapp/home.html")
            else:
                context["form"]=form
                return render(request,"bookapp/login.html",context)
    return render(request,"bookapp/login.html",context)

def django_logout(request):
    logout(request)
    return redirect("loginview")