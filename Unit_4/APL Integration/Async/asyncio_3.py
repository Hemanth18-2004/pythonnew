import asyncio , time , aiohttp

''' Used for asynchronous HTTP Requests '''

URL = ['https://google.com',
       'https://example.com',
       'https://www.python.org',
       'https://httpbin.org',
       ]

async def fetch(session, url):
    ''' One HTTP request per call '''
    start = time.time()
    try:
        async with session.get(url, timeout = 10) as resp:
            ''' A GET request is sent to the URL
                The coroutine waits for the response
                Control is returned to the event loop during '''
            ''' Wait '''
            await resp.read()
            ''' Read the full response body '''
            end = time.time()
            taken = round(end-start, 2)
            return url, resp.status, taken
