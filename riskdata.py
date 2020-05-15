from pysafebrowsing import SafeBrowsing

# Api 연동
s = SafeBrowsing('key_value')
# Data 입력 format
r = s.lookup_urls(['http://malware.testing.google.test/testing/malware/'])
r = r['http://malware.testing.google.test/testing/malware/']

# threatslist 인덱스를 위험 값 에 맞춰서 배열 선언
threatslist = ['THREAT_TYPE_UNSPECIFIED', 'UNWANTED_SOFTWARE',
               'POTENTIALLY_HARMFUL_APPLICATION', 'SOCIAL_ENGINEERING', 'MALWARE']

# 플랫폼은 겹치는 수가 많으므로 딕셔너리로 선언
platforms = {'PLATFORM_TYPE_UNSPECIFIED': 1, 'WINDOWS': 2, 'LINUX': 2, 'ANDROID': 2,
             'OSX': 2, 'IOS': 2, 'ANY_PLATFORM': 3,  'ALL_PLATFORMS': 4, 'CHROME': 2}

#
# 위험 정보 관리 로직
# 데이터 입력포멧 작업
#


def riskControl():
    riskrange = 0
    if r['malicious'] == False:
        riskrange = 0
    else:
        strplatforms = r['platforms']
        strplatforms = str(strplatforms)
        strplatforms = strplatforms.replace("['", '')
        strplatforms = strplatforms.replace("']", '')
        if platforms[strplatforms] != 0:
            riskrange += platforms[strplatforms]
        r2 = r['threats']
        if r2[0] in threatslist:
            riskrange += threatslist.index(r2[0])
    print(riskDecide(riskrange))


# 범위에 따라 위험정도를 판단
def riskDecide(a):
    if a == 0:
        return 'SAFE'
    elif 7 <= a < 9:
        return "some risk"
    elif 9 <= a < 12:
        return "risk "
    elif 12 <= a <= 14:
        return 'super danger'


if __name__ == "__main__":
    riskControl()
