from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_requests = requests.get("https://api.iex.cloud/v1/data/core/quote/"+ticker+"?token=pk_d1ba4b2f2b464890853bd41f7a2f9594")

        try:
            api = json.loads(api_requests.content)[0]
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': 'Enter a ticker ....'})


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock have been added"))
            return redirect('add_stock')

    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})









# Stock quote for Apple:
#
# https://api.iex.cloud/v1/data/core/quote/aapl?token=YOUR_TOKEN
#
# Fundamentals for Microsoft:
#
# https://api.iex.cloud/v1/data/core/fundamentals/msft?token=YOUR_TOKEN
#
# Cash flow for Tesla:
#
# https://api.iex.cloud/v1/data/core/cash_flow/tsla?token=YOUR_TOKEN&last=4