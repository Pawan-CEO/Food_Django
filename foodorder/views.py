from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foodorder.models import userinfo
from foodorder.models import foodmenu
from foodorder.models import orderhist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime
# from django.contrib.auth import login as auth_login

# Create your views here.
def home(req):
    food=foodmenu.objects.all()
    # if 'foodlist' not in req.session:

    #     foodlist=['Food Name']
        # foodlistpricee=['Food Price']
        # req.session['foodlist']=foodlist
    #     req.session['foodlistprice']=foodlistpricee
    # chec=req.session['foodlist']
    data={'food':food}

    s=render(req,'foodorder\index.html',context=data)
    return s

def order(req):
    req.session['foodlist']=[]
    req.session['foodlistprice']=[]
    ord=orderhist()
    total_value=req.GET['total']
    uname=req.session['username']
    now=datetime.datetime.now()
    ti=now.strftime("%H%m%S%Y")
    bill=uname+ti
    ord.uemail=uname
    ord.uamount=total_value
    ord.ubillno=bill
    ord.save()
    return render(req,'foodorder\order.html',{'uname':uname,'total_value':total_value})

def addfoods(req):
    foodlist=[]
    foodlistprice=[]
    if req.method=="GET":
        val=req.GET['foodselectname']
        vall=req.GET['foodselectprice']
        
        foodlist=req.session['foodlist']
        foodlistprice=req.session['foodlistprice']
        foodlist.append(val)
        foodlistprice.append(vall)
        req.session['foodlist']=foodlist
        req.session['foodlistprice']=foodlistprice

    return HttpResponseRedirect('foodorder/home')

def loginn(req):
    data={}
    foodlist=[]
    foodlistprice=[]
    req.session['foodlist']=foodlist
    req.session['foodlistprice']=foodlistprice
    if req.method=="POST":
        usernamev=req.POST['uname']
        passcode=req.POST['upass']
        user=authenticate(req,username=usernamev,password=passcode)
        if user:
            login(req,user)
            req.session['username']=usernamev
            return HttpResponseRedirect('foodorder/home')
        else:
            data['error']="Username or Password Error!!!"
            res=render(req,'foodorder\login.html',data)
            return res
    else:
        data['mass']="Try to Login"
        return render(req,'foodorder\login.html',data)


def signup(req):
    data={}
    if req.method=="POST":
        susername=req.POST['uname']
        semail=req.POST['uemail']
        smobile=req.POST['umobile']
        spasscode=req.POST['upasscode']
        spasscodes=req.POST['upasscodes']
        userr=User()
        userr.username=susername
        userr.password=spasscode
        userr.save()              
        data['mess']="Sign Up Successfull!!! "
        return render(req,'foodorder\signup.html',data)

    else:
        data['mess']="Create New User"
        return render(req,'foodorder\signup.html',data)
def logouts(req):
    uname=req.session['username']
    return render(req,'foodorder\logout.html',{'uname':uname})
def ddcard(req):
    foodlist=[]
    foodlistprice=[]
    if req.method=="GET":
        val=req.GET['foodselectname']
        vall=req.GET['foodselectprice']
        foodlist=req.session['foodlist']
        foodlistprice=req.session['foodlistprice']
        foodlist.append(val)
        foodlistprice.append(vall)
        req.session['foodlist']=foodlist
        req.session['foodlistprice']=foodlistprice
    foodlist=req.session['foodlist']
    foodlistprice=req.session['foodlistprice']
    total=0
    for a in range(len(foodlistprice)):
        total+=int(foodlistprice[a])
    total=str(total)
    mylist = zip(foodlist, foodlistprice)
    data={'mylist':mylist,'total':total}
    s=render(req,'foodorder\ddcard.html',data)
    return s
