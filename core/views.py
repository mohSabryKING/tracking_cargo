from django.shortcuts import *
from .Form_x import *

from django.views.generic import *
from django.views.generic.base import *
from django.contrib.auth import *
from django.utils.html import format_html
from django.contrib import messages as msg
from .models import *
from django.core.exceptions import ObjectDoesNotExist

from .Action_1 import *

from django_countries import countries
#import get_countries as countries 



class Add_user_page(CreateView):
      template_name="registration/add_user.html"
      model=User
      form_class=Add_user_form
      def get_context_data(self, **kwargs):
          context = super(Add_user_page, self).get_context_data(**kwargs)
          print("\n\n\n\nthe created username "+str(self.request.user.username)+"\n\n\n\n")
          #login(self.request.user.username,'home')
          return context
      
class Home_page(TemplateView):
      template_name="home.html"
      def get_context_data(self, **kwargs):
          context = super(Home_page, self).get_context_data(**kwargs)


         

          '''
          context['voy_countrys']=make_list(Voyage_tracking_info,20)
          context['voy_cargos']=make_list(Cargo_info,10)
          '''
          return context

#html/cargo/find_item.html


def find_voyage_cargos(h):
    voyages_cargos=None
    if h.method=='GET':
        if 'q_cargo' in h.GET:
            target=h.GET['q_cargo']
            voyages_cargos=Cargo_info.objects.get(pk__icontains=target)
    else:
         voyages_cargos=Cargo_info.objects.all()

        
    return render(h,'find/cargo_item.html',{'voyages':voyages_cargos})


def find_voyages(h):
    voyages_list=None
    if h.method=='GET':
        if 'q_voy' in h.GET:
            target=h.GET['q_voy']
            voyages_list=Voyage_tracking_info.objects.get(pk=target)
    else:
         voyages_list=Voyage_tracking_info.objects.all()

        
    return render(h,'find/ship_item.html',{'voyages':voyages_list})




class Country_item(TemplateView):
      template_name="list/country.html"
      def get_context_data(self, **kwargs):
          context = super(Country_item, self).get_context_data(**kwargs)
          target_count=None
          if self.request.method=="GET":
           if 'q_voy_into' in self.request.GET:
               target_count=self.request.GET['q_voy_into']
               print(f"\n\nthe target country {target_count[0:][1]}\n\n")
               list_countrys=list(countries)
               print(f"\n\nthe target country {target_count in countries[0:][1]} \n\n")
               
               context['main_country']=lin_search(target_count)
               print("search result:\n"+str(context['main_country']))
               '''
               '''
               #context['countries_of']=lin_search(target_count)    
          
          return context

# Create your views here.




class Voyage_List(TemplateView):
    template_name='list/voyages.html'
    def get_context_data(self, **kwargs):
        context = super(Voyage_List, self).get_context_data(**kwargs)
        
        the_country_c=self.kwargs['country_code']
        the_country_n=self.kwargs['country_name']
        context['target_country']=the_country_c
        context['max_filter']=None
        if self.request.method=='GET':
          if 'ship_id' in self.request.GET:
            ship_order_id=self.request.GET['ship_id']
            print("\ngetting ship number:"+str(ship_order_id))
            #msg.error(self.request," order number:"+str(self.request.GET['ship_id'])+" IS INVALID")
            msg.success(self.request," order number:"+str(ship_order_id)+" found")
            #msg.info(self.request," order number:"+str(self.request.GET['ship_id'])+" was added once")
            #msg.warning(self.request," order number:"+str(self.request.GET['ship_id'])+" is NOT ISSUED")
            try: context['target_voy']=Voyage_tracking_info.objects.get(pk=ship_order_id)
            except ObjectDoesNotExist:
             msg.error(self.request,"order number:"+str(ship_order_id)+" NOT found")
             print("ERROR FOUND")
             context['target_voy']=[]
        context['voy_filter']=Voyage_tracking_info.objects.filter(from_contry_x=the_country_c)
        context['max_filter']=count_obj_all(Voyage_tracking_info)
        context['country_c']=the_country_c
        context['country_n']=the_country_n
        print("\ntarget country:"+str(the_country_c)+"\n")
        return context


class Voyage_cargos(TemplateView):
    template_name='list/voyage_cargos.html'
    def get_context_data(self, **kwargs):
        context = super(Voyage_cargos, self).get_context_data(**kwargs)
        country_into=self.kwargs['country_x']
        ship_id=self.kwargs['vo_id']
        print("voyage headed to a country of  "+str(country_into)+" with ship_id"+str(ship_id))
        context['main_ship']=Voyage_tracking_info.objects.get(pk=ship_id)
        context['ship_cargos']=Cargo_info.objects.filter(part_of=ship_id)

        return context
