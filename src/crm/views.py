from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from .forms import OrderForm
from telebot.sendmassege import sendTelegram

def first_page(request):
    slider_list = CmsSlider.objects.all()
    price_list = PriceCard.objects.all()
    pt_list = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'price_list': price_list,
                'pt_list': pt_list,
                'form': form}
    return render(request, './index.html', dict_obj)

def thanks(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        elem = Order(order_name = name, order_phone = phone)
        elem.save()
        sendTelegram(name, phone)
        return render(request, './thanks.html', {'name': name})
    else:
        return render(request, './thanks.html')
