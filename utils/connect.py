
import pymysql.cursors
from utils import resourse

# Connection to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             db='fty',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        # 标题 来源 时间 内容 图片 描述 标签
        guonei_news = resourse.news()
        guonei_news.get_page('https://temp.163.com/special/00804KVA/cm_guonei.js?callback=data_callback')
        sql = "INSERT INTO newapp_news (newTitle, newOrigin, newDate, newContent, " \
              "newImage, newDes, newLabel, categoryID_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 1)"
        for i in range(0, len(guonei_news.newTitle)):
            # print(
                  # guonei_news.newTitle[i], guonei_news.newOrigin[i], guonei_news.newDate[i],
                  # guonei_news.newImage[i],
                  # guonei_news.newDes[i],
                  # len(guonei_news.newLabel))
            cursor.execute(sql, (
                guonei_news.newTitle[i], guonei_news.newOrigin[i], guonei_news.newDate[i],
                guonei_news.newContent[i],
                guonei_news.newImage[i],
                guonei_news.newDes[i],
                guonei_news.newLabel[i]))
            connection.commit()
    with connection.cursor() as cursor:
        # Create a new record
        # 标题 来源 时间 内容 图片 描述 标签
        guoji_news = resourse.news()
        guoji_news.get_page('https://temp.163.com/special/00804KVA/cm_guoji.js?callback=data_callback')
        sql = "INSERT INTO newapp_news (newTitle, newOrigin, newDate, newContent, " \
              "newImage, newDes, newLabel, categoryID_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 2)"
        for i in range(0, len(guoji_news.newTitle)):
            cursor.execute(sql, (
                guoji_news.newTitle[i], guoji_news.newOrigin[i], guoji_news.newDate[i], guoji_news.newContent[i],
                guoji_news.newImage[i], guoji_news.newDes[i],
                guoji_news.newLabel[i]))
            connection.commit()
    with connection.cursor() as cursor:
        # Create a new record
        # 标题 来源 时间 内容 图片 描述 标签
        yaowen_news = resourse.news()
        yaowen_news.get_page('https://temp.163.com/special/00804KVA/cm_yaowen.js?callback=data_callback')
        sql = "INSERT INTO newapp_news (newTitle, newOrigin, newDate, newContent, " \
              "newImage, newDes, newLabel, categoryID_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 3)"
        for i in range(0, len(yaowen_news.newTitle)):
            cursor.execute(sql, (
                yaowen_news.newTitle[i], yaowen_news.newOrigin[i], yaowen_news.newDate[i],
                yaowen_news.newContent[i],
                yaowen_news.newImage[i],
                yaowen_news.newDes[i],
                yaowen_news.newLabel[i]))
            connection.commit()
    with connection.cursor() as cursor:
        # Create a new record
        # 标题 来源 时间 内容 图片 描述 标签
        tech_news = resourse.news()
        tech_news.get_page('https://temp.163.com/special/00804KVA/cm_tech.js?callback=data_callback')
        sql = "INSERT INTO newapp_news (newTitle, newOrigin, newDate, newContent, " \
              "newImage, newDes, newLabel, categoryID_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 4)"
        for i in range(0, len(tech_news.newTitle)):
            cursor.execute(sql, (
                tech_news.newTitle[i], tech_news.newOrigin[i], tech_news.newDate[i], tech_news.newContent[i],
                tech_news.newImage[i], tech_news.newDes[i],
                tech_news.newLabel[i]))
            connection.commit()
    with connection.cursor() as cursor:
        # Create a new record
        # 标题 来源 时间 内容 图片 描述 标签
        sports_news = resourse.news()
        sports_news.get_page('https://temp.163.com/special/00804KVA/cm_sports.js?callback=data_callback')
        sql = "INSERT INTO newapp_news (newTitle, newOrigin, newDate, newContent, " \
              "newImage, newDes, newLabel, categoryID_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 5)"
        for i in range(0, len(sports_news.newTitle)):
            cursor.execute(sql, (
                sports_news.newTitle[i], sports_news.newOrigin[i], sports_news.newDate[i], sports_news.newContent[i],
                sports_news.newImage[i], sports_news.newDes[i],
                sports_news.newLabel[i]))
            connection.commit()

    with connection.cursor() as cursor:
        # Create a new record
        # 标题 来源 时间 内容 图片 描述 标签


        money_news = resourse.news()
        money_news.get_page('https://temp.163.com/special/00804KVA/cm_money.js?callback=data_callback')
        sql = "INSERT INTO newapp_news (newTitle, newOrigin, newDate, newContent, " \
              "newImage, newDes, newLabel, categoryID_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, 6)"
        for i in range(0, len(money_news.newTitle)):
            cursor.execute(sql, (
                money_news.newTitle[i], money_news.newOrigin[i], money_news.newDate[i], money_news.newContent[i],
                money_news.newImage[i], money_news.newDes[i],
                money_news.newLabel[i]))
            connection.commit()
finally:
    connection.close()
