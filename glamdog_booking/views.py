from django.shortcuts import render


# Create your views here.


def home_view(request):
    return render(request, "pages/home.html", {})


def signup_view(request):

    return render(request, "allauth/account/signup.html", {})


def about_view(request):
    return render(request, "pages/about.html", {})


def contact_view(request):
    return render(request, "pages/contact.html", {})


def services_view(request):
    return render(request, "pages/services.html", {})
