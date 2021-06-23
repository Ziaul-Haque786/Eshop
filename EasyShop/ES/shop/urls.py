from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="About Us"),
    path('contact/', views.contact, name="Contact Us"),
    path('productview/', views.productView, name="View"),
    path('search/', views.search, name="Search"),
    path('tracker/', views.tracker, name="Track Us"),
    path('checkout/', views.checkout, name="Checkout")
]