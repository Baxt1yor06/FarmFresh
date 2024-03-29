from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Index_carousel)
class Index_carouselAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Carousel_footer)
class Carousel_footerAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    prepopulated_fields = {"slug": ('name',)}
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Farmers)
class FarmersAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    prepopulated_fields = {"slug": ('name',)}




admin.site.register(Features)
admin.site.register(Recent_posts)
admin.site.register(News)
admin.site.register(Commets)
admin.site.register(Contact)