# -*- coding: utf-8 -*-
#Author :The Y Devil
from newapp import views
from  django.urls import path,re_path
app_name='newapp'
urlpatterns = [
       re_path(r'^$',views.index),
       path(r'new/index',views.index,name='index'),
       path(r'new/register',views.register,name='register'),
       path(r'new/login',views.login,name='login'),
       path(r'new/logout',views.logout,name='logout'),
       path(r'new/test',views.test,name='test'),
       path(r'new/main_new',views.main_new,name='main_new'),#主页新闻路由
       path(r'new/child_new',views.child_new,name='child_new'),#二级新闻路由
       path(r'new/detail_new',views.detail_new,name='detail_new'),#详细新闻路由//未完善，传值匹配
       path(r'new/advert',views.advert,name='advert'),
       path(r'new/ajax_get_comment',views.ajax_get_comment,name='ajax_get_comment'),
       path(r'new/ajax_del_comment',views.ajax_del_comment,name='ajax_del_comment'),
       path(r'new/ajax_add_comment',views.ajax_add_comment,name='ajax_add_comment'),
       path(r'new/ajax_favorite',views.ajax_favorite,name='ajax_favorite')
]