from django.shortcuts import render

# Create your views here.
import json

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from forrent import models


def add_rentmsg(request):
    if request.method == 'POST':
        rentmsg = models.forrent()
        rentmsg.houseaddress = request.POST.get("address")
        rentmsg.houseprice = request.POST.get("price")
        rentmsg.housearea = request.POST.get("area")
        rentmsg.housedescription = request.POST.get("description")
        rentmsg.linkman = request.POST.get("linkman")
        rentmsg.contact = request.POST.get("contact")
        rentmsg.save()
        return HttpResponseRedirect("/forrent/show_rentmsg/")


def add_rentmsg_to(request):
    return render(request, 'add_rentmsg.html')


def del_rentmsg(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        rentmsg = models.forrent.objects.get(pk=id)
        rentmsg.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


# def update_rentmsg(request):

def show_rentmsg(request):
    rentmsg_all = models.forrent.objects.all()
    data = {
        'rentmsg_all': rentmsg_all
    }

    return render(request, 'form_rentmsg.html', context=data)


def show_rentmsg_all_bypage(request):
    # select * from Student limit 1,10
    rentmsg_all = models.forrent.objects.all()
    lis = []
    for rentmsg in rentmsg_all:
        data = dict()
        data['id'] = rentmsg.id
        data['address'] = rentmsg.houseaddress
        data['price'] = rentmsg.houseprice
        data['area'] = rentmsg.housearea
        data['description'] = rentmsg.housedescription
        data['linkman'] = rentmsg.linkman
        data['contact'] = rentmsg.contact
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
    msgs = {"code": 0, "msg": "", "count": rentmsg_all.count(), "data": house_info}
    return JsonResponse(msgs)


def modify_rentmsg_ajax(request):
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
        rentmsg = models.forrent.objects.get(linkman=request.POST.get("linkman"))
        rentmsg.houseaddress = request.POST.get("address")
        rentmsg.houseprice = request.POST.get("price")
        rentmsg.housearea = request.POST.get("area")
        rentmsg.housedescription = request.POST.get("description")
        rentmsg.linkman = request.POST.get("linkman")
        rentmsg.contact = request.POST.get("contact")
        rentmsg.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)
