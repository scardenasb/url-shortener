from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Shortener
from .forms import ShortenerForm

# Create your views here.

def home_view(request):
    template = 'urlshortener/index.html'
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():

            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.my_url

            their_url = shortened_object.their_url

            context['new_url'] = new_url
            context['their_url'] = their_url

            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(my_url=shortened_part)

        shortener.times_followed += 1

        shortener.save()

        return HttpResponseRedirect(shortener.their_url)

    except:
        raise Http404('Link broken 👻')
