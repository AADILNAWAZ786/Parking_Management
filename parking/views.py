from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import category, add
from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
@never_cache
@login_required(login_url="login")
def show(request):
    return render(request,"dashboard.html")
    
@never_cache
@login_required(login_url="login")
def Test_case3(request):
    men=category.objects.all()
    return render(request,"category.html",{'men':men})

@never_cache
@login_required(login_url="login")
def Test_case3_1(request):
    a_1=request.POST['paring_area_no']
    a_2=request.POST['vehical_Type']
    a_3=request.POST['vehical_limit']
    a_4=request.POST['parking_charge']
    men=category(paring_area_no=a_1,vehical_Type=a_2, vehical_limit=a_3, parking_charge=a_4)
    men.save()
    return redirect ("category")

@never_cache
@login_required(login_url="login")
def Test_case3_2(request, id):
    try:
        pi = category.objects.get(pk=id)
        pi.delete()
        messages.success(request, "Category deleted successfully.")
    except category.DoesNotExist:
        messages.error(request, "Category not found.")
    return redirect('category')


    

    
@never_cache
@login_required(login_url="login")
def edit(request, ids):
    if request.method == "POST":
        e_1=request.POST.get('paring_area_no')
        e_2=request.POST.get('vehical_Type')
        e_3=request.POST.get('vehical_limit')
        e_4=request.POST.get('charge')
        g=category.objects.get(paring_area_no=e_1, vehical_Type=e_2, vehical_limit=e_3, parking_charge=e_4)
        category.objects.filter(id=ids).update(
            addid=g
        )
    return redirect('category')    


@never_cache
@login_required(login_url="login")
def Test_case4(request):
    boy=add.objects.all()
    return render(request,"vehicle_entry.html", {'boy':boy})

@never_cache
@login_required(login_url="login")
def Test_case4_1(request):
    vehicle_type = category.objects.values_list('vehicle_type', flat=True).distinct()
    parking_charge = category.objects.values_list('parking_charge',flat=True).distinct()
    vehicle_counts = add.objects.values('vehicle_type').annotate(vehicle_count=Count('id'))
    data = []
    for x in category.objects.all():
        type=x.vehicle_type
        limit=x.vehicle_limit
        count=next((item['vehicle_count'] for item in vehicle_counts if item['vehicle_type'] == type), 0)
        limit=int(limit)
        count=int(count)
        counts= limit-count
        data.append({'vehicle_type':type, "vehicle_limit":limit,'counts':counts})

    search_query = request.GET.get('query')
    if search_query:
        multi_search = Q(vehicle_type__icontains=search_query) | Q(
            vehicle_limit__icontains=search_query) | Q(parking_charge__icontains=search_query)
        vehicle = add.objects.filter(multi_search)
    else:
        vehicle = add.objects.all()

    if request.method =='POST':
        vehicle_no = request.POST['vehicle_no']
        type = request.POST['type']
        parking_area_no_id = request.POST['parking_area_no']
        author = category.objects.get(pk=parking_area_no_id)
        charge = request.POST['charge']
        add.objects.create(vehicle_no= vehicle_no, vehicle_type= type, parking_area_no=author, parking_charge= charge)
        return redirect('vehicle_entry')
    page_num = request.GET.get('page')
    paginator = Paginator(vehicle,4)

    try:
        vehicle = paginator.page(page_num)
    except PageNotAnInteger:
        vehicle = paginator.page(1)
    except EmptyPage:
        vehicle = paginator.page(paginator.num_pages)

    category_data = category.objects.values_list('parking_area_no', flat=True)
    count= category.objects.all()
    context = {'vehicle_type': vehicle_type, 'parking_charge': parking_charge, 'vehicle':vehicle, 'category_data': category_data,'count':count, 'data':data}

    return render(request, 'vehicle_entry.html',context)



@never_cache
@login_required(login_url="login")
def Test_case5(request):
    if 'a' in request.GET:
        a=request.GET['a']
        ab=add.objects.filter(vehical_number=a)
    else:
        ab=add.objects.all()
    context={
        'ab':ab
    }    
    return render(request,"Manage_Vehicles.html", context)

@never_cache
@login_required(login_url="login")
def vehicle_entry_status(request, id):
    vehicle_entry= add.objects.get(id=id)
    if vehicle_entry.status == 'parked':
        vehicle_entry.status = 'leaved'
    else:
        vehicle_entry.status ='parked'
    vehicle_entry.save()
    return redirect('Manage_Vehicles')

@never_cache
@login_required(login_url="login")
def Test_case6(request):
    if 'q' in request.GET:
        q=request.GET['q']
        search=add.objects.filter(vehical_number=q)
    else:
        search=add.objects.all()
    context={
        'search':search
    }    
    return render(request,"Search.html",context)

@never_cache
@login_required(login_url="login")
def dashboard(request):
    vehicles_parked = add.objects.filter(status='parked').count()
    vehicles_departed = add.objects.filter(status='leaved').count()
    available_category = category.objects.all().count()
    earnings = add.objects.values_list('parking_charge', flat=True).filter(status='leaved')
    print(earnings)
    temp =0
    for i in earnings:
        temp =temp+float(i)
    tot_earnings =int(temp)

    tot_records = add.objects.all().count()
    vehicle_limits = category.objects.values_list('vehical_limit',flat=True)
    tot_vehicle_limit = sum(int(limit) for limit in vehicle_limits if limit.isdigit())

    context ={'parked': vehicles_parked, 'departed':vehicles_departed,'tot_category' :available_category,
              'tot_earnings':tot_earnings, 'tot_records':tot_records,'tot_vehicle_limit':tot_vehicle_limit}

    return render(request,'dashboard.html',context)

@never_cache
@login_required(login_url="login")
def accountSetting(request):
    if request.method == 'POST':
        current_pass = request.POST.get('current')
        new_pass = request.POST.get('n_pass1')
        re_pass = request.POST.get('n_pass2')

        if not request.user.check_password(current_pass):
            messages.error(request, 'Current password is not correct')
            return redirect('Accounts')
        if new_pass != re_pass:
            messages.error(
                request, 'New password and re-entered password do not match')
            return redirect('Accounts')

        if new_pass == current_pass:
            messages.error(
                request, 'New password cannot be same as current password do not match')
            return redirect('Accounts')
        request.user.set_password(new_pass)
        request.user.save()
        login(request, request.user)
        messages.success(request, 'Password changed Successfully')
        return render(request, 'Accounts.html')
    return render(request, 'Accounts.html')





def login_view(request):
    if request.method == "POST":
        users = request.POST.get('user_name')
        password = request.POST.get('pass')
        user = authenticate(request, username=users, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def logouts (request):
    logout(request)
    return redirect('login')