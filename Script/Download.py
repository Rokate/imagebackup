import requests
import traceback
import aiohttp
import asyncio
import aiofiles
import re


if __name__ == '__main__':
    headers = {
    'authority': 'his.whboligj.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://macau-jc.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://macau-jc.com/',
    'accept-language': 'zh-CN,zh;q=0.9',}

    try:
        restime = requests.post('https://his.whboligj.com/api/CurrentInfo', headers=headers, data='{"lotteryId":2032}')

    except Exception as e:
        print('出错了',traceback.format_exc())
    else:
        print(restime.json()['data']['issue'][-3:])
