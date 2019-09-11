# Create your views here.
from django.shortcuts import redirect,render,HttpResponse,reverse
from newapp.models import category,comment,news,users,Comm_Favo
import json
#跳转第一个页面index
from utils.new_sort import get_new,get_page,get_comment,ajax_favo_comment,ajax_del,hot_new
from  utils.new_sort import add_context,Rand_News
def first(request):
    return render(request,'newapp/advert.html')
    # return redirect(reverse('newapp:login'))#ti

#新闻首页
def main_new(request):
    yaowen_list,new_recommends = get_new().main_news()
    #精彩推荐
    rand_news=Rand_News()#随机新闻
    msg = ['推荐', '国内', '国际', '要闻', '科技', '体育', '财经']  # 用于列表循环
    name = request.session.get('login_username', None)
    nameid = request.session.get('nameID', None)
    return render(request, 'newapp/news_recommend.html',
                  {'name': name, 'nameid': nameid, 'msg': msg, 'yaowen_list': yaowen_list,
                   'new_recommends':new_recommends,'rand_news':rand_news})

#二级新闻
def child_new(request):
    # 将会在这里分类，并且将阅读量，时间来排序
    #新闻类型与当前页数
    p=int(request.GET.get('p',1))
    type = request.GET.get('type', '推荐')
    msg = ['推荐', '国内', '国际', '要闻', '科技', '体育', '财经']#用于列表循环
    new_obj = get_new()#创建对象
    new_list=new_obj.current_new(p,type)#调用方法，['object'，加三个label标签]
    page=get_page(type)#获取的是一个int
    page_list=[i for i in range(1,page+1)]#用在网页上进行迭代
    p_page=[p,page_list]

    name = request.session.get('login_username', None)
    nameid = request.session.get('nameID', None)
    #获取热点新闻:
    hot_news=hot_new()
    return render(request,'newapp/news_category.html',{'name':name,'nameid':nameid,
             'type':type,'msg':msg,'p_page':p_page,'new_list':new_list,'hot_news':hot_news})

#详细新闻
def detail_new(request):
    newid=request.GET.get('newid',None)
    new_obj=get_new()#没有屏蔽传值为空的情况，
    one_new=new_obj.detail_news(newid)#新闻详细内容
    if not newid:
        return redirect(reverse('newapp:index'))
    #------------------判断名字是否长期存在
    name = request.session.get('login_username', None)
    nameid = request.session.get('nameID', None)
    #如果名字和新闻详情页都存在，判断cookie是否存在，不存在阅读量+1
    cook_newid=request.COOKIES.get('newid',None)
    #判断是否为同一篇文章
    if nameid and newid!=cook_newid:
        newview=one_new.newView
        newview+=1
        obj=news.objects.filter(newID=newid).update(newView=newview)
    #推荐新闻

    Recommend_News,Look_News=get_new().recommend_news()
    res=render(request,'newapp/news_detail.html',{'name':name,'nameid':nameid,
                    'Recommend_News':Recommend_News,'Look_News':Look_News,'one_new':one_new,})
    res.set_cookie('newid',newid,max_age=300)
    return res
#广告页面
def advert(request):
    name = request.session.get('login_username', None)
    nameid = request.session.get('nameID', None)
    return render(request,'newapp/advert.html',{'name':name,'nameid':nameid})

#第一个页面主页面
def index(request):
    yaowen_list = get_new().index_new()[0]
    guonei_list = get_new().index_new()[1]
    guoji_list = get_new().index_new()[2]
    keji_list = get_new().index_new()[3]
    tiyu_list = get_new().index_new()[4]
    money_list = get_new().index_new()[5]
    rand_news = Rand_News()#主页面
    # current=int(request.GET.get('p',1))下一页
    # 简单的session传递
    name = request.session.get('login_username', None)
    nameid = request.session.get('nameID', None)
    return render(request, 'newapp/index.html',
                  {'name': name, 'nameid': nameid, 'yaowen_list': yaowen_list, 'guonei_list': guonei_list,
                   'guoji_list': guoji_list, 'keji_list': keji_list, 'tiyu_list': tiyu_list,
                   'money_list': money_list,'rand_news':rand_news})  # 是注销还是未登录在前端页面显示
#登陆页面处理

def login(request):
    request.session.clear()
    if request.method=='GET':
        message=request.COOKIES.get('warn','')
        return render(request, 'newapp/sign.html', {'message':message})
    elif request.method=='POST':
        name=request.POST.get('user')#标签 名登录是电话/邮箱和psd
        pwd=request.POST.get('pwd')
        if '@' in  str(name):
            obj=users.objects.filter(email=name,passWord=pwd).values().first()
            if obj:#验证正确
                name=obj['userName']
                nameid=obj['nameID']
                isadmin=obj['isAdmin']
                request.session['login_username'] =name#查询出来的是nameid和名字
                request.session['login_symbol'] = True
                request.session['nameID']=nameid
                request.session.set_expiry(60*5)#保存时间为10min
                res=redirect(reverse('newapp:index'))
                res.set_cookie('isadmin', isadmin)
            else:
                warn='邮箱密码错误'
                res=redirect(reverse('newapp:login'))#.set_cookie('warn',warn,max_age=1)
                res.set_cookie('warn', warn, max_age=2)
            return res
        else:
            obj = users.objects.filter(mobile=name,passWord=pwd).values().first()#需要使用.values()获取值
            if obj:
                name = obj['userName']
                # print(name)
                nameid = obj['nameID']
                isadmin = obj['isAdmin']
                request.session['login_username']=name
                request.session['login_symbol'] = True
                request.session['nameID'] = nameid
                request.session.set_expiry(60 * 30)
                res = redirect(reverse('newapp:index'))
                res.set_cookie('isadmin',isadmin)
            else:
                # print('1')
                warn='账号密码错误'
                # print(warn)
                #res = redirect(reverse('newapp:index'))
                res=redirect(reverse('newapp:login'))
                res.set_cookie('warn',warn,max_age=2)
            return res

#注销处理
def logout(request):
     request.session.clear()#删除当前session的值
     return redirect(reverse('newapp:index'))

# @my_login#装饰器，session登陆状态如果False
#注册逻辑处理
def register(request):
     if request.method=='POST':
         #表单验证
         name=request.POST.get('yhm')#获取用名字
         pwd=request.POST.get('pwd')#获取密码//不支持两次密码验证，js处理
         email_mobile=request.POST.get('user')#需要做一个验证是电话还是邮箱

         if '@' in str(email_mobile):
             email=email_mobile
             obj_e = users.objects.filter(email=email)
             obj_n= users.objects.filter(userName=name)
             if obj_e and obj_n:
                 warn='用户或邮箱已存在'
                 res = redirect(reverse('newapp:register'))
                 res.set_cookie('warn', warn, max_age=1)
             else:
                 creat_obj=users.objects.create(userName=name,passWord=pwd,email=email)
                 res=redirect(reverse('newapp:login'))##判断是
         elif len(str(email_mobile))==11:
             mobile=email_mobile
             obj_n=users.objects.filter(userName=name)
             obj_p=users.objects.filter(mobile=mobile)
             # obj_p=''
             if obj_p and obj_n:
                 warn='Existence'
                 res = redirect(reverse('newapp:register'))
                 res.set_cookie('warn', warn, max_age=1)
             else:
                 # print('完成')
                 creat_obj=users.objects.create(userName=name,mobile=mobile,passWord=pwd)
                 res=redirect(reverse('newapp:login'))
         else:
             warn='邮箱或电话错误'
             res=redirect(reverse('newapp:register'))
             res.set_cookie('warn',warn,max_age=1)
         return res
     elif request.method=='GET':
         warn=request.COOKIES.get('warn')#判断
         if not warn:
             warn=''
         return  render(request,'newapp/register.html',{'warn':warn})

#ajax对评论返回的信息
def ajax_get_comment(request):
    res = {'status': True, 'error': None, 'data': None}#将要返回的信息
    try:
        # msg=request.POST.get('newid')
        newid=request.COOKIES.get('newid',None)
        all_mess=get_comment(newid)
    except Exception as e:
        res['status']=False
        res['error']='获取评论失败'
    else:
        res['data']=all_mess
        return HttpResponse(json.dumps(res))

#ajax点赞
def ajax_favorite(request):
    res = {'status': True, 'error': None, 'data': None}
    #判断某人是否点过赞
    try:
        comment_ID=request.GET.get('commentid',None)#评论
        name_id=request.session.get('nameID',None)
        # newid=request.POST.get('newid')
        if comment_ID and name_id:
            #查看是否存在此人点赞
            obj=Comm_Favo.objects.filter(commentID=comment_ID,nameID=name_id)
            if not obj:
                obj1=ajax_favo_comment(int(comment_ID),int(name_id))#点赞+1
                res['data']='点赞成功'
        else:
            res['error']='点赞失败'
            res['status'] = False

    except:
        res['status']=False
        res['error']='点赞失败'
    else:
        return HttpResponse(json.dumps(res))

def ajax_del_comment(request):
    res={'status': True, 'error': None, 'data': None}
    try:
        commentid = request.GET.get('commentid')
        nameid = request.session.get('nameID',None)
        obj=users.objects.filter(nameID=nameid,isAdmin=1)
    except:
        res['status']=False
        res['error']='出现未知错误'
    else:
        if obj:
            o=ajax_del(commentid)
            if o:
                res['data']='删除成功!'
        return HttpResponse(json.dumps(res))

def ajax_add_comment(request):
    res = {'status': True, 'error': None, 'data': None}
    try:
        nameid=request.session.get('nameID',None)
        newid=request.COOKIES.get('newid',None),
        text=request.POST.get('context','')
        print(type(newid),type(nameid),type(text))
        if nameid and newid and text:
            nameid=int(nameid)
            newid = int(list(newid)[0])
            print('11')
            obj=add_context(nameid,newid,text)
            res['data'] = '添加成功'
        else:
            res['error']='请登陆在评论'
            res['status']=False
        return HttpResponse(json.dumps(res))
    except:
        res['status'] = False
        res['error'] = '出现未知错误'

#测试来用的
def test(request):
    obj=comment.objects.filter().all()
    print(obj)


