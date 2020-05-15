import json
from database import Database
import riskdata


class RestfulModelling(Database):

    # Define get
    def getWork(self, url):
        print("여기까진탓다?")
        sql = "SELECT url_no,url "
        sql += "FROM url_repostiory "
        sql += "WHERE url='{}';".format(url)
        print('Log Point 1  ', sql)
        result = {}
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            return("error : {}".format(e))

        result = {} if len(result) == 0 else result[0]

        return result

    def postWork(self, url):
        print('Postwork Test url.get("url")',
              url.get("url"), type(url.get("url")))
        sql = "INSERT INTO url_repository(url) "
        sql += "values('{url}')".format(url=json.dumps(url.get("url", "")))
        print(sql)
        result = None
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            result = {"PostWork Error": "{}".format(e)}
        return result
