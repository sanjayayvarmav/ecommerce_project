from django.urls import path, include
from. import views

urlpatterns = [

    # path('',views.home,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('detail/',views.detail,name='detail'),
    # path('thanks/',views.thanks,name='thanks'),
     path('',views.new,name='new'),
     #path('operation/',views.result,name='result'),

]
