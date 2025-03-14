from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password  # For password hashing
from .models import Product
from django.shortcuts import render, get_object_or_404

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # If login is successful, redirect to home page
                return redirect('home')  # Replace 'home' with your actual home page URL
            else:
                messages.error(request, "Invalid password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'login.html')

# Sign-up view
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hashed_password = make_password(password)  # Hash the password before storing
        
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            # Create new user
            User.objects.create(username=username, email=email, password=hashed_password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login_view')  # Redirect to login page after successful sign up
    
    return render(request,'sign.html')

def home(request):
    products = Product.objects.all()[:3]  # Limits to 6 products
    return render(request, "homepage.html", {"products": products})
def product_view(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def cart_view(request):
     return render(request,'cart.html')
def men(request):
    products = Product.objects.all()
    return render(request,'man.html',{"products": products})
def women(request):
    products = Product.objects.all()
    return render(request,'woman.html',{"products": products})
 
    