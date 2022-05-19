from ast import Num
from django.shortcuts import redirect, render
from sympy import product
from .models import Product,category,cart
# Create
#  your views here.

def products(request):
    a=0
    price1 =0
    for v in cart.objects.all():
        a=a+int(v.num)
        for f in Product.objects.all():
            if v.price ==f.id:
                price1 =price1 +(int(f.price)*int(v.num))
    return render(request, 'index.html', {'pro':Product.objects.all().order_by("-date_n"),'total':price1,'item':a,'pro1':Product.objects.all().filter(id =2),'cat':category.objects.all()})
 
def detail(request,proid):
    a=0
    price1 =0
    for v in cart.objects.all():
        a=a+int(v.num)
        for f in Product.objects.all():
            if v.price ==f.id:
                price1 =price1 +(int(f.price)*int(v.num))      
    return render(request, 'details.html',{'pro':Product.objects.filter(id = proid),'item':a,'total':price1,'cat':category.objects.all()})

def cats(request,proid):
    a=0
    price1 =0
    for v in cart.objects.all():
        a=a+int(v.num)
        for f in Product.objects.all():
            if v.price ==f.id:
                price1 =price1 +(int(f.price)*int(v.num))
    return render(request, 'index.html',{'pro':Product.objects.all().filter(categorid =proid),'total':price1,'item':a,'pro1':Product.objects.all().filter(id =proid),'cat':category.objects.all()})

def cartitem(request):
    a=0
    price1 =0
    for v in cart.objects.all():
        a=a+int(v.num)
        for f in Product.objects.all():
            if v.price ==f.id:
                price1 =price1 +(int(f.price)*int(v.num))
                
                
    return render(request, 'contact.html',{'pro':Product.objects.all(),'item':a,'cars':cart.objects.all(),'cat':category.objects.all()})



def carts(request,proid):
    a=int(cart.objects.filter(price=proid).count())
    if a >= 1:
        s=cart.objects.get(price=proid)
        cart.objects.filter(price=proid).update(num=int(s.num)+1)
    else:
        carts=cart(price=proid,num=1)
        carts.save()
    return redirect("/")

def delet(request,proid):
    a=int(cart.objects.filter(price=proid).count())
    if a!=0:
        q=cart.objects.get(price=proid)
        if q.num >1:
            cart.objects.filter(price=proid).update(num=int(q.num)-1)
        
        else:
            q.delete()
    return redirect("/cartitem/")

