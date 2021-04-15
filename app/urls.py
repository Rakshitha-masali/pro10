from django.urls import path
from app import views
my_app="app"

urlpatterns = [
    path('view1/',views.view1,name="view1"),
    path('view2/<email>',views.view2,name="view2"),
    path('view3/<name>',views.view3,name="view3"),
    path('',views.if_demo,name="if_demo"),
    path('samp/',views.ifelse_demo,name="ifelse_demo"),
    path('for/',views.for_demo,name="for_demo"),

]



