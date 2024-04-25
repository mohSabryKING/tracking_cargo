import phonenumbers
from phonenumbers import geocoder ,carrier
from opencage.geocoder import OpenCageGeocode
import folium
import math
from django.contrib import messages

from django_countries import countries

#number_p='+201501029717'
#number_p='+201099118405'
number_p='+201062524938'
def tracking_model_1():
 key_geo='056ebb16bfd642edadc394530547f305'
 check_num=phonenumbers.parse(number_p)
 number_locat=geocoder.description_for_number(check_num,'ar')
 number_provider=carrier.name_for_number(check_num,'ar')
 geo_locat=OpenCageGeocode(key_geo)
 q=str(number_locat)
 find_locat=geo_locat.geocode(q)
 len_y=find_locat[0]['geometry']['lat']*1.141796
 wid_x=find_locat[0]['geometry']['lng']*1.067708
 locat_x=folium.Map(location=[len_y,wid_x],zoom_start=2)
 #pay google:https://console.cloud.google.com/freetrial/signup/billing/EG?_gl=1*9uzi4c*_up*MQ..&gclid=19ff0df96eea1c36993c6bddb2c4129b&gclsrc=3p.ds&_ga=2.216489951.-831456188.1713691701&_gac=1.52552552.1713691702.19ff0df96eea1c36993c6bddb2c4129b&facet_utm_source=bing&facet_utm_campaign=emea-eg-all-ar-bkws-all-all-trial-e-gcp-1011340&facet_utm_medium=cpc&facet_url=https:%2F%2Fcloud.google.com%2Fgcp&facet_id_list=%5B97545651%5D&pli=1
 folium.Marker([len_y,wid_x],popup=number_locat).add_to(locat_x)
 locat_x.save("my_locat2.html")
 print("->"*10)

 print("the phone of :"+number_p)
 print("the called is from "+str(number_locat))
 print("the provider is "+str(number_provider))
 print("the co ordin is :"+str(len_y)+","+str(wid_x))
 #29.976766, 31.249200----->6,2
 print("the location on map is "+str(locat_x))
 print("->"*10)
 #x:
 '''

'''
#y
'''

'''









def make_list(class_x,counts):
      list_obj=[class_x.objects.create(pk=i) for i in range(counts)]
      print("->>-"*10)
      print(str(list_obj))
      print("->>-"*10)
      return list_obj


def lin_search(target):
    country_list=list(countries)
    output_list=[]
    for i in range(len(country_list)):
        if target==country_list[i][1] or (target in country_list[i][1]) or country_list[i][1].startswith(target):
            print("->>-"*10)
            print(country_list[i][0]+" at index of "+str(i)+" and starts with "+target)
            print(" Type of "+str(type(country_list[i])))
            print("->>-"*10)
            output_list.insert(i,country_list[i])
            return output_list


def Bin_search(target):pass



def count_obj_all(target_class):
    count_obj=target_class.objects.all().count()
    print("counter of the Model:"+str(count_obj))
    return count_obj

def count_obj_filter(target_class,val):
    count_obj=target_class.objects.filter(from_contry_x=val).count()
    print("counter of filtered Model:"+str(count_obj))
    return count_obj
    
    