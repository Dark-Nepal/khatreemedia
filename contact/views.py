from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def contact(request):
    if request.method == 'POST':
       filledform = ContactForm(request.POST)
       if filledform.is_valid():
        note = 'Your message is sent !!'
        filledform.save()
        newform = ContactForm()
        return render(request, 'contact.html',{
            'form' : ContactForm,
            'note' : note
        })

    else:
        newform = ContactForm()    
        return render(request, 'contact.html', {'form' : newform })

   
