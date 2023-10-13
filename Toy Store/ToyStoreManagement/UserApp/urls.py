from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('ShowToys/<id>',views.ShowToys),
    path('ViewDetails/<id>',views.ViewDetails),
    path('AddToCart',views.AddToCart),
    path('Login',views.Login),
    path('SignUp',views.SignUp),
    path('Logout',views.Logout),
    path('ShowCart',views.ShowCart),
    path('ModifyCart',views.ModifyCart),
    path('MakePayment',views.MakePayment),
]
