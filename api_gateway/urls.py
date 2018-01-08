"""api_gateway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from gateway import views

urlpatterns = [

    url(r'^$', views.homePage),
    url(r'^admin/', admin.site.urls),
    url(r'^add-api/', views.addApiView),
    url(r'^add-info/',views.insertApiInfo),
    url(r'^display-api/',views.disApiInfo),
    url(r'^delete-api/',views.deleteApiInfo),
    url(r'^edit-api',views.updateApiInfo),
    url(r'^commit-api/(\d)/',views.commitApiInfo),

    url(r'^add-vers/', views.addVersView),
    url(r'^ins-vers/',views.insertVersInfo),
    url(r'^display-vers/',views.disVersInfo),
    url(r'^delete-vers/',views.deleteVersInfo),
    url(r'^edit-vers',views.updateVersInfo),
    url(r'^commit-vers/(\d+)/',views.commitVersInfo),

    url(r'^add-acl/', views.addAclView),
    url(r'^ins-acl/',views.insertAclInfo),
    url(r'^display-acl/',views.disAclInfo),
    url(r'^delete-acl/',views.deleteAclInfo),
    url(r'^edit-acl',views.updateAclInfo),
    url(r'^commit-acl/(\d+)/',views.commitAclInfo),

            ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
