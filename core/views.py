from django.shortcuts import render
from contact.models import testimonial

# Create your views here.
def home(request):
    feed = testimonial.objects.all()
    return render(request, 'home.html', {'feed':feed})