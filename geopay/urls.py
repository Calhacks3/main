from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^transaction/(?P<longitude>\w+)/(?P<latitude>\w+)/(?P<amount>\w+)$',
        views.TransactionHandler.as_view(), name='transaction'),
    url(r'^products/(?P<longitude>\w+)/(?P<latitude>\w+)$',
        views.ProductHandler.as_view(), name='products'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
