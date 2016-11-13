import json
import requests

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Customer, Merchant

from django.forms.models import model_to_dict

API_KEY = '5099880dfe81d420392f11747e919624'

class HomeView(TemplateView):

    template_name = 'geopay/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name)


class TransactionHandler(View):
    def get(self, request, longitude, latitude, amount, description=None):
        """Description is a dictionary"""
        customer = Customer.objects.get(pk=1)
        merchant = Merchant.objects.get(longitude=longitude, latitude=latitude)
        payload = {
            'merchant_id': merchant.merchant_id, 'medium': 'balance',
            'amount': amount
        }
        if description:
            sentence = ''
            for k, v in description:
                if v:
                    sentence += '{0},'.format(k)
            payload['description'] = description

        url = 'http://api.reimaginebanking.com/accounts/{0}/purchases?key={1}'.format(customer.cust_id, API_KEY)
        response = requests.post(url, json=payload)
        json_data = json.loads(response.text)
        return JsonResponse(json_data)


class ProductHandler(View):
    def get(self, request, longitude, latitude):
        merchant = Merchant.objects.get(longitude=longitude, latitude=latitude)
        json_data = {'products': []}
        for product in merchant.products.all():
            json_data['products'].append({product.name: float(product.price)})
        return JsonResponse(json.dumps(json_data, ensure_ascii=False), safe=False)
