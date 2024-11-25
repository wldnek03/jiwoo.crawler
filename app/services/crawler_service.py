import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_jobs():
    url = 'https://www.saramin.co.kr/zf_user/jobs/list/domestic'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = [job.text.strip() for job in soup.select('.job_tit > a')]
    companies = [comp.text.strip() for comp in soup.select('.corp_name > a')]

    # 데이터 정제 및 중복 제거
    data = pd.DataFrame({'title': titles, 'company': companies})
    data.drop_duplicates(inplace=True)

    return data