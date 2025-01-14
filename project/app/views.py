from django.shortcuts import render,redirect

# Create your views here.
user=[]
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        for i in user:
            if username==i['username'] and password==i['password']:
                print([i['name']])
            return redirect(home)
    return render(request,'login.html')

def sign(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        d={}
        user.append({'username':username,'email':email,'password':password})
        print(user)
    return render(request,'sign.html')
def home(request):
    return render(request,'homepage.html')