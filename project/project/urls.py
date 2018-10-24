"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from FKFAapp import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('report', views.report_view, name='report'),
    path('cages', views.cages_view, name='cages'),
    path('new_wqm', views.new_wqm_view, name='new_wqm'),
    path(r'tabledetail', views.tblDetail_view, name='tabledetail'),
    path(r'listcage', views.listcages_view, name='listcage'),
    path(r'inputWQM', views.inputWQM_view, name='inputWQM'),
    path('advisory', views.advisory_view, name='advisory'),
    path('damagesummary', views.damsummary_view, name='damagesummary'),
    path('sendemail', views.sendemail_view, name='sendemail'),
    path('insertWQM', views.insertWQM_view, name='insertWQM'),
    path('addcontact', views.addcontact_view, name='addcontact'),
    path('testing/<int:qwe>/<int:month>/', views.testing, name='test'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
