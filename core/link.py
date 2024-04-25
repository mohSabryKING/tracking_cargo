from django.urls import *
from .views import *
from django.contrib.auth import views as log_x

urlpatterns = [
     path('login',log_x.LoginView.as_view(template_name='registration/login.html'),name='login'),
      path('logout',log_x.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
      path('add_user',Add_user_page.as_view(),name='reg'),
      path('',Home_page.as_view(),name='home'),
      path('find_cargo',find_voyage_cargos,name='q_c'),
      path('find_voyage',find_voyages,name='q_v'),
      path('list_into_country',Country_item.as_view(),name='into_country'),
      path('list_into_country/voyages_<str:country_code>:<str:country_name>',Voyage_List.as_view(),name='voyages'),
      path('list_into_country/voyages_<str:country_code>:<str:country_name>/Voyage_num<int:vo_id>',Voyage_cargos.as_view(),name='voyage_cargos'),
]