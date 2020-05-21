from pysafebrowsing import SafeBrowsing


# url 요청을 받아서 GSB 형태 포멧에 따라 형태를 변환시켜줌
def controlrisk(url):

    s = SafeBrowsing('GSBKEY')
    url = url['url']
    r = s.lookup_urls([url])
    r = r[url]
    # threatlist 에 따른 데이터 형태 정렬 (인덱스 위치가 해당 위험정도임)
    threatslist = ['THREAT_TYPE_UNSPECIFIED', 
		   'UNWANTED_SOFTWARE',
                   'POTENTIALLY_HARMFUL_APPLICATION',
		   'SOCIAL_ENGINEERING',
		   'MALWARE']
    
    # platform 에 따른 데이터 형태 정렬 (중복값이 많으므로 딕셔너리로 선언 )
    platforms = {'PLATFORM_TYPE_UNSPECIFIED': 1,
                 'ANDROID': 2, 
		 'CHROME': 2,
                 'IOS': 2, 
                 'LINUX': 2,
                 'OSX': 2, 
 		 'WINDOWS': 2,
                 'ANY_PLATFORM': 3,  
                 'ALL_PLATFORMS': 4}

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

    return str(decide_risk(riskrange))


# 범위에 따라 위험정도를 판단
def decide_risk(a):
    if a == 0:
        return 'SAFE'
    elif 7 <= a < 9:
        return "some risk"
    elif 9 <= a < 12:
        return "risk "
    elif 12 <= a <= 14:
        return 'super danger'
