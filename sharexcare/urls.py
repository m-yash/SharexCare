from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$',views.index,name='home'),
    
    url(r'^home',views.explorePage,name='explorepage'),

    url(r'^signin',views.signin,name='signin'),
    url(r'^signup',views.signup,name='signup'),

    url(r'^explore',views.login_user,name='login'),
    url(r'^saved',views.saved,name='saved'),

    url(r'^post',views.create_post,name='create_post'),
    url(r'CreateShare',views.post_save,name='save_post'),
     
    #url(r'',views.logoutUser, name='logout'),

    path('/profile/<id>',views.profile_view,name='profile_view'),

    url(r'user_profile',views.loggedin_users_profile_view,name='user_profile_view'),

    path('/share/<title>',views.feedRead,name='feed_read'),
    #path('/profile/<id>',views.profile_view,name='profile_view'),
    
 
]