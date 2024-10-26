from django.contrib import admin
from .models import CarnivorousPost , pterosaursPost ,herbivoresPost
# Register your models here.
class CarnivorousPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_image')
    fields = ('title', 'content', 'image_url', 'image')
    def display_image(self , obj):
        if obj.image_url:
            return f'<img src="{obj.image_url}" width="100" height="100" />'
        elif obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return '(no image)'
    
    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(CarnivorousPost, CarnivorousPostAdmin)


class herbivoresPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_image')
    fields = ('title', 'content', 'image_url', 'image')
    def display_image(self , obj):
        if obj.image_url:
            return f'<img src="{obj.image_url}" width="100" height="100" />'
        elif obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return '(no image)'
    
    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(herbivoresPost, herbivoresPostAdmin)

class pterosaursPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'display_image')
    fields = ('title', 'content', 'image_url', 'image')
    def display_image(self , obj):
        if obj.image_url:
            return f'<img src="{obj.image_url}" width="100" height="100" />'
        elif obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return '(no image)'
    
    display_image.allow_tags = True
    display_image.short_description = 'Image'

admin.site.register(pterosaursPost, pterosaursPostAdmin)
