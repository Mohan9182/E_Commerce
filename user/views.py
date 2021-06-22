from django.shortcuts import redirect, render
from .models import User,Orders
from .forms import Signupform
from django.views.decorators.csrf import csrf_protect

user_auth = 0
user = ''

cameras = {
    1:{'name': 'Nikon','price':39000,'pic':'1.jpg'},
    2:{'name': 'Canon','price':20000,'pic':'2.jpg'},
    3:{'name': 'Samsung','price':25000,'pic':'3.jpg'},
    4:{'name': 'LG','price':15000,'pic':'4.jpg'},
    5:{'name': 'Sony','price':40000,'pic':'5.jpg'},
    6:{'name': 'Fujifilm','price':35000,'pic':'6.jpg'},
}

orders = []

@csrf_protect
def signup(request):
    global user_auth
    form = Signupform()
    print(User.objects.get(email='mmohan9182@gmail.com'))
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=form.cleaned_data['email'])
            user_auth = user.id
            return redirect(index)
    return render(request,"signup.html",{'form':form})

def index(request):
    global user_auth
    return render(request,"index.html",{user_auth:user_auth})

@csrf_protect
def login(request):
    global user_auth,orders,user
    if request.method == 'POST':
        data = request.POST
        user = User.objects.get(email=data['email'])
        user_auth = user.id
        if user.password == data['password']: return render(request,"index.html",{'user_auth':user_auth})
    return render(request,"login.html")

def logout(request):
    global user_auth
    user_auth = False
    return redirect(index)

def camera(request):
    global cameras,orders,user
    orders = Orders.objects.filter(user=user,status='Added to cart').values_list('product_id',flat=True)
    return render(request,"products.html",{'user_auth':user_auth,'products':cameras,'orders':orders})

def add_to_cart(request,id):
    global user_auth,user
    order = Orders(user = user,product_id = id, status = 'Added to cart')
    order.save()
    return redirect(camera)
