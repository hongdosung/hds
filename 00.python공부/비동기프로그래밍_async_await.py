# 비동기 프로그래밍은 I/O 바운드 작업을 효율적으로 처리할 수 있는 강력한 도구입니다. 
# 파이썬은 asyncio 모듈과 async 및 await 키워드를 사용하여 비동기 프로그래밍을 지원합니다. 
# 이를 통해 네트워크 요청, 파일 읽기/쓰기 등 대기 시간이 발생하는 작업을 비동기적으로 처리하여 응답성을 높이고 성능을 최적화할 수 있습니다.
# 비동기 프로그래밍은 동시성을 제공하여, 여러 작업을 병렬로 수행할 수 있게 합니다. 
# async 키워드는 비동기 함수를 정의하며, await 키워드는 비동기 함수의 완료를 기다리는 데 사용됩

# asyncio 모듈은 비동기 프로그래밍을 위한 도구를 제공합니다.
# asyncio.run() 함수를 사용하여 비동기 함수를 실행합니다.
# asyncio.sleep() 함수를 사용하여 비동기 함수의 실행을 지연할 수 있습니다.
# asyncio 모듈은 이벤트 루프를 사용하여 비동기 함수를 실행하고 관리합니다.
# 비동기 함수는 다른 비동기 함수를 호출할 수 있습니다.
# 비동기 함수는 다른 비동기 함수의 실행을 기다릴 수 있습니다.
# 비동기 함수는 동기 함수를 호출할 수 없습니다.
# 비동기 함수는 동기 함수의 실행을 기다릴 수 없습니다.
# 비동기 함수는 asyncio.sleep() 함수를 사용하여 실행을 지연할 수 있습니다.
# 비동기 함수는 asyncio.create_task() 함수를 사용하여 다른 비동기 함수를 백그라운드에서 실행할 수 있습니다.
# 비동기 함수는 asyncio.gather() 함수를 사용하여 여러 비동기 함수를 병렬로 실행할 수 있습니다.
# 비동기 함수는 asyncio.wait() 함수를 사용하여 여러 비동기 함수를 순차적으로 실행할 수 있습니다.
# 비동기 함수는 asyncio.as_completed() 함수를 사용하여 여러 비동기 함수의 결과를 순서대로 처리할 수 있습니다.
# 비동기 함수는 asyncio.shield() 함수를 사용하여 다른 비동기 함수의 취소를 방지할 수 있습니다.
# 비동기 함수는 asyncio.TimeoutError 예외를 사용하여 비동기 함수의 실행 시간을 제한할 수 있습니다.
# 비동기 함수는 asyncio.Queue 클래스를 사용하여 비동기 함수 간에 데이터를 교환할 수 있습니다.
# 비동기 함수는 asyncio.Event 클래스를 사용하여 비동기 함수 간에 이벤트를 전달할 수 있습니다.
# 비동기 함수는 asyncio.Lock 클래스를 사용하여 비동기 함수 간에 상호 배제를 구현할 수 있습니다.
# 비동기 함수는 asyncio.Semaphore 클래스를 사용하여 비동기 함수 간에 병렬 처리를 제한할 수 있습니다.
# 비동기 함수는 asyncio.Condition 클래스를 사용하여 비동기 함수 간에 조건 변수를 사용할 수 있습니다.
# 비동기 함수는 asyncio.EventLoop 클래스를 사용하여 이벤트 루프를 직접 제어할 수 있습니다.
# 비동기 함수는 asyncio.subprocess 클래스를 사용하여 외부 프로세스를 비동기적으로 실행할 수 있습니다.
# 비동기 함수는 asyncio.run_coroutine_threadsafe() 함수를 사용하여 스레드에서 비동기 함수를 실행할 수 있습니다.
# 비동기 함수는 asyncio.run_until_complete() 함수를 사용하여 비동기 함수를 동기적으로 실행할 수 있습니다.
# 비동기 함수는 asyncio.create_unix_server() 함수를 사용하여 UNIX 소켓 서버를 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.create_unix_connection() 함수를 사용하여 UNIX 소켓 클라이언트를 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.start_server() 함수를 사용하여 TCP 서버를 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.open_connection() 함수를 사용하여 TCP 클라이언트를 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.start_unix_server() 함수를 사용하여 UNIX 소켓 서버를 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.start_unix_connection() 함수를 사용하여 UNIX 솼켓 클라이언트를 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.start_tls() 함수를 사용하여 TLS 연결을 비동기적으로 생성할 수 있습니다.
# 비동기 함수는 asyncio.start_server() 함수를 사용하여 SSL 연결을 비동기적으로 생성할 수 있습니다.

# aiohttp 라이브러리를 사용하여 비동기적으로 HTTP 요청을 처리할 수 있습니다.
# aiohttp.ClientSession 클래스를 사용하여 HTTP 클라이언트를 생성할 수 있습니다.
# aiohttp.ClientSession.get() 메서드를 사용하여 GET 요청을 보낼 수 있습니다.
# aiohttp.ClientSession.post() 메서드를 사용하여 POST 요청을 보낼 수 있습니다.
# aiohttp.ClientSession.put() 메서드를 사용하여 PUT 요청을 보낼 수 있습니다.
# aiohttp.ClientSession.delete() 메서드를 사용하여 DELETE 요청을 보낼 수 있습니다.
# aiohttp.ClientSession.request() 메서드를 사용하여 사용자 정의 HTTP 요청을 보낼 수 있습니다.
# aiohttp.ClientResponse 클래스를 사용하여 HTTP 응답을 처리할 수 있습니다.
# aiohttp.ClientResponse.text() 메서드를 사용하여 텍스트 응답을 읽을 수 있습니다.
# aiohttp.ClientResponse.json() 메서드를 사용하여 JSON 응답을 읽을 수 있습니다.
# aiohttp.ClientResponse.content() 메서드를 사용하여 이진 응답을 읽을 수 있습니다.
# aiohttp.ClientResponse.status 메서드를 사용하여 응답 상태 코드를 확인할 수 있습니다.
# aiohttp.ClientResponse.headers 메서드를 사용하여 응답 헤더를 확인할 수 있습니다.
# aiohttp.ClientTimeout 클래스를 사용하여 HTTP 요청 시간 제한을 설정할 수 있습니다.
# aiohttp.ClientError 클래스를 사용하여 HTTP 요청 오류를 처리할 수 있습니다.
# aiohttp.ClientConnectionError 클래스를 사용하여 HTTP 연결 오류를 처리할 수 있습니다.
# aiohttp.ClientResponseError 클래스를 사용하여 HTTP 응답 오류를 처리할 수 있습니다.
# aiohttp.ClientPayloadError 클래스를 사용하여 HTTP 페이로드 오류를 처리할 수 있습니다.
# aiohttp.ClientProxyConnectionError 클래스를 사용하여 HTTP 프록시 연결 오류를 처리할 수 있습니다.
# aiohttp.ClientSSLError 클래스를 사용하여 HTTP SSL 오류를 처리할 수 있습니다.
# aiohttp.ClientTimeoutError 클래스를 사용하여 HTTP 요청 시간 초과 오류를 처리할 수 있습니다.
# aiohttp.ClientOSError 클래스를 사용하여 HTTP OS 오류를 처리할 수 있습니다.
# aiohttp.ClientConnectorError 클래스를 사용하여 HTTP 연결 오류를 처리할 수 있습니다.
# aiohttp.ClientPayloadError 클래스를 사용하여 HTTP 페이로드 오류를 처리할 수 있습니다.
# aiohttp.ClientRequestError 클래스를 사용하여 HTTP 요청 오류를 처리할 수 있습니다.
# aiohttp.ClientResponseError 클래스를 사용하여 HTTP 응답 오류를 처리할 수 있습니다.
# aiohttp.ClientSession.close() 메서드를 사용하여 HTTP 클라이언트를 닫을 수 있습니다.
# aiohttp.ClientSession.closed 속성을 사용하여 HTTP 클라이언트가 닫혔는지 확인할 수 있습니다.
# aiohttp.ClientSession.connector 속성을 사용하여 HTTP 연결을 확인할 수 있습니다.
# aiohttp.ClientSession.cookie_jar 속성을 사용하여 HTTP 쿠키를 확인할 수 있습니다.
# aiohttp.ClientSession.connector.close() 메서드를 사용하여 HTTP 연결을 닫을 수 있습니다.
# aiohttp.ClientSession.connector.closed 속성을 사용하여 HTTP 연결이 닫혔는지 확인할 수 있습니다.
# aiohttp.ClientSession.connector.connect() 메서드를 사용하여 HTTP 연결을 열 수 있습니다.
# aiohttp.ClientSession.connector.connecting 속성을 사용하여 HTTP 연결이 열리는 중인지 확인할 수 있습니다.
# aiohttp.ClientSession.connector.limit 속성을 사용하여 HTTP 연결 제한을 확인할 수 있습니다.
# aiohttp.ClientSession.connector.limit = 100을 사용하여 HTTP 연결 제한을 설정할 수 있습니다.
# aiohttp.ClientSession.connector.limit_per_host 속성을 사용하여 호스트당 HTTP 연결 제한을 확인할 수 있습니다.
# aiohttp.ClientSession.connector.limit_per_host = 10을 사용하여 호스트당 HTTP 연결 제한을 설정할 수 있습니다.
# aiohttp.ClientSession.connector.proxy 속성을 사용하여 HTTP 프록시를 확인할 수 있습니다.
# aiohttp.ClientSession.connector.proxy = 'http://proxy.com'을 사용하여 HTTP 프록시를 설정할 수 있습니다.
# aiohttp.ClientSession.connector.proxy_auth 속성을 사용하여 HTTP 프록시 인증을 확인할 수 있습니다.
# aiohttp.ClientSession.connector.proxy_auth = aiohttp.Basic
# aiohttp.ClientSession.connector.proxy_auth.login = 'user'
# aiohttp.ClientSession.connector.proxy_auth.password = 'password'
# aiohttp.ClientSession.connector.proxy_auth = aiohttp.Basic(login='user', password='password')을 사용하여 HTTP 프록시 인증을 설정할 수 있습니다.
# aiohttp.ClientSession.connector.proxy_auth.login = 'user'을 사용하여 HTTP 프록시 인증 로그인을 설정할 수 있습니다.
# aiohttp.ClientSession.connector.proxy_auth.password = 'password'을 사용하여 HTTP 프록시 인증 비밀번호를 설정할 수 있습니다.
# aiohttp.ClientSession.connector.proxy_auth = aiohttp.Basic(login='user', password='password')을 사용하여 HTTP 프록시 인증을 설정할 수 있습니다.

# aiofiles 라이브러리를 사용하여 비동기적으로 파일을 읽고 쓸 수 있습니다.
# aiofiles.open() 함수를 사용하여 비동기 파일 객체를 생성할 수 있습니다.
# aiofiles.open() 함수는 async with 문과 함께 사용할 수 있습니다.
# aiofiles.open() 함수는 await 키워드를 사용하여 파일을 읽고 쓸 수 있습니다.
# aiofiles.open() 함수는 async for 문을 사용하여 파일을 반복할 수 있습니다.


import asyncio
import aiohttp
import aiofiles
import os

dir_path = 'hds/example_dir'

# say_hello 함수는 비동기 함수로 정의되었으며, await asyncio.sleep(1)을 사용하여 1초 동안 대기합니다. 
# asyncio.run 함수를 사용하여 이벤트 루프를 실행하고 비동기 함수를 호출합니다.
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
print(f"{'='*100}\n")


# task1과 task2는 동시에 실행되며, asyncio.gather를 사용하여 두 작업을 병렬로 처리합니다.
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
print(f"{'='*100}\n")

# aiohttp.ClientSession을 사용하여 비동기적으로 HTTP GET 요청을 보내고, 응답을 비동기적으로 처리합니다.
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main_html():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://example.com')
        print(html)

asyncio.run(main_html())
print(f"{'='*100}\n")

# aiofiles 라이브러리를 사용하여 파일을 비동기적으로 읽고 쓸 수 있습니다.
async def write_file():
    async with aiofiles.open(os.path.join(dir_path, 'example.txt'), mode='w') as file:
        await file.write('Hello, async world!')

async def read_file():
    async with aiofiles.open(os.path.join(dir_path, 'example.txt'), mode='r') as file:
        contents = await file.read()
        print(contents)

async def main_file():
    await write_file()
    await read_file()

asyncio.run(main_file())
print(f"{'='*100}\n")

# 위 코드에서는 fetch 함수로 웹 페이지를 비동기적으로 다운로드하고, 
# save_to_file 함수로 비동기적으로 파일에 저장합니다.
# main 함수에서는 여러 URL을 동시에 처리하기 위해 asyncio.gather를 사용합니다.
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def save_to_file(filename, content):
    async with aiofiles.open(os.path.join(dir_path, filename), 'w') as file:
        await file.write(content)

async def download_page(session, url, filename):
    content = await fetch(session, url)
    #print(content)
    await save_to_file(filename, content)

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
            filename = f'page_{i}.html'
            tasks.append(download_page(session, url, filename))
        await asyncio.gather(*tasks)

urls = ['http://example.com', 'http://example.org', 'http://example.net']
#urls = ['https://ezportal.bizmeka.com']
asyncio.run(main(urls))

# 위 코드에서는 fetch 함수로 웹 페이지를 비동기적으로 다운로드하고, save_to_file 함수로 비동기적으로 파일에 저장합니다. 
# main 함수에서는 여러 URL을 동시에 처리하기 위해 asyncio.gather를 사용합니다.
# async 및 await 키워드와 asyncio 모듈을 사용하면, 복잡한 비동기 작업을 간단하고 효율적으로 구현할 수 있습니다.

print(f"{'='*100}\n")


from bs4 import BeautifulSoup

def parse_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        yield link.get('href')

async def fetch_html_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def save_to_file_async(filename, content):
    async with aiofiles.open(os.path.join(dir_path, filename), 'w') as file:
        await file.write(content)

async def process_page_async(url):
    print(f'url => {url}')
    html = await fetch_html_async(url)
    links = list(parse_links(html))
    print(f'link => {links}')
    await save_to_file_async(f'{url.replace("http://", "").replace("/", "_")}.txt', '\n'.join(links))
    print(f"Processed {url} with {len(links)} links")

async def main_async(urls):
    tasks = [process_page_async(url) for url in urls]
    await asyncio.gather(*tasks)

# 예제 실행
urls = ['http://example.com', 'http://example.org', 'http://example.net']
asyncio.run(main_async(urls))