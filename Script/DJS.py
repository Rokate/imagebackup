import aiohttp
import asyncio

async def download(session, url, sem, i, contentlist):
    async with sem:
        try:
            async with session.get(url) as response:
                data = await response.text()
                contentlist[i] = data
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            
async def MHCZ():
    jscontent = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"><meta name="applicable-device" content="mobile"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>澳门图片</title></head><body><style type="text/css">.box{margin:5px 0;border-radius: 5px;overflow: hidden;background: #FFF;filter: progid:DXImageTransform.Microsoft.gradient(startcolorstr=#99000000, endcolorstr=#99000000);}</style><h1 align="center" style="color:red ; font-size:50px">澳门马会传真</h1>'
    mhczurl = "https://67292c.com"
    mhcz = [
        f"{mhczurl}/bbs/1x1m.js",
        f"{mhczurl}/bbs/czjx.js",
        f"{mhczurl}/bbs/1ax.js",
        f"{mhczurl}/bbs/sqi.js",
        f"{mhczurl}/bbs/ase.js",
        f"{mhczurl}/bbs/daxiba.js",
        f"{mhczurl}/bbs/qisha.js",
        f"{mhczurl}/bbs/lanw.js",
        f"{mhczurl}/bbs/12m.js",
        f"{mhczurl}/bbs/lczjx.js",
        f"{mhczurl}/bbs/cypt.js",
        f"{mhczurl}/bbs/1x.js",
        f"{mhczurl}/bbs/alg.js",
        f"{mhczurl}/bbs/sb.js",
        f"{mhczurl}/bbs/1anv.js",
        f"{mhczurl}/bbs/jy4x.js",
        f"{mhczurl}/bbs/dszt.js",
        f"{mhczurl}/bbs/tian.js",
        f"{mhczurl}/bbs/gjh.js",
        f"{mhczurl}/bbs/3qbc.js",
        f"{mhczurl}/bbs/jy1x.js",
        f"{mhczurl}/bbs/jy2x.js",
        f"{mhczurl}/bbs/5m.js",
        f"{mhczurl}/bbs/liuao.js",
        f"{mhczurl}/bbs/gs.js",
        f"{mhczurl}/bbs/hong.js",
        f"{mhczurl}/bbs/xx1.js",
        f"{mhczurl}/bbs/xx2.js",
        f"{mhczurl}/bbs/2x.js",
        f"{mhczurl}/bbs/no.js",
        f"{mhczurl}/bbs/dshuang.js",
        f"{mhczurl}/bbs/xiang.js",
        f"{mhczurl}/bbs/ng.js",
        f"{mhczurl}/bbs/bawei.js",
        f"{mhczurl}/bbs/sanhang.js",
        f"{mhczurl}/bbs/shy.js",
        f"{mhczurl}/bbs/10x.js",
        f"{mhczurl}/bbs/hct.js",
        f"{mhczurl}/bbs/2xzt.js",
        f"{mhczurl}/bbs/gjpjm.js",
        f"{mhczurl}/bbs/4x.js",
        f"{mhczurl}/bbs/sob.js",
        f"{mhczurl}/bbs/sofb.js",
        f"{mhczurl}/bbs/yuan.js",
        f"{mhczurl}/bbs/sha.js",
    ]
    contentlist = [
        "1x1m.js",
        "czjx.js",
        "1ax.js",
        "sqi.js",
        "ase.js",
        "daxiba.js",
        "qisha.js",
        "lanw.js",
        "12m.js",
        "lczjx.js",
        "cypt.js",
        "1x.js",
        "alg.js",
        "sb.js",
        "1anv.js",
        "jy4x.js",
        "dszt.js",
        "tian.js",
        "gjh.js",
        "3qbc.js",
        "jy1x.js",
        "jy2x.js",
        "5m.js",
        "liuao.js",
        "gs.js",
        "hong.js",
        "xx1.js",
        "xx2.js",
        "2x.js",
        "no.js",
        "dshuang.js",
        "xiang.js",
        "ng.js",
        "bawei.js",
        "sanhang.js",
        "shy.js",
        "10x.js",
        "hct.js",
        "2xzt.js",
        "gjpjm.js",
        "4x.js",
        "sob.js",
        "sofb.js",
        "yuan.js",
        "sha.js",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = []
        sem = asyncio.Semaphore(6)
        for i in range(len(mhcz)):
            task = asyncio.create_task(download(session, mhcz[i], sem, i, contentlist))
            tasks.append(task)
        await asyncio.gather(*tasks)
    for content in contentlist:
        jscontent = (
            jscontent
            + f'<div class="box"><script type="text/javascript">{content}</script>'
        )
    with open("./Script/Src/mhcz.txt", "w") as f:
        f.write(jscontent + "</body></html>")


if __name__ == "__main__":
    print("jsfile下载。。")
    asyncio.run(MHCZ())
    
    
