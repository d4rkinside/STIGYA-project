from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from products.models import ProductMaster
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def home(request):
    return render(request, 'products/home.html')  # Render the home.html template

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  # Redirect to dashboard or desired page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'products/login.html', {'form': form})

def add(request):
    if request.method == "POST":
        asin = request.POST.get('asin')
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        timer=datetime.now().strftime("%c")
        


        prod=ProductMaster(
            asin = asin,
            name = name,
            brand = brand,
            created_at = timer,
            updated_at = timer
            
        )
        prod.save()
        return redirect('productlist')
    return render(request,'products/productlist.html')

def edit(request):

    prod=ProductMaster.objects.all()

    data={
        'prod':prod,
    }
    return redirect(request,'productlist.html')

def update(request,id):
    if request.method == "POST":
        asin = request.POST.get('asin')
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        created_at = request.POST.get('created_at')
        timer =datetime.now().strftime("%c")
        updated_at=timer

        prod=ProductMaster(
            id=id,
            asin=asin,
            name=name,
            brand=brand,
            updated_at=updated_at,
            created_at=created_at
        )
        prod.save()
        return redirect('productlist')


    return redirect(request,'productlist')

def delete(request,id):
    prod=ProductMaster.objects.filter(id=id)
    prod.delete()
    data={
        'prod':prod
    }

    return redirect('productlist')

def sele(request):
    
    return render(request,'products/sele.html')

def addtocart(request):
    if request.method == 'POST':
        asin = request.POST.get('asin')
        url="https://www.amazon.in/dp/"+asin

        # Initialize Selenium WebDriver
        driver = webdriver.Chrome()
        driver.get(url)
        handles=driver.window_handles
        driver.switch_to.window(handles[0])
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()           

        #add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(()))       
        #add_to_cart_button.click()

        time.sleep(2)
        driver.quit()


        return render(request, 'products/sele.html')
    else:
        return render(request, 'products/sele.html')

def productlist(request):
    prod = ProductMaster.objects.all()

    data = {
        'prod':prod,
    }

    return render(request,'products/productlist.html',data)


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_change_done')  # Redirect to a success page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'products/change_password.html', {'form': form})

@login_required
def dashboard(request):
    # Your dashboard logic here
    return render(request, 'products/dashboard.html')
