"""Home_Rental_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from Landlord import views as Lview
from User import views as Uview
from House  import views as Hviews
from Renters import views as Rview

from Advertisement import views as Adview



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Landlords/',Lview.Landlordinfo),
    path('Registration/',Uview.registration),
    path('house/',Hviews.House_info),
    path('Renters/',Rview.Rentersinfo),

    path('NewLandlords/',Lview.insertlandlordinfo),
    path('Advertisment/',Adview.advertisementinfo)
    ]

