import json

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from zhenghe import models


# Create your views here.

def to_login(request):
    return render(request, 'login.html')


def add_user(request):
    user = models.User()
    if request.method == 'POST':
        if (request.POST.get("password") == request.POST.get("check")):
            user.username = request.POST.get("username")
            user.password = request.POST.get("password")
            user.save()
            return render(request, 'login.html')
        else:
            data = {
                'error': '您输入的密码不一致！请重新输入'
            }
            return render(request, 'add_user.html', context=data)


def add_user_to(request):
    return render(request, 'add_user.html')


def check_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        rs = models.User.objects.filter(username=username).filter(password=password)
        if rs.exists():
            # 登录验证成功
            # return HttpResponseRedirect('/house/menu/')
            return render(request, 'main_menu.html')
        else:
            # 登陆失败
            data = {
                'error': '您输入的用户名或密码有误！请重新输入'
            }
            return render(request, 'login.html', context=data)


def menu(request):
    return render(request, 'main_menu.html')


def welcome(request):
    return render(request, 'welcome.html')


# 二手房视图
def showall_secondhand(request):
    houseInfo = models.SecondHouse.objects.all()
    data = {
        'houseInfo': houseInfo
    }

    return render(request, 'form_secondhand.html', context=data)


# def to_showall_secondhand_echarts(request):
#     return render(request, 'echarts_secondhand.html')


def showall_secondhand_echarts(request):
    # if request.method == "POST":
    houseInfo = models.SecondHouse.objects.all()
    pricevalue1 = pricevalue2 = pricevalue3 = pricevalue4 = pricevalue5 = 0
    areavalue1 = areavalue2 = areavalue3 = areavalue4 = areavalue5 = areavalue6 = areavalue7 = areavalue8 = areavalue9 = areavalue0 = 0
    for house in houseInfo:
        pricetemp = float(house.houseprice)
        if pricetemp >= 0 and pricetemp < 100:
            pricevalue1 += 1
        elif pricetemp >= 100 and pricetemp < 120:
            pricevalue2 += 1
        elif pricetemp >= 120 and pricetemp < 140:
            pricevalue3 += 1
        elif pricetemp >= 140 and pricetemp < 160:
            pricevalue4 += 1
        else:
            pricevalue5 += 1
        areatemp = float(house.housearea)
        if areatemp >= 0 and areatemp < 50:
            areavalue1 += 1
        elif areatemp >= 50 and areatemp < 60:
            areavalue2 += 1
        elif areatemp >= 60 and areatemp < 70:
            areavalue3 += 1
        elif areatemp >= 70 and areatemp < 80:
            areavalue4 += 1
        elif areatemp >= 80 and areatemp < 90:
            areavalue5 += 1
        elif areatemp >= 90 and areatemp < 100:
            areavalue6 += 1
        elif areatemp >= 100 and areatemp < 110:
            areavalue7 += 1
        elif areatemp >= 110 and areatemp < 120:
            areavalue8 += 1
        elif areatemp >= 120 and areatemp < 130:
            areavalue9 += 1
        else:
            areavalue0 += 1

    areavalue = [areavalue1, areavalue2, areavalue3, areavalue4, areavalue5, areavalue6, areavalue7, areavalue8,
                 areavalue9, areavalue0]
    pricevlaue = [pricevalue1, pricevalue2, pricevalue3, pricevalue4, pricevalue5]
    keys = ['价格100万以内', '价格100-120万', '价格120-140万', '价格140-160万', '价格160万以上']
    data = {}
    for k, v in zip(keys, pricevlaue):
        data.update({k: v, }, )
    print(areavalue, pricevlaue)
    return render(request, 'echarts_secondhand.html', {'data': json.dumps(data), 'area': json.dumps(areavalue)})


def show_secondhouse_all_bypage(request):
    # select * from Student limit 1,10
    houseInfo = models.SecondHouse.objects.all()
    lis = []
    for house in houseInfo:
        data = dict()
        data['id'] = house.id
        data['title'] = house.housetitle
        data['address'] = house.houseaddress
        data['price'] = house.houseprice
        data['area'] = house.housearea
        data['description'] = house.housedescription
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
    houses = {"code": 0, "msg": "", "count": houseInfo.count(), "data": house_info}
    return JsonResponse(houses)


def modify_secondhouse_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        houseInfo = models.SecondHouse.objects.get(pk=id)
        houseInfo.housetitle = request.POST.get("title")
        houseInfo.houseaddress = request.POST.get("address")
        houseInfo.houseprice = request.POST.get("price")
        houseInfo.housearea = request.POST.get("area")
        houseInfo.housedescription = request.POST.get("description")
        houseInfo.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


def drop_secondhouse_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        houseInfo = models.SecondHouse.objects.get(pk=id)
        houseInfo.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


def to_add_secondhouse(request):
    return render(request, 'add_secondhouse.html')


def add_secondhouse(request):
    if request.method == 'POST':
        houseInfo = models.SecondHouse()
        houseInfo.housetitle = request.POST.get("title")
        houseInfo.houseaddress = request.POST.get("address")
        houseInfo.houseprice = request.POST.get("price")
        houseInfo.housearea = request.POST.get("area")
        houseInfo.housedescription = request.POST.get("description")
        houseInfo.save()
        return HttpResponseRedirect("/house/showall_secondhand/")


# 新房视图
def showall_new(request):
    houseInfo = models.NewHouse.objects.all()
    data = {
        'houseInfo': houseInfo
    }
    return render(request, 'form_new.html', context=data)


def showall_new_echarts(request):
    houseInfo = models.NewHouse.objects.all()
    newpricevalue1 = newpricevalue2 = newpricevalue3 = newpricevalue4 = newpricevalue5 = 0
    newareavalue1 = newareavalue2 = newareavalue3 = newareavalue4 = newareavalue5 = newareavalue6 = newareavalue7 = newareavalue8 = newareavalue9 = newareavalue0 = 0
    for house in houseInfo:
        newpricetemp = house.houseprice
        if newpricetemp != '价格待定':
            newpricetemp = float(newpricetemp)
            if newpricetemp >= 0 and newpricetemp < 7000:
                newpricevalue1 += 1
            elif newpricetemp >= 7000 and newpricetemp < 12000:
                newpricevalue2 += 1
            elif newpricetemp >= 12000 and newpricetemp < 17000:
                newpricevalue3 += 1
            elif newpricetemp >= 17000 and newpricetemp < 22000:
                newpricevalue4 += 1
            else:
                newpricevalue5 += 1
        newareatemp = house.housearea
        if newareatemp != '暂无描述':
            if '-' in newareatemp:
                newareatemp1 = float(newareatemp.split("-")[1])
                newareatemp2 = float(newareatemp.split("-")[0])
                newareatemp = (newareatemp1 + newareatemp2) / 2
                if newareatemp >= 0 and newareatemp < 50:
                    newareavalue1 += 1
                elif newareatemp >= 50 and newareatemp < 70:
                    newareavalue2 += 1
                elif newareatemp >= 70 and newareatemp < 90:
                    newareavalue3 += 1
                elif newareatemp >= 90 and newareatemp < 110:
                    newareavalue4 += 1
                elif newareatemp >= 110 and newareatemp < 130:
                    newareavalue5 += 1
                elif newareatemp >= 130 and newareatemp < 150:
                    newareavalue6 += 1
                elif newareatemp >= 150 and newareatemp < 170:
                    newareavalue7 += 1
                elif newareatemp >= 170 and newareatemp < 190:
                    newareavalue8 += 1
                elif newareatemp >= 190 and newareatemp < 210:
                    newareavalue9 += 1
                else:
                    newareavalue0 += 1
            else:
                newareatemp = float(newareatemp)
                if newareatemp >= 0 and newareatemp < 50:
                    newareavalue1 += 1
                elif newareatemp >= 50 and newareatemp < 70:
                    newareavalue2 += 1
                elif newareatemp >= 70 and newareatemp < 90:
                    newareavalue3 += 1
                elif newareatemp >= 90 and newareatemp < 110:
                    newareavalue4 += 1
                elif newareatemp >= 110 and newareatemp < 130:
                    newareavalue5 += 1
                elif newareatemp >= 130 and newareatemp < 150:
                    newareavalue6 += 1
                elif newareatemp >= 150 and newareatemp < 170:
                    newareavalue7 += 1
                elif newareatemp >= 170 and newareatemp < 190:
                    newareavalue8 += 1
                elif newareatemp >= 190 and newareatemp < 210:
                    newareavalue9 += 1
                else:
                    newareavalue0 += 1

    newareavalue = [newareavalue1, newareavalue2, newareavalue3, newareavalue4, newareavalue5, newareavalue6,
                    newareavalue7, newareavalue8, newareavalue9, newareavalue0]
    newpricevlaue = [newpricevalue1, newpricevalue2, newpricevalue3, newpricevalue4, newpricevalue5]
    keys = ['价格5000元/平方米以内', '价格5000-10000元/平方米', '价格10000-15000元/平方米', '价格15000-20000元/平方米', '价格20000元/平方米以上']
    data = {}
    for k, v in zip(keys, newpricevlaue):
        data.update({k: v, }, )
    print(newareavalue, newpricevlaue)
    return render(request, 'echarts_new.html', {'data': json.dumps(data), 'area': json.dumps(newareavalue)})


def show_newhouse_all_bypage(request):
    # select * from Student limit 1,10
    houseInfo = models.NewHouse.objects.all()
    lis = []
    for house in houseInfo:
        data = dict()
        data['id'] = house.id
        data['title'] = house.housetitle
        data['address'] = house.houseaddress
        data['price'] = house.houseprice
        data['area'] = house.housearea
        data['description'] = house.housedescription
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
    houses = {"code": 0, "msg": "", "count": houseInfo.count(), "data": house_info}
    return JsonResponse(houses)


def modify_newhouse_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        houseInfo = models.NewHouse.objects.get(pk=id)
        houseInfo.housetitle = request.POST.get("title")
        houseInfo.houseaddress = request.POST.get("address")
        houseInfo.houseprice = request.POST.get("price")
        houseInfo.housearea = request.POST.get("area")
        houseInfo.housedescription = request.POST.get("description")
        houseInfo.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)
        # return render(request,'main_menu.html',context=data)

def drop_newhouse_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        houseInfo = models.NewHouse.objects.get(pk=id)
        houseInfo.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


def to_add_newhouse(request):
    return render(request, 'add_newhouse.html')


def add_newhouse(request):
    if request.method == 'POST':
        houseInfo = models.NewHouse()
        houseInfo.housetitle = request.POST.get("title")
        houseInfo.houseaddress = request.POST.get("address")
        houseInfo.houseprice = request.POST.get("price")
        houseInfo.housearea = request.POST.get("area")
        houseInfo.housedescription = request.POST.get("description")
        houseInfo.save()
        return HttpResponseRedirect("/house/showall_new/")


# 租房视图
def showall_rent(request):
    houseInfo = models.RentHouse.objects.all()
    data = {
        'houseInfo': houseInfo
    }
    return render(request, 'form_rent.html', context=data)


def showall_rent_echarts(request):
    houseInfo = models.RentHouse.objects.all()
    pricevalue1 = pricevalue2 = pricevalue3 = pricevalue4 = pricevalue5 = 0
    areavalue1 = areavalue2 = areavalue3 = areavalue4 = areavalue5 = areavalue6 = areavalue7 = areavalue8 = areavalue9 = areavalue0 = 0
    for house in houseInfo:
        pricetemp = float(house.houseprice)
        if pricetemp >= 0 and pricetemp < 1000:
            pricevalue1 += 1
        elif pricetemp >= 1000 and pricetemp < 2000:
            pricevalue2 += 1
        elif pricetemp >= 2000 and pricetemp < 3000:
            pricevalue3 += 1
        elif pricetemp >= 3000 and pricetemp < 4000:
            pricevalue4 += 1
        else:
            pricevalue5 += 1
        areatemp = float(house.housearea)
        if areatemp >= 0 and areatemp < 50:
            areavalue1 += 1
        elif areatemp >= 50 and areatemp < 60:
            areavalue2 += 1
        elif areatemp >= 60 and areatemp < 70:
            areavalue3 += 1
        elif areatemp >= 70 and areatemp < 80:
            areavalue4 += 1
        elif areatemp >= 80 and areatemp < 90:
            areavalue5 += 1
        elif areatemp >= 90 and areatemp < 100:
            areavalue6 += 1
        elif areatemp >= 100 and areatemp < 110:
            areavalue7 += 1
        elif areatemp >= 110 and areatemp < 120:
            areavalue8 += 1
        elif areatemp >= 120 and areatemp < 130:
            areavalue9 += 1
        else:
            areavalue0 += 1

    areavalue = [areavalue1, areavalue2, areavalue3, areavalue4, areavalue5, areavalue6, areavalue7, areavalue8,
                 areavalue9, areavalue0]
    pricevlaue = [pricevalue1, pricevalue2, pricevalue3, pricevalue4, pricevalue5]
    keys = ['价格1000元/月以内', '价格1000-2000元/月', '价格2000-3000元/月', '价格3000-4000元/月', '价格4000元/月以上']
    data = {}
    for k, v in zip(keys, pricevlaue):
        data.update({k: v, }, )
    print(areavalue)
    return render(request, 'echarts_rent.html', {'data': json.dumps(data), 'area': json.dumps(areavalue)})


def show_renthouse_all_bypage(request):
    # select * from Student limit 1,10
    houseInfo = models.RentHouse.objects.all()
    lis = []
    for house in houseInfo:
        data = dict()
        data['id'] = house.id
        data['title'] = house.housetitle
        data['address'] = house.houseaddress
        data['price'] = house.houseprice
        data['area'] = house.housearea
        data['description'] = house.housedescription
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
    houses = {"code": 0, "msg": "", "count": houseInfo.count(), "data": house_info}
    return JsonResponse(houses)


def modify_renthouse_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        houseInfo = models.RentHouse.objects.get(pk=id)
        houseInfo.housetitle = request.POST.get("title")
        houseInfo.houseaddress = request.POST.get("address")
        houseInfo.houseprice = request.POST.get("price")
        houseInfo.housearea = request.POST.get("area")
        houseInfo.housedescription = request.POST.get("description")
        houseInfo.save()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


def drop_renthouse_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        houseInfo = models.RentHouse.objects.get(pk=id)
        houseInfo.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


def to_add_renthouse(request):
    return render(request, 'add_renthouse.html')


def add_renthouse(request):
    if request.method == 'POST':
        houseInfo = models.RentHouse()
        houseInfo.housetitle = request.POST.get("title")
        houseInfo.houseaddress = request.POST.get("address")
        houseInfo.houseprice = request.POST.get("price")
        houseInfo.housearea = request.POST.get("area")
        houseInfo.housedescription = request.POST.get("description")
        houseInfo.save()
        return HttpResponseRedirect("/house/showall_rent/")


def test(request):
    return render(request, 'main_menu.html')
