from django.shortcuts import render
from contact.models import testimonial

# Create your views here.
def service(request):
   feed = testimonial.objects.all()

   return render(request, 'service.html',{'feed':feed,})