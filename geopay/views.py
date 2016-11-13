import json
import requests

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Customer, Merchant

API_KEY = '5099880dfe81d420392f11747e919624'

class HomeView(TemplateView):

    template_name = 'geopay/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name)


class TransactionHandler(View):
    def get(self, request, longitude, latitude, amount):
        customer = Customer.objects.get(pk=1)
        merchant = Merchant.objects.get(longitude=longitude, latitude=latitude)
        payload = {
            'merchant_id': merchant.merchant_id, 'medium': 'balance',
            'amount': amount
        }
        url = 'http://api.reimaginebanking.com/accounts/{0}/purchases?key={1}'.format(customer.cust_id, API_KEY)
        response = requests.post(url, json=payload)
        json_data = json.loads(response.text)
        return JsonResponse(json_data)
