from django.shortcuts import render
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django import forms
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            print("Passwords do not match.")
            return redirect('signup')

        # Create the user
        user = CustomUser.objects.create_user(username=username, email=email, password=password, firstname=first_name, lastname=last_name)
        user.save()

        # Redirect to a success page or homepage
        return redirect('login')
    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.get(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a specific page after successful login
            return redirect('index')  
        else:
            # Handle invalid login credentials
            pass
    return render(request, 'login.html')

def index(request):
    user = request.user
    print(user)
    return render(request , 'index.html')
def base(request):
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def signout(request):
    return render(request,'signout.html')
def confirmation(request):
    return render(request,'confirmation.html')
def dashboard(request):
    user = request.user   
    if user.is_authenticated:
        user = CustomUser.objects.get(email = user)
        print(user.firstname)
    else:
        print("User is not authenticated")
    return render(request,'dashboard.html', { 'user': user })

@login_required
def profiledeatils(request):
    user = request.user   
    
    return render(request,'profiledetails.html' , { 'user': user })


def address(request):
    return render(request,'address.html')

def shop(request, category):
    # products = Product.objects.filter(category__name=category)
    return render(request, 'shop.html')
def signout(request):
    return render(request,'signout.html')
def product_details(request, product_id):
    # product = get_object_or_404(Product, pk=product_id)
    # product_images = [product.product_image_1, product.product_image_2, product.product_image_3, product.product_image_4, product.product_image_5]
    # product_colours = product.Colors.all()
    # product_size = product.sizes.all()
    
    
    return render(request, 'product_details.html')



def add_to_cart(request, product_id):
    user = request.user
    # cart_item = CartItem.objects.get(user = user)
    # product = get_object_or_404(Product, pk=product_id)
    # CartItem.objects.create(user=user ,
    #                         product_name = product.product_name ,
    #                         price = product.product_price ,
    #                         quantity = 1,
    #                         total = product.product_price)
    

    
    
    return redirect('view_cart')
@login_required
def view_cart(request):
    # Retrieve cart items for the current user
    # cart_items = CartItem.objects.filter(user=request.user)
    
    # total_price = sum(item.total for item in cart_items)
    
    return render(request, 'shop_cart.html')

def remove_from_cart(request, product_id):
    # Your logic to remove an item from the cart
    return redirect('view_cart')






