from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^transaction/(?P<merchant_id>\w+)/(?P<amount>\w+)$',
        views.TransactionHandler.as_view(), name='transaction')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
