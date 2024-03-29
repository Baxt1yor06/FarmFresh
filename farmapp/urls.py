from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('product', product, name='product'),
    path('blog_grid', blog_grid, name='blog'),
    path('blog_detail', blog_detail, name='detail'),
    path('feature', feature, name='feature'),
    path('team', team, name='team'),
    path('client', client, name='client'),
    path('contact', contact, name='contact'),



    path('home1/<slug:home1>', detail1, name='detail1'),
    path('home2/<slug:home2>', detail2, name='detail2'),
    path('home3/<slug:home3>', detail3, name='detail3'),
    path('home4/<slug:home4>', detail4, name='detail4'),
    path('home6/<slug:home6>', detail6, name='detail6'),
    path('home7/<slug:home7>', detail7, name='detail7'),
    path('home8/<slug:home8>', detail8, name='detail8'),
    path('home9/<slug:home9>', detail9, name='detail9'),


    path('home1/update/<slug>/', CarouselUpdateView.as_view(), name='CarouselUpdateView'),
    path('home1/delete/<slug>/', CarouselDeleteView.as_view(), name='CarouselDeleteView'),
    path('home1/create/', CarouselCreateView.as_view(), name='CarouselCreateView'),
    path('home3/update/<slug>/', AboutUpdateView.as_view(), name='AboutUpdateView'),
    path('home3/delete/<slug>/', AboutDeleteView.as_view(), name='AboutDeleteView'),
    path('home3/create/', AboutCreateView.as_view(), name='AboutCreateView'),
    path('home2/update/<slug>/', CarouselfooterUpdateView.as_view(), name='CarouselfooterUpdateView'),
    path('home2/delete/<slug>/', CarouselfooterDeleteView.as_view(), name='CarouselfooterDeleteView'),
    path('home2/create/', CarouselfooterCreateView.as_view(), name='CarouselfooterCreateView'),
    path('home7/update/<slug>/', ClientUpdateView.as_view(), name='ClientUpdateView'),
    path('home7/delete/<slug>/', ClientDeleteView.as_view(), name='ClientDeleteView'),
    path('home7/create/', ClientCreateView.as_view(), name='ClientCreateView'),
    path('home8/update/<slug>/', FarmersUpdateView.as_view(), name='FarmersUpdateView'),
    path('home8/delete/<slug>/', FarmersDeleteView.as_view(), name='FarmersDeleteView'),
    path('home8/create/', FarmersCreateView.as_view(), name='FarmersCreateView'),
    path('home9/update/<slug>/', PostUpdateView.as_view(), name='PostUpdateView'),
    path('home9/delete/<slug>/', PostDeleteView.as_view(), name='PostDeleteView'),
    path('home9/create/', PostCreateView.as_view(), name='PostCreateView'),
    path('home6/update/<slug>/', ProductUpdateView.as_view(), name='ProductUpdateView'),
    path('home6/delete/<slug>/', ProductDeleteView.as_view(), name='ProductDeleteView'),
    path('home6/create/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('home4/update/<slug>/', ServiceUpdateView.as_view(), name='ServiceUpdateView'),
    path('home4/delete/<slug>/', ServiceDeleteView.as_view(), name='ServiceDeleteView'),
    path('home4/create/', ServiceCreateView.as_view(), name='ServiceCreateView'),

]
