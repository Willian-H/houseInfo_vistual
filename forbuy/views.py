from django.shortcuts import render

# Create your views here.
import json

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from forbuy import models


def add_buymsg(request):
    if request.method == 'POST':
        buymsg = models.forbuy()
        buymsg.houseaddress = request.POST.get("address")
        buymsg.houseprice = request.POST.get("price")
        buymsg.housearea = request.POST.get("area")
        buymsg.housedescription = request.POST.get("description")
        buymsg.linkman = request.POST.get("linkman")
        buymsg.contact = request.POST.get("contact")
        buymsg.save()
        return HttpResponseRedirect("/forbuy/show_buymsg/")


def add_buymsg_to(request):
    return render(request, 'add_buymsg.html')


def del_buymsg(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        buymsg = models.forbuy.objects.get(pk=id)
        buymsg.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


# def update_rentmsg(request):

def show_buymsg(request):
    buymsg_all = models.forbuy.objects.all()
    data = {
        'rentmsg_all': buymsg_all
    }

    return render(request, 'form_buymsg.html', context=data)


def show_buymsg_all_bypage(request):
    # select * from Student limit 1,10
    buymsg_all = models.forbuy.objects.all()
    lis = []
    for buymsg in buymsg_all:
        data = dict()
        data['id'] = buymsg.id
        data['address'] = buymsg.houseaddress
        data['price'] = buymsg.houseprice
        data['area'] = buymsg.housearea
        data['description'] = buymsg.housedescription
        data['linkman'] = buymsg.linkman
        data['contact'] = buymsg.contact
        lis.append(data)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里
    house_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    msgs = {"code": 0, "msg": "", "count": buymsg_all.count(), "data": house_info}
    return JsonResponse(msgs)


def modify_buymsg_ajax(request):
    # if request.method == 'POST':
    #     # id = request.POST.get("id")
    #     id = 2
    #     rentmsg = models.forrent.objects.get(pk=id)
    #     rentmsg.houseaddress = request.POST.get("address")
    #     rentmsg.houseprice = request.POST.get("price")
    #     rentmsg.housearea = request.POST.get("area")
    #     rentmsg.housedescription = request.POST.get("description")
    #     rentmsg.linkman = request.POST.get("linkman")
    #     rentmsg.contact = request.POST.get("contact")
    #     rentmsg.save()
    #     data = {
    #         'msg': "success"
    #     }
    #     return JsonResponse(data)
    if request.method == 'POST':
        buymsg = models.forbuy.objects.get(linkman=request.POST.get("linkman"))
        buymsg.houseaddress = request.POST.get("address")
        buymsg.houseprice = request.POST.get("price")
        buymsg.housearea = request.POST.get("area")
        buymsg.housedescription = request.POST.get("description")
        buymsg.linkman = request.POST.get("linkman")
        buymsg.contact = request.POST.get("contact")
        buymsg.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)

