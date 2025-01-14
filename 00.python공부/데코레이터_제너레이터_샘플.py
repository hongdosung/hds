# 데코레이터를 사용하여 함수 실행 시간을 측정하고, 제너레이터를 사용하여 대용량 데이터를 처리합니다.

import time
import requests
from bs4 import BeautifulSoup

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def fetch_html(url):
    response = requests.get(url)
    return response.text

def parse_links(html):
    soup = BeautifulSoup(html, 'html.parser') # 첫번째 인자: response의 body를 텍스트로 전달, 두번째 인자: "html"로 분석한다는 것을 명시
    for link in soup.find_all('a'):
        print(link)
        yield link.get('href')

# 예제 실행
url = 'http://example.com'
html = fetch_html(url)
print(html+'\n')
for link in parse_links(html):
    print(link)

# 위 코드에서는 timer_decorator를 사용하여 fetch_html 함수의 실행 시간을 측정하고, 
# parse_links 제너레이터를 사용하여 HTML 문서에서 링크를 추출합니다.