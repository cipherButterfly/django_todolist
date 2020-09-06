from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import item
import datetime

# Create your views here.

def main_page(request):

    item_list = item.objects.order_by('pk')
    template = loader.get_template('polls/main_page.html')
    now = datetime.datetime.now()
    context = {
        'item' : item_list,
        'now' : now,
    }

    try:
        new_item = request.POST['new_item']
    except (KeyError, item.DoesNotExist):
        return render(request, 'polls/main_page.html',{
            'item' : item_list,
            'now' : now,
            'error_message' : "The box is empty",
        })
    else:
        item.objects.create(item_text = new_item)

        return HttpResponseRedirect(reverse('main_page'))

    return HttpResponse(template.render(context, request))


