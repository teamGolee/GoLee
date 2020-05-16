import json
from database import Database
import riskdata


class RestfulModelling(Database):
    # Define get
    def getWork(self, url):
        url = url['url']
        sql = "SELECT url_no,url,url_status "
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

    def postWork(self, url):
        sql = "INSERT INTO url_repository(url,url_status) "
        sql += "values({url} , {url_status} )".format(
            url=json.dumps(url.get("url", "")),
            url_status=json.dumps(riskdata.riskControl(url))
        )
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"PostWork Error": "{}".format(e)}
        return result