import json
import riskdata

from database import Database


#
class RestfulModelling(Database):

    # get 요청시 로직
    def getWork(self, url):

        url = url['url']
        sql = "SELECT url_no,url,url_status,title,insert_time,update_time "
        sql += "FROM url_repository "
        sql += "WHERE url='{}';".format(url)
        result = {}
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("error : {}".format(e))
        if len(result) == 0:
            result = 'None'
        else:
            result = result[0]

        return result

    # Post 요청시 로직
    def postWork(self, url):

        sql = "INSERT INTO url_repository(url,url_status,title) "
        sql += "values({url} , {url_status} , {title} )".format(
            url=json.dumps(url.get("url", "")),
            url_status=json.dumps(riskdata.controlrisk(url)),
            title=json.dumps(riskdata.decide_title())
        )
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"PostWork Error": "{}".format(e)}

        return result

    # 업데이트 로직 
    def updateWork(self, time, url):
        sql = "UPDATE url_repository SET "
        sql += " update_time = '{}' , ".format(time)
        sql += " url_status = '{}' , ".format(
            json.dumps(riskdata.controlrisk(url)))
        sql += " title = '{}' , ".format(
            riskdata.decide_title())
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"UpdateWork Error": "{}".format(e)}

        return result
