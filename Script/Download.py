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


async def main(a, b, c, d):
    qishu = a
    qish = b
    qs = c
    urld = d
    urls = [
        ["https://www.353583.com/tutu/faf.jpg", "a-faf.jpg"],
        ["https://www.353583.com/tutu/fgmc.jpg", "a-fgmc.jpg"],
        ["https://www.353583.com/tutu/6i12m.jpg", "a-6i12m.jpg"],
        ["https://www.353583.com/tutu/gd.jpg", "a-gd.jpg"],
        ["https://www.353583.com/tutu/lhwt.jpg", "a-lhwt.jpg"],
        ["https://www.353583.com/tutu/ugyf.jpg", "a-ugyf.jpg"],
        [f"https://69760b.com/img/amhg{qishu}.jpg", "a-amhg.jpg"],
        [f"https://69760b.com/img/jrqy{qishu}.jpg", "a-jrqy.jpg"],
        [f"https://69760b.com/img/nm4x8m{qishu}.jpg", "a-nm4x8m.jpg"],
        [f"http://123186a.com/gsbtu/baoma{qishu}.jpg", "a-baoma.jpg"],
        [f"http://123186a.com/gsbtu/hdjr{qishu}.jpg", "a-hdjr.jpg"],
        [f"https://69760b.com/img/jl3x{qishu}.jpg", "a-jl3x.jpg"],
        ["https://www.353583.com/tutu/ujcc.jpg", "a-ujcc.jpg"],
        [f"https://www.29761b.com/img/djpt{qishu}.jpg", "a-djpt.jpg"],
        [f"https://69760b.com/img/1xzt{qishu}.jpg", "a-1xzt.jpg"],
        [f"https://tk2.{urld}/col/{qish}/amsgyy.jpg", "a-amsgyy.jpg"],
        [f"https://tk2.{urld}/col/{qish}/zbxyb.jpg", "a-zbxyb.jpg"],
        [f"https://tk2.{urld}/col/{qish}/n1.jpg", "a-n1.jpg"],
        [f"https://tk2.{urld}/col/{qish}/dcxj.jpg", "a-dcxj.jpg"],
        [f"https://tk2.{urld}/col/{qish}/ampm.jpg", "a-ampm.jpg"],
        [f"https://tk2.{urld}/col/{qish}/sszm.jpg", "a-sszm.jpg"],
        [f"https://tk2.{urld}/col/{qish}/ktzsx.jpg", "a-ktzsx.jpg"],
        [f"https://tk2.{urld}/col/{qish}/rv.jpg", "a-rv.jpg"],
        [f"https://tk2.{urld}/col/{qish}/tt38.jpg", "a-tt38.jpg"],
        [f"https://tk2.{urld}/col/{qish}/amffh.jpg", "a-amffh.jpg"],
        [f"https://tk2.{urld}/col/{qish}/amfql.jpg", "a-amfql.jpg"],
        [f"https://tk2.{urld}/col/{qish}/twqp.jpg", "a-twqp.jpg"],
        [f"https://tk2.{urld}/col/{qish}/mfpy.jpg", "a-mfpy.jpg"],
        [f"https://tk2.{urld}/col/{qish}/lhlxsm.jpg", "a-lhlxsm.jpg"],
        [f"https://tk2.{urld}/col/{qish}/b8.jpg", "a-b8.jpg"],
        [f"https://tk2.{urld}/col/{qish}/tjn.jpg", "a-tjn.jpg"],
        [f"https://tk2.{urld}/col/{qish}/ampt.jpg", "a-ampt.jpg"],
        [f"https://tk2.{urld}/col/{qish}/lmkz.jpg", "a-lmkz.jpg"],
        ["https://67292b.com/tu/f011.jpg", "a-f011.jpg"],
        [f"https://tk.{urld}/col/{qs}/n1.jpg", "x-n1.jpg"],
        [f"https://tk.{urld}/col/{qs}/b002.jpg", "x-b002.jpg"],
        [f"https://tk.{urld}/col/{qs}/b004.jpg", "x-b004.jpg"],
        [f"https://tk.{urld}/col/{qs}/b006.jpg", "x-b006.jpg"],
        [f"https://tk.{urld}/col/{qs}/b008.jpg", "x-b008.jpg"],
        [f"https://tk.{urld}/col/{qs}/j11.jpg", "x-j11.jpg"],
        [f"https://tk.{urld}/col/{qs}/qlb.jpg", "x-qlb.jpg"],

    ]
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = []
        for i, url in enumerate(urls):
            filename = "./Script/Src/" + url[1]
            task = asyncio.create_task(download_image(session, url[0], filename))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    #a6.003123.club
    try:
        #amcode = {"code": "71"} site:lh49.app
        #https://am49.app/forum/master/list?postCategory=71
        info = requests.get('https://h5.118z2.com:8443/tk118/h5/picture/detail/latest?pictureTypeId=28854').json()
        #qish = requests.post('https://am49.app/open/latest/single?code=71').json()['data']['nextIssueNo'][-3:]
        qish = info['data']['period']
        qishu = '00'+ str(qish)
        #qishu = qish.lstrip('0')
        #Lday = requests.get('https://49252a.com/unite49/h5/index/lotteryTime')
        #qishu = Lday.json()['data']['list'][0]['isLotteryDay'] + 1
        #qish = str(qishu).zfill(3)
        #118tk.com https://118z1.com/#/ https://49tkapp.com/
        #url = requests.get('https://49252a.com/unite49/h5/picture/detail/latest?pictureTypeId=28854').json()['data']['largePictureUrl']
        url = info['data']['largePictureUrl']
        pattern = re.compile("https://tk2.(.*?)/")
        match = re.findall(pattern, url)
        domain_port = match[0]
        
        #xgcode = {"code": "28"} https://am49.app/forum/master/list?postCategory=28
        #qs = requests.post('https://am49.app/open/latest?code=28').json()['data']['nextIssueNo'][-3:].lstrip('0')
        qs = requests.get('https://h5.118z2.com:8443/tk118/h5/picture/detail/latest?pictureTypeId=10870').json()['data']['period']
        
    except Exception as e:
        print("日期更新出错了", traceback.format_exc())
    else:
        print("图片列表下载。。。")
        asyncio.run(main(qish, qishu, qs, domain_port))
        
