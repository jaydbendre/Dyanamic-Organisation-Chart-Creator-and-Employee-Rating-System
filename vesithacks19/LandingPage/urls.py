from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.index,name='index'),
    url(r'^(?P<id>\w{0,50})/team_member/$', views.team_member_dashboard_render, name="team_member"),
    url(r'^history/$', views.team_member_history, name="history"),
    url(r'^edit/$', views.edit, name="edit"),
    path('login',views.render_login,name="view_login"),
    path('login_check',views.login,name='login'),
    path('log_out',views.log_out,name='logout'),
    path('submit',views.check_if_submitted,name="check_if_submitted"),

    # url(r'^test/$', views.test, name="test"),
    # url(r'^history/$', views.history, name="history"),

    #url(r'^test/$', views.test, name="test"),
    #url(r'^history/$', views.team_member_history, name="history"),
    #url(r'^edit/$', views.edit, name="edit"),

    path('login',views.render_login,name="view_login"),
    path('login_check',views.login,name='login'),
    path('log_out',views.log_out,name='logout'),
    path('submit',views.check_if_submitted,name="check_if_submitted"),
	#url(r'^(?P<id>\w{0,50})/team_incharge/$', views.team_incharge_index, name="team_incharge_index"),
	path("team_incharge/<int:id>", views.team_incharge_index, name="team_incharge_index"),
    url(r'^rating/$', views.rating, name="rating"),
    #url(r'^test/$', views.test, name="test"),
    #url(r'^history/$', views.history, name="history"),
    #url(r'^edit/$', views.edit, name="edit"),
    path('login_check',views.login,name="login_check"),
    path('team_member/dabba',views.render_dabba,name="render_dabba"),
    path('add_user',views.add_user,name="add_user"),

    #path('team_incharge_dabba', views.team_incharge_dabba, name="team_incharge_dabba"),
    # path('rating', views.rating, name="rating"),
    path('render_file_form',views.render_file_form,name="render_file_form"),
    path('admin_index', views.admin_index, name="admin_index"),
    url('createnotification',views.create_notification,name="display_notification"),
    url(r'^incharge_edit_profile/$', views.team_incharge_edit, name="incharge_edit"),
    path('simple_upload',views.simple_upload, name="file_upload")
]