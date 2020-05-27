from django.shortcuts import render
from Chef.models import Gallery, Contact
from Chef.forms import ContactForm


def home(request):
    return render(request, 'Chef/index.html')


def gallery_view(request):
    img = Gallery.objects.all()
    return render(request, 'Chef/gallery.html', {'img_gallery': img})


def contact_us(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            all_contact = Contact.objects.create(first_name=data['first_name'], last_name=data['last_name'],
                                                 email=data['email'], message=data['message'])
            all_contact.save()
            print("end")
            return render(request, 'Chef/ContactUs.html', {'success': True})
        else:

            return render(request, 'Chef/ContactUs.html', {'error': True, 'form': form})

    else:
        return render(request, 'Chef/ContactUs.html', {'form': ContactForm()})


def about_us(request):
    return render(request, 'Chef/About Us.html')
