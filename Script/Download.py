import requests
import traceback
import aiohttp
import asyncio
import aiofiles
import re


async def download_image(session, url, filepath):
    
    try:
        async with session.get(url) as response:
            if response.headers["Content-Type"] == "image/jpeg":
                async with aiofiles.open(filepath, "wb") as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
            else:
                print(filepath + "下载出错了")
    except Exception as e:
        print("下载出错:\t", url, repr(e))


async def main(a, b, c):
    qishu = a
    qish = b
    qs = c
    urls = [
        [f"https://www.353583.com/tutu/faf{qishu}.jpg", "a-faf.jpg"],
        [f"https://www.353583.com/tutu/fgmc{qishu}.jpg", "a-fgmc.jpg"],
        [f"https://www.353583.com/tutu/6i12m{qishu}.jpg", "a-6i12m.jpg"],
        [f"https://www.353583.com/tutu/gd{qishu}.jpg", "a-gd.jpg"],
        [f"https://www.353583.com/tutu/lhwt{qishu}.jpg", "a-lhwt.jpg"],
        [f"https://www.353583.com/tutu/ugyf{qishu}.jpg", "a-ugyf.jpg"],
        [f"https://69760b.com/img/amhg{qishu}.jpg", "a-amhg.jpg"],
        [f"https://69760b.com/img/nm4x8m{qishu}.jpg", "a-nm4x8m.jpg"],
        [f"http://123186a.com/gsbtu/baoma{qishu}.jpg", "a-baoma.jpg"],
        [f"http://123186a.com/gsbtu/hdjr{qishu}.jpg", "a-hdjr.jpg"],
        [f"https://69760b.com/img/jl3x{qishu}.jpg", "a-jl3x.jpg"],
        [f"https://www.353583.com/tutu/ujcc{qishu}.jpg", "a-ujcc.jpg"],
        [f"https://www.29761b.com/img/djpt{qishu}.jpg", "a-djpt.jpg"],
        [f"https://69760b.com/img/1xzt{qishu}.jpg", "a-1xzt.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/zbxyb.jpg", "a-zbxyb.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/n1.jpg", "a-n1.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/dcxj.jpg", "a-dcxj.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/ampm.jpg", "a-ampm.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/sszm.jpg", "a-sszm.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/ktzsx.jpg", "a-ktzsx.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/rv.jpg", "a-rv.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/tt38.jpg", "a-tt38.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/amffh.jpg", "a-amffh.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/amfql.jpg", "a-amfql.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/twqp.jpg", "a-twqp.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/mfpy.jpg", "a-mfpy.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/lhlxsm.jpg", "a-lhlxsm.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/b8.jpg", "a-b8.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/tjn.jpg", "a-tjn.jpg"],
        [f"https://tk2.qingxinmingxiang.com:4949/col/{qish}/ampt.jpg", "a-ampt.jpg"],    
        ["https://67292b.com/tu/f011.jpg", "a-f011.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/n1.jpg", "x-n1.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/b002.jpg", "x-b002.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/b004.jpg", "x-b004.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/b006.jpg", "x-b006.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/b008.jpg", "x-b008.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/j11.jpg", "x-j11.jpg"],
        [f"https://tk.qingxinmingxiang.com:4949/col/{qs}/qlb.jpg", "x-qlb.jpg"],

    ]
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = []
        for i, url in enumerate(urls):
            filename = "./Script/Src/" + url[1]
            task = asyncio.create_task(download_image(session, url[0], filename))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def downloadamimg():
    amimg = [
         ["https://xam666.003123lhzz.xyz/js8/tu/4.jpg","a-mj.jpg"],
        ["https://xam666.003123lhzz.xyz/js8/tu/lxx.png","a-shxg.png"],
    ]
    for i, url in enumerate(amimg):
        response = requests.get(url[0])
        file_path = "./Script/Src/" + url[1]
        with open(file_path, 'wb') as f:
            f.write(response.content)


async def downloadxgimg():
    xgimg = [
        [
            "https://xgtk.003123.work/index.php?c=119",
            '<th><a href="(.*?)">',
        ],
        [
            "https://xgtk.003123.work/index.php?c=17",
            '<th><a href="(.*?)">',
        ],
    ]
    y = 0
    data = {"password": "003123.com"}
    for url in xgimg:
        pic = str(y)
        y = y + 1
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url[0],data=data) as resp:
                    page = await resp.text()
                    pattern = re.compile(url[1])
                    m = re.findall(pattern, page)
                    async with session.get(m[0]) as resp:
                        page2 = await resp.text()
                    pattern2 = re.compile('InterPhoto.image.php(.*?)"')
                    m2 = re.findall(pattern2, page2)
                    headers = {
                        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98"',
                        "Referer": m[0],
                        "sec-ch-ua-mobile": "?0",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36",
                        "sec-ch-ua-platform": '"Windows"',
                    }
                    picfile = await session.get(
                        "https://xgtk.003123.work/InterPhoto.image.php" + m2[0],
                        headers=headers,
                    )
                    async with aiofiles.open(f"./Script/Src/xgpic{pic}.jpg", "wb") as f:
                        while True:
                            chunk = await picfile.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)
        except Exception as e:
            print("下载出错:\t", url[0], repr(e))


if __name__ == "__main__":
    #a6.003123.club
    try:
        #amcode = {"code": "71"}
        qishu = requests.post('https://am49.app/open/latest?code=71').json()['data']['nextIssueNo'][-3:]
        qish = qishu.lstrip('0')
        
        #xgcode = {"code": "28"}
        qs = requests.post('https://am49.app/open/latest?code=28').json()['data']['nextIssueNo'][-3:].lstrip('0')
    except Exception as e:
        print("日期更新出错了", traceback.format_exc())
    else:
        print("图片列表下载。。。")
        asyncio.run(main(qishu, qish, qs))
        print("am图片下载。。。")
        asyncio.run(downloadamimg())
        print("xg图片下载。。。")
        asyncio.run(downloadxgimg())
