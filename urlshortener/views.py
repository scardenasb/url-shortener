from django.http import HttpResponseRedirect, Http404
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Shortener
from .forms import ShortenerForm
from django.views.generic import FormView, RedirectView


class UrlCreateView(FormView):
    form_class = ShortenerForm
    template_name = 'urlshortener/index.html'
    success_message = _("Url correcta")
    success_url = reverse_lazy("urlshortener:home")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(UrlCreateView, self).get_form_kwargs(*args, **kwargs)
        their_url = self.kwargs.get('their_url')
        kwargs['their_url'] = their_url
        return kwargs

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        context = self.get_context_data()
        cd = form.cleaned_data
        cd_url = cd.get('their_url')
        obj = Shortener.objects.create(their_url=cd_url)

        new_url = self.request.build_absolute_uri('/') + obj.my_url
        context['new_url'] = new_url
        context['old_url'] = obj.their_url
        context['form'] = form

        messages.success(self.request, self.success_message)
        return self.render_to_response(context)


class RedirectView(RedirectView):

    template_name = 'urlshortener/index.html'
    model = Shortener

    def get(self, request, shortened_part, *args, **kwargs):
        try:
            shortener = Shortener.objects.get(my_url=shortened_part)

            shortener.times_followed += 1

            shortener.save()

            return HttpResponseRedirect(shortener.their_url)

        except:
            raise Http404('Link broken 👻')
