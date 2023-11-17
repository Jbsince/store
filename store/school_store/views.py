from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Department, Purpose, Course
from django.contrib.auth.models import User
from . forms import RegistrationForm
from django.http import JsonResponse



# Create your views here.

def purchase(request):
    return render(request, 'purchase.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME ALREADY TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                print("User Created:", user.username)

                auth.login(request, user)  # Log the user in after registration
                return redirect('login')  # Redirect to the home page or wherever you want to go after registration
        else:
            messages.info(request, "PASSWORDS DO NOT MATCH")
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('purchase')
        else:
            messages.info(request, 'INVALID CREDENTIALS TO LOGIN')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
    # Fetch the departments from the database
    departments = Department.objects.all()

    return render(request, 'home.html', {'links': departments})






def booking(request):
    selected_department_id = request.GET.get('department', '')

    if selected_department_id:
        selected_department = Department.objects.get(pk=selected_department_id)
        courses = Course.objects.filter(department_id=selected_department_id)
    else:
        selected_department = None
        courses = Course.objects.none()

    departments = Department.objects.all()
    purpose = Purpose.objects.all()

    form = RegistrationForm(request.POST or None)
    form.fields['courses'].queryset = courses

    if form.is_valid():
        form.Save()
        # Add a success message
        messages.success(request, 'Order Confirmed!')
        return redirect('/')

    context = {
        'departments': departments,
        'courses': courses,
        'purpose': purpose,
        'selected_department': selected_department,
        'form': form
    }

    return render(request, 'booking.html', context)



def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_name_id=department_id).values('id', 'course_name')
    return JsonResponse({'courses': list(courses)})



