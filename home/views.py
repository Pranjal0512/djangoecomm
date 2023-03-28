from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog_list(request):
    return render(request,'blog_list.html')

def product(request):
    return render(request,'product.html')

def testimonial(request):
    return render(request,'testimonial.html')
