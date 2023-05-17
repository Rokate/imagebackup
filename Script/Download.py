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
        [f"https://49629a.com/img/amhg{qishu}.jpg", "a-amhg.jpg"],

        [f"https://49629a.com/img/nm4x8m{qishu}.jpg", "a-nm4x8m.jpg"],
        [f"http://123186a.com/gsbtu/baoma{qishu}.jpg", "a-baoma.jpg"],
        [f"http://123186a.com/gsbtu/hdjr{qishu}.jpg", "a-hdjr.jpg"],
        [f"https://49629a.com/img/jl3x{qishu}.jpg", "a-jl3x.jpg"],
        [f"https://www.353583.com/tutu/ujcc{qishu}.jpg", "a-ujcc.jpg"],
        [f"https://www.29761b.com/img/djpt{qishu}.jpg", "a-djpt.jpg"],
        [f"https://49629a.com/img/1xzt{qishu}.jpg", "a-1xzt.jpg"],

        ["https://67292b.com/tu/f011.jpg", "a-f011.jpg"],

    ]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(urls):
            filename = "./Script/Src/" + url[1]
            task = asyncio.create_task(download_image(session, url[0], filename))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def downloadamimg():
    amimg = [
        "https://amtutu.003123.club/index.php?c=5",
        "https://amtutu.003123.club/index.php?c=2",
    ]
    y = 0
    data = {"password": "003123.com"}
    for url in amimg:
        pic = str(y)
        y = y + 1
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=data) as resp:
                    page = await resp.text()
                    pattern = re.compile('Title: <a href="(.*?)">No Title')
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
                        "https://amtutu.003123.club/InterPhoto.image.php" + m2[0],
                        headers=headers,
                    )
                    async with aiofiles.open(f"./Script/Src/ampic{pic}.jpg", "wb") as f:
                        while True:
                            chunk = await picfile.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)
        except Exception as e:
            print("下载出错:\t", url, repr(e))


async def downloadxgimg():
    xgimg = [
        [
            "https://xgtutu.003123.club/index.php?c=3",
            'Title: <a href="(.*?)">马经',
        ],
        [
            "https://xgtutu.003123.club/index.php?c=17",
            'Title: <a href="(.*?)">守护幸福',
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
                        "https://xgtutu.003123.club/InterPhoto.image.php" + m2[0],
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
        print("保存html")
        temp = """
<h1 align="center" style="color:red ; font-size:50px">澳门图片</h1><iframe src="https://zhibo.ahntsy.com:777/" height="180" width=100% title="澳门开奖"></iframe><div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/n1.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/n1.jpg" / ><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/rv.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/rv.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/dcxj.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/dcxj.jpg" / ><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/sszm.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/sszm.jpg" / ></div><div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-faf.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-faf.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-fgmc.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-fgmc.jpg" / ></div><div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-6i12m.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-6i12m.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-gd.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-gd.jpg" / ></div><div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-lhwt.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-lhwt.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-ugyf.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-ugyf.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/ktzsx.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/ktzsx.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-amhg.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-amhg.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/zbxyb.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/zbxyb.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-nm4x8m.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-nm4x8m.jpg" / ></div><div align="center" class="imgblock"><a href="https://123186a.com/gsbtu/baoma{qish}.jpg" target="_blank"><img src="https://123186a.com/gsbtu/baoma{qish}.jpg" / ><a href="https://123186a.com/gsbtu/hdjr{qish}.jpg" target="_blank"><img src="https://123186a.com/gsbtu/hdjr{qish}.jpg" / ></div><div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/ampic0.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/ampic0.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/ampic1.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/ampic1.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/tt38.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/tt38.jpg" / ><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/amffh.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/amffh.jpg" / ></div>
<div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/amfql.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/amfql.jpg" / ><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/twqp.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/twqp.jpg" / ></div>
<div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-jl3x.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-jl3x.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-ujcc.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-ujcc.jpg" / ></div>
<div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-djpt.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-djpt.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-1xzt.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-1xzt.jpg" / ></div>
<div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/lhlxsm.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/lhlxsm.jpg" / ><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/b8.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/b8.jpg" / ></div>
<div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/mfpy.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/mfpy.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-f011.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/a-f011.jpg" / ></div>
<div align="center" class="imgblock"><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/tjn.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/tjn.jpg" / ><a href="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/ampt.jpg" target="_blank"><img src="https://tk2.shuangshuangjieyanw.com:4949/col/{qish}/ampt.jpg" / ></div><div align="center"><iframe src="https://zhibo.chong0123.com:777/" height="150" width=100% title="香港开奖"></iframe></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/n1.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/n1.jpg" /></div><div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic0.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic0.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic1.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic1.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b002.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b002.jpg" / ><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b004.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b004.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b006.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b006.jpg" / ><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b008.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b008.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/j11.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/j11.jpg" / ><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/qlb.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/qlb.jpg" / ></div></body></html>
"""     
        temp1 = """
<h1 align="center" style="color:red ; font-size:50px">香港图片</h1><iframe src="https://zhibo.chong0123.com:777/" height="150" width=100% title="香港开奖"></iframe></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/n1.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/n1.jpg" /></div><div align="center" class="imgblock"><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic0.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic0.jpg" / ><a href="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic1.jpg" target="_blank"><img src="https://gh-proxy.com/https://raw.githubusercontent.com/Rokate/imagebackup/main/Script/Src/xgpic1.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b002.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b002.jpg" / ><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b004.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b004.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b006.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b006.jpg" / ><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b008.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/b008.jpg" / ></div><div align="center" class="imgblock"><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/j11.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/j11.jpg" / ><a href="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/qlb.jpg" target="_blank"><img src="https://tk.shuangshuangjieyanw.com:4949/col/{qs}/qlb.jpg" / ></div></body></html>
"""
        tempp='<!DOCTYPE html><html><head><meta charset="utf-8"><title>澳门图片</title></head><body><style type="text/css">.imgblock img{width:50%;height:500px;flost:left;}</style>'
        text=temp.format(qish=qish,qs=qs)
        text1=temp1.format(qs=qs)
        with open("./Script/Src/html.txt", "w") as f:
            f.write(tempp+text)
        with open("./Script/Src/xgt.txt", "w") as f:
            f.write(tempp+text1)
