from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact

# Create your views here.

def frontpage(request):
    return render(request, 'website/frontpage.html')

def about(request):
    return render(request, 'website/about.html')

def we_do(request):
    return render(request, 'website/we_do.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)



        if form.is_valid():

            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            contact = Contact(name=name, number=number, email=email, content=content)
            contact.save()

            print('the form was valid')


            send_mail('The contact form subject', 'This is the message', 'tehmeer012@yahoo.com', ['freelanceali786@gmail.com'])

            return redirect('contact')
        else:
            print('problem with number.')

    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {
        'form': form,
    })
