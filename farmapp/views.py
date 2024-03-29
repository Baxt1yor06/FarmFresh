from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import *

# Create your views here.

# Base templates 
def index(request):
    home1 = Index_carousel.objects.all()
    home2 = Carousel_footer.objects.all()
    home3 = About.objects.all()
    home4 = Service.objects.all()
    home5 = Features.objects.all()
    home6 = Products.objects.all()
    home7 = Client.objects.all()
    home8 = Farmers.objects.all()
    home9 = Posts.objects.all()
    context = {
      'home1' : home1,
      'home2' : home2,
      'home3' : home3,
      'home4' : home4,
      'home5' : home5,
      'home6' : home6,
      'home7' : home7,
      'home8' : home8,
      'home9' : home9
      } 
    return render(request, 'index.html', context=context)


def about(request):
    about1 = About.objects.all()
    about2 = Farmers.objects.all()
    context = {
        'about1' : about1,
        'about2' : about2
    }
    return  render(request, 'about.html', context=context)


def service(request):
    service1 = Service.objects.all()
    service2 = Client.objects.all()
    context = {
        'service1' : service1,
        'service2' : service2
    }
    return render(request, 'service.html', context=context)

def product(request):
    product1 = Products.objects.all()
    product2 = Features.objects.all()
    context = {
        'product1' : product1,
        'product2' : product2
    }
    return render(request,'product.html', context=context)

def blog_grid(request):
    blog_grid1 = Posts.objects.all()
    blog_grid2 = Recent_posts.objects.all()
    context = {
        'blog1' : blog_grid1,
        'blog2' : blog_grid2
    }
    return render(request,'blog.html', context=context)

def blog_detail(request):
    blog_detail1 = News.objects.all()
    blog_detail2 = Recent_posts.objects.all()
    blog_detail3 = Commets.objects.all()
    context = {
       'detail1' : blog_detail1,
       'detail2' : blog_detail2, 
       'detail3' : blog_detail3    
    }
    return render(request, 'detail.html', context=context)

def feature(request): 
    feature = Features.objects.all()
    context = {
        'feature' : feature
    }
    return render(request, 'feature.html', context=context)

def team(request):
    team = Farmers.objects.all()
    context = {
        'team' : team
    }
    return render(request, 'team.html', context=context)

def client(request):
    client = Client.objects.all()
    context = {
        'client' : client
    }
    return render(request, 'testimonial.html', context=context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Sizning malumotingiz qabul qilindi</h1>")
    context = {
        'form': form
    }
    return render(request,'contact.html',context=context)




# Detail templates

def detail1(request,home1):
    home1 = get_object_or_404(Index_carousel, slug=home1)
    context = {
        'home1': home1
    }
    return render(request,'details/detail1.html',context=context)

def detail2(request,home2):
    home2 = get_object_or_404(Carousel_footer, slug=home2)
    context = {
        'home2': home2
    }
    return render(request,'details/detail2.html',context=context)


def detail3(request,home3):
    home3 = get_object_or_404(About, slug=home3)
    context = {
        'home3' : home3
    }
    return render(request,'details/detail3.html',context=context)


def detail4(request,home6):
    home4 = get_object_or_404(Service, slug=home4)
    context = {
        'home4' : home4
    }
    return render(request,'details/detail4.html',context=context)


def detail6(request,home6):
    home6 = get_object_or_404(Products, slug=home6)
    context = {
        'home6' : home6
    }
    return render(request,'details/detail6.html',context=context)


def detail7(request,home7):
    home7 = get_object_or_404(Client, slug=home7)
    context = {
        'home7': home7
    }
    return render(request,'details/detail7.html',context=context)

def detail8(request,home8):
    home8 = get_object_or_404(Farmers, slug=home8)
    context = {
        'home8': home8
    }
    return render(request,'details/detail8.html',context=context)

def detail9(request,home9):
    home9 = get_object_or_404(Posts, slug=home9)
    context = {
        'home9': home9
    }
    return render(request,'details/detail7.html',context=context)





# Change views
    

class CarouselUpdateView(UpdateView):
    model = Index_carousel
    fields = ('__all__')
    template_name = 'Change_templates/CarouselUpdateView.html'
class CarouselDeleteView(DeleteView):
    model = Index_carousel
    template_name = 'Change_templates/CarouselDeleteView.html'
    success_url = reverse_lazy('index')
class CarouselCreateView(CreateView):
    model = Index_carousel
    template_name = 'Change_templates/CarouselCreateView.html'
    fields = "__all__"

class AboutUpdateView(UpdateView):
    model = About
    fields = ('__all__')
    template_name = 'Change_templates/AboutUpdateView.html'
class AboutDeleteView(DeleteView):
    model = About
    template_name = 'Change_templates/AboutDeleteView.html'
    success_url = reverse_lazy('index')
class AboutCreateView(CreateView):
    model = About
    template_name = 'Change_templates/AboutCreateView.html'
    fields = "__all__"


class CarouselfooterUpdateView(UpdateView):
    model = Carousel_footer
    fields = ('__all__')
    template_name = 'Change_templates/CarouselfooterUpdateView.html'
class CarouselfooterDeleteView(DeleteView):
    model = Carousel_footer
    template_name = 'Change_templates/CarouselfooterDeleteView.html'
    success_url = reverse_lazy('index')
class CarouselfooterCreateView(CreateView):
    model = Carousel_footer
    template_name = 'Change_templates/CarouselfooterCreateView.html'
    fields = "__all__"


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('__all__')
    template_name = 'Change_templates/ClientUpdateView.html'
class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'Change_templates/ClientDeleteView.html'
    success_url = reverse_lazy('index')
class ClientCreateView(CreateView):
    model = Client
    template_name = 'Change_templates/ClientCreateView.html'
    fields = "__all__"



class FarmersUpdateView(UpdateView):
    model = Farmers
    fields = ('__all__')
    template_name = 'Change_templates/FarmersUpdateView.html'
class FarmersDeleteView(DeleteView):
    model = Farmers
    template_name = 'Change_templates/FarmersDeleteView.html'
    success_url = reverse_lazy('index')
class FarmersCreateView(CreateView):
    model = Farmers
    template_name = 'Change_templates/FarmersCreateView.html'
    fields = "__all__"


class PostUpdateView(UpdateView):
    model = Posts
    fields = ('__all__')
    template_name = 'Change_templates/PostUpdateView.html'
class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'Change_templates/PostDeleteView.html'
    success_url = reverse_lazy('index')
class PostCreateView(CreateView):
    model = Posts
    template_name = 'Change_templates/PostCreateView.html'
    fields = "__all__"



class ProductUpdateView(UpdateView):
    model = Products
    fields = ('__all__')
    template_name = 'Change_templates/ProductUpdateView.html'
class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'Change_templates/ProductDeleteView.html'
    success_url = reverse_lazy('index')
class ProductCreateView(CreateView):
    model = Products
    template_name = 'Change_templates/ProductCreateView.html'
    fields = "__all__"


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ('__all__')
    template_name = 'Change_templates/ServiceUpdateView.html'
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'Change_templates/ServiceDeleteView.html'
    success_url = reverse_lazy('index')
class ServiceCreateView(CreateView):
    model = Service
    template_name = 'Change_templates/ServiceCreateView.html'
    fields = "__all__"



