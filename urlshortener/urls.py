from django.urls import path
from .views import UrlCreateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static

appname = "shortener"

urlpatterns = [
    path('', UrlCreateView.as_view(), name='home'),
    path('<str:shortened_part>', RedirectView.as_view(), name='redirect'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
