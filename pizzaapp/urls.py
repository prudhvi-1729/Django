from django.contrib import admin
from django.urls import path
from .views import acceptorder,declineorder,adminorders,userorders,placeorder,userlogout,customerwelcomeview,userauthenticate,customerwelcomeview,homepage,adminloginview,adminhomepageview,authenticateadmin,logoutadmin,addpizza,deletepizza,signupuser,userloginview
urlpatterns = [
    path('admin/', adminloginview,name="adminloginpage"),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name="adminhomepage" ),
    path('adminlogout/',logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),
    path('',homepage,name="homepage"),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview,name="userloginpage"),
    path('customer/welcome/',customerwelcomeview,name="customerpage"),
    path('customer/authenticate/',userauthenticate),
    path('userlogout/',userlogout),
    path('placeorder/',placeorder),
    path('userorders/',userorders),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder),
]
