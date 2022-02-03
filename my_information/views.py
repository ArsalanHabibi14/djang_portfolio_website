from django.shortcuts import render, redirect
from .models import MyInformation
from .models import MyProjectsWork, Contacts
from .models import MyServices, MyCategorySkills
from .forms import ContactForm


# 451 x 211
def main_page(request):
    user = MyInformation.objects.get_active_user()
    category = MyCategorySkills.objects.all()
    services = MyServices.objects.all()
    blogs = MyProjectsWork.objects.all()
    contact_form = ContactForm(request.POST or None)
    context = {
        'user': user,
        'categories': category,
        'services': services,
        'blogs': blogs,
        'contact_form': contact_form
    }
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        Contacts.objects.create(full_name=full_name, email=email, message=message)
        context['contact_form'] = ContactForm()
        return redirect('Thanks')
    else:
        print("Error")
    return render(request, 'index.html', context)


def blog_detail(request, *args, **kwargs):
    user = MyInformation.objects.get_active_user()
    blog_id = kwargs.get('blog_id')
    blog = MyProjectsWork.objects.filter(id=blog_id).first()
    context = {
        'user': user
    }
    if blog is not None:
        context['blog'] = blog
    return render(request, 'blog-post-1.html', context)


def Thanks_page(request):
    user = MyInformation.objects.get_active_user()
    context = {
        'user': user
    }
    return render(request, 'Thanks.html', context)
