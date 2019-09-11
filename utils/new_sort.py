# -*- coding: utf-8 -*-
#Author :The Y Devil
import os,django,datetime,time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new.settings")# project_name 项目名称
django.setup()
from newapp.models import news,comment,Comm_Favo
from random import randint
class get_new(object):
    def __init__(self):
        #传一个页数，根据请求页数来查找实时的数据库

        self.new_list=[]

    def current_new(self,current,type):
        self.current = current
        self.type = type
        start=(self.current-1)*3
        end=self.current*3
        #跨表连接查询
        #推荐时候没有办法
        if self.type=='推荐':
            new_objs = news.objects.all().order_by('-newView')[start:end]
        else:
            new_objs=news.objects.filter(categoryID__categoryName=self.type).order_by('-newView', 'newID')[start:end]
        self.new_list.append(new_objs)
        for new_obj in new_objs:
            label_list=[]
            for label in new_obj.newLabel.split(' '):
                if label!='':
                    label_list.append(label)
            self.new_list.append(label_list)
            # print(self.new_list)
        return self.new_list#返回对象总共四个

    def index_new(self):
        yaowen_news = news.objects.filter(categoryID=3)[:3]
        guonei_news = news.objects.filter(categoryID=1)[:5]
        guoji_news = news.objects.filter(categoryID=2)[:5]
        keji_news = news.objects.filter(categoryID=4)[:5]
        tiyu_news = news.objects.filter(categoryID=5)[:5]
        money_news = news.objects.filter(categoryID=6)[:5]
        return yaowen_news, guonei_news, guoji_news, keji_news, tiyu_news, money_news  # 返回对象总共四个

    def main_news(self):
        yaowen_news = news.objects.filter(categoryID=3)[:5]
        new_objs = news.objects.all().order_by('-newView')[:3]
        return yaowen_news,new_objs
    #获取详细新闻页
    def detail_news(self,newid):
        one_new=news.objects.get(newID=newid)
        return one_new
    def recommend_news(self):
        News_obj=news.objects.all().order_by('-newView', '-newDate')
        Recommend_News=News_obj[:5]#推荐
        Look_News=News_obj[5:10]#大家都在看
        return Recommend_News,Look_News

#获取各文章的评论
def get_comment(newid):
    all_com=[]
    commens=comment.objects.filter(newID_id=newid).values('commentID','commentContent','commentDate',
                'commentFavorite','nameID__userName', )\
        .order_by('-commentDate','commentFavorite')
    for com in commens:
        com['commentDate']=datetime.datetime.timestamp(com['commentDate'])
        all_com.append(com)
    return all_com
        #(datetime.datetime.timestamp(com['commentDate'])转换为时间戳

def ajax_favo_comment(commentid,name_id):
    #设置成为已点赞
    favos = Comm_Favo.objects.create(nameID_id=name_id, commentID_id=commentid,isFavorite=1)
    favos=comment.objects.filter(commentID=commentid,nameID_id=name_id).values('commentFavorite')
    favo=favos[0]['commentFavorite']
    favo+=1
    obj=comment.objects.filter(commentID=commentid).update(commentFavorite=favo)#添加成功

def ajax_del(commentid):
    obj=comment.objects.filter(commentID=commentid).delete()
    if obj:
        print('success')
    else:
        print('11')

#获取热点新闻newView
def hot_new():
    hot_objs = news.objects.all().order_by('-newView')[0:5]
    return hot_objs

def add_context(nameid,newid,context):
    #newid_r=newid[1]
    obj=comment.objects.create(nameID_id=nameid,newID_id=newid,commentContent=context,)



def get_page(type):#获取总页数
    new_obj = news.objects.filter(categoryID__categoryName=type)
    page,v=divmod(len(new_obj),3)
    if v:
        page+=1
    return page

#随机新闻，每次四个
def Rand_News():
    rand_news=news.objects.all()
    All_News_Page,Residue=divmod(len(rand_news),4)
    #开始切片
    A_News_Page=randint(0,All_News_Page+1)
    News_Obj=rand_news[4*(A_News_Page-1):4*A_News_Page]
    return News_Obj


if __name__ == '__main__':
    # P=get_new(1,'国际')
    # P.detail_new(4518)
    # get_comment(4518)
    # ajax_del(1)
    # add_context(1,4518,'1998')
    p=get_new()
    p.recommend_news()



  # {% for new_recomment in new_recommends %}
  #                           <li>
  #                               <div class="news-time">
  #                                   <img class="time-pic"  src="/static/img/time.png" alt="time">
  #                                   <span class="time-text">{{ new_recomment.newDate }}</span>
  #                               </div>
  #                               <a href="{% url 'newapp:detail_new' %}?newid={{ new_recomment.newID }}" class="item-main">
  #                                   <div class="news-banner"><img class="animate animate-scale" src="{{ new_recomment.newImage}}" alt="banner"></div>
  #                                   <div class="news-info">
  #                                       <h3 class="info-title">{{ new_recomment.newTitle|truncatechars:"22" }}</h3>
  #                                       <p class="info-desc">{{ new_recomment.newContent|truncatechars:"50" }}</p>
  #                                   </div>
  #                               </a>
  #                           </li>
  #                           {% endfor %}