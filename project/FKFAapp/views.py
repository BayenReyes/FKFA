from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.templatetags.static import static
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home_view(request):
    return render(request, 'FKFA/home.html')


def report_view(request):
    return render(request, 'FKFA/report.html')


def cages_view(request):
    return render(request, 'FKFA/Cages.html')


def new_wqm_view(request):
    return render(request, 'FKFA/new_WQM.html')


def damsummary_view(request):
    return render(request, 'FKFA/Damage_Summary.html')


def sendemail_view(request):
    if request.method == 'POST':
        re = request.POST.getlist('chk[]'),
        re = " ,".join(["<{}>".format(r) for r in re[0]])


        context = {
            'recipients': re,
            'message': request.POST.get('message'),
            'file': request.FILES.getlist('file'),
        }
        return render(request, 'queries/sendemail.html', context)
    else:
        return render(request, 'FKFA/Advisory.html')


def tblDetail_view(request):
    context = {
        'date': request.GET.get('date'),
    }
    return render(request, 'FKFA/tblDetails.html', context)


def listcages_view(request):
    context = {
        'muni': request.GET.get('muni'),
        'area': request.GET.get('area'),
    }
    return render(request, 'FKFA/listofcageowners.html', context)


def advisory_view(request):
    return render(request, 'FKFA/Advisory.html')


def inputWQM_view(request):
    chkarea = request.GET.getlist('chkarea[]')

    txarea = [car + " " + request.GET.get('txt' + car.replace(" ", "")) if request.GET.get(
        'txt' + car.replace(" ", "")) else car for car in chkarea]
    context = {
        'param': request.GET.getlist('param[]'),
        'area': txarea,
    }
    return render(request, 'FKFA/input_WQM.html', context)


def insertWQM_view(request):
    if request.method == 'POST':
        areaid = request.POST.getlist('Are[]')
        pareme = [request.POST.getlist(a + '[]') for a in areaid]
        value = [[request.POST.getlist(s + '[]') for s in p] for p in pareme]

        context = {
            'areaname': request.POST.getlist('Area[]'),
            'paramname': request.POST.getlist('Param[]'),
            'areaid': areaid,
            'parame': pareme,
            'value': value,
        }
        return render(request, 'queries/insert_WQM.html', context)
    else:
        return render(request, 'FKFA/new_WQM.html')


def addcontact_view(request):
    if request.method == 'POST':

        context = {
            'name': request.POST.get('txtname'),
            'email': request.POST.get('txtemail'),
        }
        #html = "{% addcontact '"+context['name']+"' '"+context['email']+"' %}"

        # t = Template("<html><body>{% load mytags %}{% addcontact path name email %}</body></html>")
        # html = t.render(Context(context))
        # return HttpResponse(html)
        return render(request, 'queries/addcontact.html',context)
    else:
        return render(request, 'queries/testing')


def testing(request,qwe, month):
    return render(request, 'FKFA/testing_path.html', {'people': month})

from django.contrib.auth import authenticate, login

def login_view(request):
    #logout(request)
    if not request.user.is_authenticated:
        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request,'FKFA/login.html')
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login')