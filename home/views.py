from django.shortcuts import render
from.models import *
# Create your views here.
def home(request):
    views={}
    views['services']= Service.objects.all()
    views['products']= Product.objects.all()
    views['ads']= Ad.objects.all()
    views['testimonials']= Testimonial.objects.all()
    views['informations']= Information.objects.all()
    views['sliders']= Slider.objects.all()
    return render(request,'index.html',views)

def about(request):
    views = {}
    views['services'] = Service.objects.all()
    views['ads'] = Ad.objects.all()


    return render(request,'about.html',views)

def contact(request):
    views = {}
    views['ads'] = Ad.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            message=message,

        )
    return render(request,'contact.html')

def blog_list(request):
    views = {}
    views['services'] = Service.objects.all()
    return render(request,'blog_list.html',views)

def product(request):
    views = {}
    views['products'] = Product.objects.all()
    return render(request,'product.html',views)

def testimonial(request):
    views = {}
    views['testimonials'] = Testimonial.objects.all()
    return render(request,'testimonial.html',views)
