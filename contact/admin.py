from django.contrib import admin
from .models import contact, testimonial
from django.contrib.auth.models import Group

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name','email','subject','message',
    )

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('fullname','feedback','position',)
    fields =( 
        'feedback','fullname', 'position',
    )


admin.site.register(contact, ContactAdmin)
admin.site.register(testimonial, TestimonialAdmin)
admin.site.unregister(Group)
