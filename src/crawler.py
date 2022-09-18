import requests
import re
from bs4 import BeautifulSoup as bs

cookies = {
    'WMONID': 'D7IubHhBxjU',
    'daepyoSidoCd': '',
    'daepyoSiguCd': '',
    'mvmPlaceSidoCd': '',
    'mvmPlaceSiguCd': '',
    'rd1Cd': '',
    'rd2Cd': '',
    'realVowel': '35207_45207',
    'roadPlaceSidoCd': '',
    'roadPlaceSiguCd': '',
    'vowelSel': '35207_45207',
    'realJiwonNm': '%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8',
    'JSESSIONID': 'Ld9LcQP56aczchoLzc9AMKL2MuVc6eAYn3EaNWbvubb1tQOabZwf7f27IEs1AyuA.amV1c19kb21haW4vYWlzMQ==',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'WMONID=D7IubHhBxjU; daepyoSidoCd=; daepyoSiguCd=; mvmPlaceSidoCd=; mvmPlaceSiguCd=; rd1Cd=; rd2Cd=; realVowel=35207_45207; roadPlaceSidoCd=; roadPlaceSiguCd=; vowelSel=35207_45207; realJiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8; JSESSIONID=Ld9LcQP56aczchoLzc9AMKL2MuVc6eAYn3EaNWbvubb1tQOabZwf7f27IEs1AyuA.amV1c19kb21haW4vYWlzMQ==',
    'Origin': 'https://www.courtauction.go.kr',
    'Referer': 'https://www.courtauction.go.kr/InitMulSrch.laf',
    'Sec-Fetch-Dest': 'frame',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

# data = 'bubwLocGubun=1&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jpDeptCd=000000&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&notifyLoc=on&rd1Cd=&rd2Cd=&realVowel=35207_45207&rd3Rd4Cd=&notifyRealRoad=on&saYear=2022&saSer=&ipchalGbncd=000331&termStartDt=2022.09.17&termEndDt=2022.10.01&lclsUtilCd=&mclsUtilCd=&sclsUtilCd=&gamEvalAmtGuganMin=&gamEvalAmtGuganMax=&notifyMinMgakPrcMin=&notifyMinMgakPrcMax=&areaGuganMin=&areaGuganMax=&yuchalCntGuganMin=&yuchalCntGuganMax=&notifyMinMgakPrcRateMin=&notifyMinMgakPrcRateMax=&srchJogKindcd=&mvRealGbncd=00031R&srnID=PNO102001&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102001&_CUR_CMD=InitMulSrch.laf&_CUR_SRNID=PNO102001&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=&_LOGOUT_CHK=&_FORM_YN=Y'
# data = 'srnID=PNO102000&jiwonNm=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&bubwLocGubun=1&jibhgwanOffMgakPlcGubun=&mvmPlaceSidoCd=&mvmPlaceSiguCd=&roadPlaceSidoCd=&roadPlaceSiguCd=&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&rd1Cd=&rd2Cd=&rd3Rd4Cd=&roadCode=&notifyLoc=1&notifyRealRoad=1&notifyNewLoc=1&mvRealGbncd=1&jiwonNm1=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&jiwonNm2=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&mDaepyoSidoCd=&mvDaepyoSidoCd=&mDaepyoSiguCd=&mvDaepyoSiguCd=&realVowel=00000_55203&vowelSel=00000_55203&mDaepyoDongCd=&mvmPlaceDongCd=&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102000&_CUR_CMD=RetrieveMainInfo.laf&_CUR_SRNID=PNO102000&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=PNO102001&_LOGOUT_CHK=&_FORM_YN=Y'
data = 'srnID=PNO102000&jiwonNm=%B4%EB%B1%B8%C1%F6%B9%E6%B9%FD%BF%F8&bubwLocGubun=1&jibhgwanOffMgakPlcGubun=&mvmPlaceSidoCd=&mvmPlaceSiguCd=&roadPlaceSidoCd=&roadPlaceSiguCd=&daepyoSidoCd=&daepyoSiguCd=&daepyoDongCd=&rd1Cd=&rd2Cd=&rd3Rd4Cd=&roadCode=&notifyLoc=1&notifyRealRoad=1&notifyNewLoc=1&mvRealGbncd=1&jiwonNm1=%B4%EB%B1%B8%C1%F6%B9%E6%B9%FD%BF%F8&jiwonNm2=%BC%AD%BF%EF%C1%DF%BE%D3%C1%F6%B9%E6%B9%FD%BF%F8&mDaepyoSidoCd=&mvDaepyoSidoCd=&mDaepyoSiguCd=&mvDaepyoSiguCd=&realVowel=00000_55203&vowelSel=00000_55203&mDaepyoDongCd=&mvmPlaceDongCd=&_NAVI_CMD=&_NAVI_SRNID=&_SRCH_SRNID=PNO102000&_CUR_CMD=RetrieveMainInfo.laf&_CUR_SRNID=PNO102000&_NEXT_CMD=RetrieveRealEstMulDetailList.laf&_NEXT_SRNID=PNO102002&_PRE_SRNID=PNO102001&_LOGOUT_CHK=&_FORM_YN=Y'

response = requests.post('https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf', cookies=cookies, headers=headers, data=data)
response.raise_for_status()
soup = bs(response.text, "lxml")
# print('soup: ', soup.find(attrs={'class':'Ltbl_list_lvl0'}))
var1 = soup.find('tbody')
print('result:', var1.td.next_sibling.next_sibling.next_sibling.next_sibling.get_text())
# print('soup: ', soup)
# elements = soup.select('tbody tr td')
# elements = soup.select('/html/body/div/div[1]/div[4]/div[3]/div[2]/div[1]/form/div/ul[1]/li[2]/select[1]')
# elements = soup.select('ul li select option')
# //*[@id="idJiwonNm1"]
# /html/body/div/div[1]/div[4]/div[3]/div[2]/div[1]/form/div/ul[1]/li[2]/select[1]
# /html/body/div[1]/div[4]/div[3]/div[4]/form[1]/table/tbody/tr[1]
# (//*[@id="contents"]/div[4]/form[1]/table/tbody/tr[1]

# elements = soup.select('tbody tr td')
# print('elements: ', elements)

# for index, element in enumerate(elements, 1):
#     if element.text == re.compile("^대구"):
#         print("{}번째 정보: {}".format(index, element.text))