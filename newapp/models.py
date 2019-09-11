from django.db import models

# Create your models here.
class users(models.Model):
    nameID=models.AutoField(primary_key=True)#时间序号
    userName=models.CharField(max_length=20,null=False,unique=True)
    passWord=models.CharField(max_length=10,null=False)
    email=models.EmailField(null=True)
    mobile=models.CharField(max_length=12,null=True)
    isAdmin=models.IntegerField(default=0)
class category(models.Model):
    categoryID=models.AutoField(primary_key=True)
    categoryName=models.CharField(null=False,max_length=20,unique=True)
    categoryDes=models.TextField()

class news(models.Model):
    newID=models.AutoField(primary_key=True)
    newTitle=models.CharField(max_length=50,null=False)
    newOrigin=models.CharField(max_length=20,null=False)#来源
    newDate=models.CharField(max_length=20,null=False)
    newView=models.IntegerField(default=0)#观看数
    newContent=models.TextField()
    newImage=models.URLField(null=False)#链接
    #关联新闻种类
    categoryID=models.ForeignKey(category,on_delete=models.CASCADE)
    newLabel=models.CharField(max_length=40,null=False)#标签
    newDes=models.TextField(null=True)#文章描述

#评论
class  comment(models.Model):
    commentID=models.AutoField(primary_key=True)
    nameID=models.ForeignKey(users,on_delete=models.CASCADE)
    newID=models.ForeignKey(news,on_delete=models.CASCADE)
    commentContent=models.TextField()
    commentDate=models.DateTimeField(auto_now_add=True)
    commentFavorite=models.IntegerField(default=0)#点赞数
#广告
class  advertis(models.Model):
    priority=models.IntegerField(default=0)#广告优先级
    advImageurl=models.URLField()
    advPageurl=models.URLField()
    advID=models.AutoField(primary_key=True)

class  Comm_Favo(models.Model):
    nameID=models.ForeignKey(users,to_field='nameID',on_delete=models.CASCADE)
    commentID=models.ForeignKey(comment,to_field='commentID',on_delete=models.CASCADE)
    isFavorite=models.IntegerField(default=0)


