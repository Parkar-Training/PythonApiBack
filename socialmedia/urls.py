from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from user import views
from user.views import UserD, User, emailOtp, OTP2, verifyOtp

from advanceProfile import views
from advanceProfile.views import Adv

from Posts.deletePost import dPost
from Posts.postPost import pPost

from frndlst.views import frnd, getF






#from user.views import LogIn#User
#UserList, UserDetail, User
#from user.views import showData

urlpatterns = [
    path('admin/', admin.site.urls),
   # url(r'^api/show/(?P<userId>\d+)/$', UserDetail.as_view(),name='user_list'),


  #  path('view/', showData(),name='show data')


   # url(r'^api/show/$', UserList.as_view(), name='user_list'),

    url(r'^api/signup$',view=User), #Signup
    url(r'^api/put$',view=User), #forgetPassword
    url(r'^api/emailOtp2$',view=emailOtp), #OTP Email

    url(r'^api/otp/(?P<userId>\d+)/$',emailOtp.as_view(),name = 'otp store'),
   # url(r'^api/otp$',view=OTP2.as_view()),
    url(r'^api/emailOtp$',emailOtp.as_view()),
    url(r'^api/delete/(?P<userId>\d+)/$',UserD.as_view(),name='delete user'),

    url(r'^api/deletePost/(?P<id>\d+)/$',dPost.as_view(),name='delete Post'),
    url(r'^api/post', pPost.as_view()),

    url(r'^postF$',view=getF),
#added new urls
    url(r'^api/login$', UserD.as_view()),
    url(r'^api/verify$', verifyOtp.as_view()),
    #url(r'^api/login$',view= LogIn)
    #url('api/sign_in', views.signin),
    #url('api/sign_up', views.sign_up),
    url(r'^api/advprof$', Adv.as_view()),
    url(r'^api/frndlst$', frnd.as_view())



]
