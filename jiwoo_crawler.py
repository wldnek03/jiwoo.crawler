# https://www.saramin.co.kr/zf_user/search?company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchType=search&searchword={}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&pagecount=100
import datetime
import requests
from bs4 import BeautifulSoup
keyword = input("키워드를 입력하세요 : ")
allPage = input("몇 페이지까지 추출하시겠어요?")

for page in range(1, int(allPage)+1):
    soup = requests.get('https://www.saramin.co.kr/zf_user/search?company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchType=search&searchword={}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&pagecount=100'.format(keyword), headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(soup.text, 'html.parser')
    jobs = html.select('div.item_recruit')

    for job in jobs:
        try:
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            title = job.select_one('a')['title'].strip().replace(',','')
            company = job.select_one('div.area_corp > strong > a').text.strip()
            url = 'https://www.saramin.co.kr' + job.select_one('a')['href']
            deadline = job.select_one('span.date').text.strip()
            location = job.select('div.job_condition > span')[0].text.strip()
            experience = job.select('div.job_condition > span')[1].text.strip()
            requirement = job.select('div.job_condition > span')[2].text.strip()
            jobtype = job.select('div.job_condition > span')[3].text.strip()
            print(today, title, company, url, deadline, location, experience, requirement, jobtype)
        except Exception:
            pass
    #today = datetime.datetime.now().strftime('%Y-%m-%d')
