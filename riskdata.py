from pysafebrowsing import SafeBrowsing
s = SafeBrowsing('키값보호 ㅎㅎ ')
r = s.lookup_urls(['http://malware.testing.google.test/testing/malware/'])
r = r['http://malware.testing.google.test/testing/malware/']

threatslist = ['THREAT_TYPE_UNSPECIFIED', 'UNWANTED_SOFTWARE',
               'POTENTIALLY_HARMFUL_APPLICATION', 'SOCIAL_ENGINEERING', 'MALWARE']

platforms = {'PLATFORM_TYPE_UNSPECIFIED': 1, 'WINDOWS': 2, 'LINUX': 2, 'ANDROID': 2,
             'OSX': 2, 'IOS': 2, 'ANY_PLATFORM': 3,  'ALL_PLATFORMS': 4, 'CHROME': 2}


def riskrangemanagemnet():
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
    print(riskDecision(riskrange))


def riskDecision(a):
    if a == 0:
        return 'SAFE'
    elif 7 <= a < 9:
        return "some risk"
    elif 9 <= a < 12:
        return "risk "
    elif 12 <= a <= 14:
        return 'super danger'


if __name__ == "__main__":
    riskrangemanagemnet()
