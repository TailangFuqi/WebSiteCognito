"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from website.views.APIs import updateAccount, loginproc, getUserInfo, signupproc, activationproc, resetpasswordproc, reregistpasswordproc, logoutproc, changepasswordproc, csrftoken, apiTest
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getcsrftoken', csrftoken.CsrfView, name="getcsrftoken"),
    path('updateaccount', updateAccount.updateAccount, name="updateAccount"),
    path('loginproc', loginproc.login, name="loginproc"),
    path('getUserInfo', getUserInfo.getUserInfo, name="getUserInfo"),
    path('signupproc', signupproc.signup, name="signupproc"),
    path('activationproc', activationproc.activation, name="activationproc"),
    path('resetpasswordproc', resetpasswordproc.resetpassword,
         name="resetpasswordproc"),
    path('reregistpasswordproc', reregistpasswordproc.reregistpassword,
         name="reregistpasswordproc"),
    path('logoutproc', logoutproc.logout, name="logoutproc"),
    path('changepasswordproc', changepasswordproc.changepassword,
         name="changepassword"),
]
