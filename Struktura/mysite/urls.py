"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from cart import views as cart_vievs
from user import views as user_vievs
from product import views as product_views
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_vievs.register_view, name='register'),
    path('', user_vievs.login_view, name='user_login'),
    path('index/', cart_vievs.index, name='index'),
    path('logout/', user_vievs.logout_view, name='user_logout'),
    path('newcart/', cart_vievs.new_cart_view, name='newcart'),
    path('structure/', cart_vievs.show_cart, name='cart_structure'),
    path('cart/', product_views.new_product_view, name='cart'),
    path('blog/', blog_views.blog_view, name='blog'),
    path('blog/new_post', blog_views.newPost_view, name='new_post'),
    path('blog/new_post/<int:pk>', blog_views.post_details_view, name='new_post'),



]
