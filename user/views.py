from django.shortcuts import redirect, render
from .models import User,Orders,Products
from .forms import Signupform
from django.views.decorators.csrf import csrf_protect

user_auth = 0
user = ''

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
        if user.password == data['password']:
            orders = Orders.objects.filter(user=user,status='Added to cart').values_list('product_id',flat=True)
            return render(request,"index.html",{'user_auth':user_auth})
    return render(request,"login.html")

def logout(request):
    global user_auth,user
    user_auth = False
    user = ''
    return redirect(index)

def camera(request):
    global orders,user
    cameras = Products.objects.filter(category=0)
    if user: orders = Orders.objects.filter(user=user,status='Added to cart').values_list('product_id',flat=True)
    return render(request,"products.html",{'user_auth':user_auth,'products':cameras,'orders':orders})

def add_to_cart(request,id):
    global user_auth,user
    Orders(user = user,product_id = id, status = 'Added to cart').save()
    return redirect(camera)

def cart(request):
    global user_auth,orders
    products = Products.objects.filter(id__in=orders)
    total = sum([product.price for product in products])
    return render(request,"cart.html",{'user_auth':user_auth,'products':products,'total':total})

def delete_from_cart(request,id):
    global user,orders
    Orders.objects.filter(user=user,product_id=id).delete()
    orders = Orders.objects.filter(user=user,status='Added to cart').values_list('product_id',flat=True)
    return redirect(cart)

def checkout(request):
    global orders,user
    Orders.objects.filter(user=user).update(status='Confirmed')
    orders = []
    return redirect(cart)