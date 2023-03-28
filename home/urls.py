from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('blog_list', blog_list, name='blog_list'),
    path('product', product, name='product'),
    path('testimonial', testimonial, name='testimonial'),

]
