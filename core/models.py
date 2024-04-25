from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
import datetime

from django_countries.fields import CountryField,Country
from django_countries import countries

title_model='Let\'s Get In Touch!'
para_model='''
I'm not sure what more context I could give; I just want the person entering the date in to not have to change it to 10:00 every single time they add a new event (but still have the option to change it). The solution is admittedly simple if there is one; that looks like it might work

'''

# Create your models here.
class User_profile_Model(models.Model):
      #---user_x = models.OneToOneField(User,related_name='has_profile', on_delete=models.CASCADE)
      user_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
      user_email = models.EmailField(max_length=200,verbose_name='your email',default='contact@egye.com')
      
      
      made_in = models.DateTimeField(auto_now=True)
      
      

      def __str__(self):
            return str(self.pk)
      def mail_me(self):
            return format_html(f"<a href='mailto:{self.user_email}' class='mail_btn' id='mail_num{self.pk}'> Send an email</a>")

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'User_profile_Model'
            verbose_name_plural = 'User_profile_Model'



class Voyage_tracking_info(models.Model):
      #'posted_by','ship_name','from_country_x','from_time','to_country_y','to_time','made_in','bio','start_d','end_d',
      #---posted_by = models.ForeignKey(User, related_name='added_by', on_delete=models.CASCADE)
      ship_name = models.CharField(max_length=30, blank=True, null=True,verbose_name='ship_name',default="MAERSK")
      from_contry_x =  models.CharField(max_length=50,  null=True, choices=CountryField().choices + [(str(countries[0:][1]), 'Select Country')])
      #from_contry_x = CountryField(verbose_name="from")
      from_time = models.TimeField(auto_now=False, auto_now_add=False,verbose_name='start voyage time',default=datetime.time(16, 00))
      date_of_sail = models.DateField(auto_now=False, auto_now_add=False,verbose_name='start sailing date',default=datetime.date(2022, 1,5))
      
      to_contry_y =  models.CharField(max_length=50,  null=True, choices=CountryField().choices + [(CountryField().name, 'Select Country')])
      #to_contry_y = CountryField(verbose_name='to')
      
      to_time = models.TimeField(auto_now=False, auto_now_add=False,verbose_name='end voyage time',default=datetime.time(23, 00))
      arrival_date= models.DateField(auto_now=False, auto_now_add=False,verbose_name='start arrival date',default=datetime.date(2022, 3,12))
      doc_status = models.BooleanField(verbose_name="documentary status",default=True)
      
      made_in = models.DateTimeField(auto_now=True)
      info = models.TextField(verbose_name="details",default=para_model,max_length=300)
      
      
      def doc_status_validation(self):
            if self.doc_status :return format_html(f"<b class='msg sus'>ISSUED</b>")
            else:return format_html(f"<b class='msg err'> NOT ISSUED</b>")

      def __str__(self):
            return "VOYAGE NUM:"+str(self.pk)+"-->"+self.ship_name
      def start_date(self):return "ETS:"+str(self.date_of_sail)
      def end_date(self):return "ETA:"+str(self.arrival_date)
      def tracking_status(self):
            if self.pk:
                  if self.date_of_sail==datetime.date.today():
                        print("order created and stored for security issues")
                        return format_html(f"<b class='msg warn'>ON CREATION</b>")
                  else:
                        print("order created and siled")
                        return format_html(f"<b class='msg sus'>ISSUED</b>")
            else:
                  return format_html(f"<b class='msg err'> NOT ISSUED</b>")
      def country_A(self):
            print(f"from {Country(code=self.from_contry_x)}")
            return str(Country(code=self.from_contry_x).name)
      def country_B(self):
            print(f"to {Country(code=self.to_contry_y).name} :{self.to_contry_y}")
            return str(Country(code=self.to_contry_y).name)
      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Voyage_tracking_info'
            verbose_name_plural = 'Voyage_tracking_info'



class Cargo_info(models.Model):
      #'part_of','cargo_title','info'
      part_of= models.ForeignKey(Voyage_tracking_info, related_name='member_of',null=True, on_delete=models.CASCADE)
      cargo_title = models.CharField(max_length=30, blank=True, null=True,verbose_name='ship_name',default=title_model)
      info = models.TextField(verbose_name="details",default=para_model,max_length=300)
      made_in = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.cargo_title

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Cargo_info'
            verbose_name_plural = 'Cargo_info'



class Orders(models.Model):
      shipping_x = models.ForeignKey(Voyage_tracking_info, related_name='shipping_line', on_delete=models.CASCADE)
      order_x = models.ForeignKey(Cargo_info, related_name='order_x', on_delete=models.CASCADE)

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Ordes'
            verbose_name_plural = 'Ordes'