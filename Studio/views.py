from django.shortcuts import render
from Studio.models import Photo, Contact


def index(request):
    return render(request, "Studio/index.html")


def about(request):
    return render(request, "Studio/about.html")


def service(request):
    return render(request, "Studio/service.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'Studio/contact.html')


def portfolio(request):
    photos = Photo.objects.all()
    params = {'photo': photos}
    return render(request, "Studio/portfolio.html", params)


def portfoliomodel(request, id):
    photos = Photo.objects.filter(id=id)
    return render(request, "Studio/portfoliomodel.html", {'photo': photos[0]})

