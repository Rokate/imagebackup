import aiohttp
import asyncio
import aiofiles
import codecs
import os
from urllib.parse import unquote


async def download(session, url, sem, i, contentlist):
    async with sem:
        try:
            async with session.get(url) as response:
                data = await response.read()
                try:
                    text = data.decode('utf-8')
                except UnicodeDecodeError as e:
                    text = codecs.decode(data, 'utf-8', 'ignore')
                contentlist[i] = text
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            
async def dlxjw(session, url, sem, filepath):
    async with sem:
        try:
            async with session.get(url) as response:        
              async with aiofiles.open(filepath, "wb") as f:
                data = await response.read()
                await f.write(data)
        except Exception as e:
            print(f"Failed to download {url}: {e}")          
#获取dihzi url+/yjjy/wenzhang.js
async def MHCZ():
    print("mhcz下载。。。")
    mhczurl = "https://67292c.com"
    jscontent = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"><meta name="applicable-device" content="mobile"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>澳门图片</title></head><body><style type="text/css">.box{margin:5px 0;border-radius: 5px;overflow: hidden;background: #FFF;filter: progid:DXImageTransform.Microsoft.gradient(startcolorstr=#99000000, endcolorstr=#99000000);}</style><h1 align="center" style="color:red ; font-size:50px">'
        + f'<a href="{mhczurl}">澳门马会传真</a></h1>'
    )
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
        f"{mhczurl}/bbs/xiao.js",
        f"{mhczurl}/bbs/1x.js",
        f"{mhczurl}/bbs/3x.js",
        f"{mhczurl}/bbs/alg.js",
        f"{mhczurl}/bbs/sb.js",
        f"{mhczurl}/bbs/1anv.js",
        f"{mhczurl}/bbs/jy3x.js",
        f"{mhczurl}/bbs/jy4x.js",
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
    async with aiohttp.ClientSession() as session:
        tasks = []
        sem = asyncio.Semaphore(10)
        for i in range(len(mhcz)):
            task = asyncio.create_task(download(session, mhcz[i], sem, i, mhcz))
            tasks.append(task)
        await asyncio.gather(*tasks)
    for content in mhcz:
        jscontent = (
            jscontent
            + f'<div class="box"><script type="text/javascript">{content}</script></div>'
        )
    with open("./Script/Src/mhcz.txt", "w") as f:
        f.write(jscontent + "</body></html>")


async def XJW():
    print("xjw下载。。。")
    xjwurl = "https://868680.com"
    jscontent = (
        '<!DOCTYPE html><html><head><META NAME="ROBOTS" CONTENT="INDEX,NOFOLLOW"><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" /><meta name="applicable-device" content="mobile" /><meta name="apple-mobile-web-app-capable" content="yes" /><meta name="apple-mobile-web-app-status-bar-style" content="black" /><meta content="telephone=no" name="format-detection" /><title>澳门图片</title></head><body><style type="text/css">.box{margin-top:0px;padding: 0px;border: solid 0px #949494;border-radius: 1px;background: #fff;box-shadow: 0 2px 5px rgba(0,0,0,0.1);}</style><h1 align="center" style="color:red ; font-size:50px">'
        + f'<a href="{xjwurl}/868679.html">澳门玄机网</a></h1>'
    )
    xjw = [
        f"{xjwurl}/chajian/%E4%B8%89%E8%82%96%E4%B8%89%E7%A0%81.js",
        f"{xjwurl}/chajian/%E9%A1%B6%E9%83%A8%E5%85%AD%E8%82%96.js",
        f"{xjwurl}/chajian/td6m.js",
        f"{xjwurl}/chajian/zhsl.js",
        f"{xjwurl}/chajian/16%E7%A0%81%E4%B8%AD%E7%89%B9.js",
        f"{xjwurl}/chajian/%E5%B9%B3%E7%89%B9%E4%B8%80%E8%82%96.js",
        f"{xjwurl}/chajian/3q4x8m.js",
        f"{xjwurl}/chajian/7x14m.js",
        f"{xjwurl}/chajian/wh1b.js",
        f"{xjwurl}/chajian/%E5%9B%9B%E8%82%96%E4%B8%AD%E7%89%B9.js",
        f"{xjwurl}/chajian/xj18m.js",
        f"{xjwurl}/chajian/3wzt.js",
        f"{xjwurl}/chajian/%E6%9D%80%E4%B8%A4%E8%82%96%E5%9B%BE.js",
        f"{xjwurl}/chajian/%E7%BB%BC%E5%90%88%E7%89%B9%E7%A0%81.js",
        f"{xjwurl}/chajian/%E5%9B%9B%E7%BB%84%E4%BA%94%E4%B8%8D%E4%B8%AD.js",
        f"{xjwurl}/chajian/6x6m.js",
        f"{xjwurl}/chajian/dx8m.js",
        f"{xjwurl}/chajian/%E5%8D%95%E5%8F%8C%E4%B8%AD%E7%89%B9.js",
        f"{xjwurl}/chajian/%E9%98%B4%E9%98%B312%E7%A0%81.js",
        f"{xjwurl}/chajian/pt2m.js",
        f"{xjwurl}/chajian/%E4%B8%80%E6%B3%A2%E5%8D%8A%E6%B3%A2.js",
        f"{xjwurl}/chajian/2qpt.js",
        f"{xjwurl}/chajian/%E4%BA%94%E5%AD%97%E7%9C%9F%E8%A8%80.js",
        f"{xjwurl}/chajian/1x1m.js",
        f"{xjwurl}/chajian/%E6%AC%B2%E9%92%B1%E6%96%99.js",
        f"{xjwurl}/chajian/%E7%A5%9E%E5%A5%87%E5%9B%9B%E5%AD%97.js",
        f"{xjwurl}/chajian/%E4%B8%80%E5%AD%97%E8%A7%A3%E7%89%B9%E7%A0%81.js",
        f"{xjwurl}/chajian/%E5%85%AD%E8%82%96.js",
        f"{xjwurl}/chajian/%E4%BA%8C%E5%AD%97%E7%BB%8F.js",
        f"{xjwurl}/chajian/%E7%90%B4%E6%A3%8B%E4%B9%A6%E7%94%BB.js",
		f"{xjwurl}/chajian/%E6%B3%A2%E8%89%B2.js",
		f"{xjwurl}/chajian/%E4%B8%80%E7%82%B9%E9%80%9A%E7%8E%84%E6%9C%BA.js",
		f"{xjwurl}/chajian/%E4%B8%89%E5%A4%B4%E4%B8%AD%E7%89%B9.js",
		f"{xjwurl}/chajian/%E5%B9%B3%E7%89%B9%E8%BF%9E%E5%B0%BE.js",
		f"{xjwurl}/chajian/%E5%AE%B6%E9%87%8E.js",
		f"{xjwurl}/chajian/%E6%98%A5%E5%A4%8F%E7%A7%8B%E5%86%AC.js",
		f"{xjwurl}/chajian/%E7%AE%A1%E5%AE%B6%E5%A9%86%E8%A7%A3%E6%9E%90.js",
		f"{xjwurl}/chajian/%E4%B8%83%E5%B0%BE.js",
		f"{xjwurl}/chajian/%E6%9D%80%E4%B8%89%E8%82%96.js",
		f"{xjwurl}/chajian/%E5%B9%B3%E5%B0%BE.js",
		f"{xjwurl}/chajian/%E7%8C%9C%E7%89%B9%E8%BE%93%E5%B0%BD%E5%85%89.js",
		f"{xjwurl}/chajian/36%E7%A0%81.js",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = []
        sem = asyncio.Semaphore(10)
        for url in xjw:
            filename = unquote(os.path.basename(url), 'utf-8')
            jscontent = (
            jscontent
            + f'<div class="box"><h1 align="center" style="color:red ; font-size:25px">---------分割线---------</h1><script type="text/javascript" src="https://gcore.jsdelivr.net/gh/Rokate/imagebackup@main/Script/Src/xjw/{filename}"  charset="gb2312"></script></div>'
        )
            filepath = "./Script/Src/xjw/" + filename
            task = asyncio.create_task(dlxjw(session, url, sem, filepath))
            tasks.append(task)
        await asyncio.gather(*tasks)
        with open("./Script/Src/xjw.txt", "w") as f:
            f.write(jscontent + "</body></html>")
   


async def MRY():
    print("mry下载。。。")
    mryurl = "https://138383b.com"  
    #26572.com
    jscontent = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta name="applicable-device" content="mobile"><meta name="apple-itunes-app" content="app-id=529696004"><meta name="viewport" content="width=device-width,initial-scale=1, maximum-scale=1, user-scalable=no"><meta name="apple-mobile-web-app-capable" content="yes"><title>澳门图片</title></head><body><style type="text/css">.white-box { margin-top: 10px; padding: 5px; border: solid 1px #ddd; border-radius: 5px; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}</style><h1 align="center" style="color:red ; font-size:50px">'
        + f'<a href="{mryurl}/26572.html">澳门美人鱼论坛</a></h1>'
    )
    mry = [
        f"{mryurl}/dbu.js",
        f"{mryurl}/cj13.js",
        f"{mryurl}/cj10.js",
        f"{mryurl}/cj07.js",
        f"{mryurl}/cj06.js",
        f"{mryurl}/cj20.js",
        f"{mryurl}/cj08.js",
        f"{mryurl}/ptxj.js",
        f"{mryurl}/cj09.js",
        f"{mryurl}/cj05.js",
        f"{mryurl}/mhcz.js",
        f"{mryurl}/cj02.js",
        f"{mryurl}/cj03.js",
        f"{mryurl}/ampm.js",
        f"{mryurl}/cj16.js",
        f"{mryurl}/cj18.js",
        f"{mryurl}/cj01.js",
        f"{mryurl}/cj21.js",
        f"{mryurl}/cj17.js",
        f"{mryurl}/cj23.js",
        f"{mryurl}/cj24.js",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = []
        sem = asyncio.Semaphore(10)
        for i in range(len(mry)):
            task = asyncio.create_task(download(session, mry[i], sem, i, mry))
            tasks.append(task)
        await asyncio.gather(*tasks)
    for content in mry:
        jscontent = (
            jscontent
            + f'<div class="box"><h1 align="center" style="color:red ; font-size:25px">---------分割线---------</h1><script type="text/javascript" charset="utf-8">{content}</script></div>'
        )
    with open("./Script/Src/mry.txt", "w") as f:
        f.write(jscontent + "</body></html>")


async def ZLW():
    print("zlw下载。。。")
    zlwurl = "https://49629.com"
    jscontent = (
        '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"><meta name="applicable-device" content="mobile"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>澳门图片</title></head><body><style type="text/css">.white-box { margin-top: 10px; padding: 5px; border: solid 1px #ddd; border-radius: 5px; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}</style><h1 align="center" style="color:red ; font-size:50px">'
        + f'<a href="{zlwurl}/62.html">最全资料网</a></h1>'
    )
    zlw = [
        f"{zlwurl}/bbs/yy4wzt.js",
        f"{zlwurl}/bbs/yydx1t.js",
        f"{zlwurl}/bbs/yyjy2x.js",
        f"{zlwurl}/bbs/1w1mz.js",
        f"{zlwurl}/bbs/yyds2x.js",
    ]
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = []
        sem = asyncio.Semaphore(2)
        for i in range(len(zlw)):
            task = asyncio.create_task(download(session, zlw[i], sem, i, zlw))
            tasks.append(task)
        await asyncio.gather(*tasks)
    for content in zlw:
        jscontent = (
            jscontent
            + f'<div style="margin:0px;"><script type="text/javascript" charset="utf-8">{content}</script></div>'
        )
    with open("./Script/Src/zlw.txt", "w") as f:
        f.write(jscontent + "</body></html>")


async def LFW():
    print("lfw下载。。。")
    lfwurl = "https://29761b.com"
    jscontent = (
        '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"><meta name="applicable-device" content="mobile"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black"><meta http-equiv="X-UA-Compatible" content="ie=edge"><meta content="telephone=no" name="format-detection" /><title>澳门图片</title></head><body><style type="text/css">.white-box { margin-top: 10px; padding: 5px; border: solid 1px #ddd; border-radius: 5px; background: #fff; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}</style><h1 align="center" style="color:red ; font-size:50px">'
        + f'<a href="{lfwurl}/29048.html">雷锋老牌论坛</a></h1>'
    )
    lfw = [
        f"{lfwurl}/bbs/db5x.js",
        f"{lfwurl}/bbs/lf4.js",
        f"{lfwurl}/bbs/mmxj.js",
        f"{lfwurl}/bbs/hz6x.js",
        f"{lfwurl}/bbs/4x4m.js",
        f"{lfwurl}/bbs/gjpjm.js",
        f"{lfwurl}/bbs/jx3xx.js",
        f"{lfwurl}/bbs/ptpt.js",
        f"{lfwurl}/bbs/cbtj.js",
        f"{lfwurl}/bbs/16m.js",
        f"{lfwurl}/bbs/sx.js",
        f"{lfwurl}/bbs/dx.js",
        f"{lfwurl}/bbs/ds.js",
        f"{lfwurl}/bbs/dwxjj.js",
        f"{lfwurl}/bbs/ptrlx.js",
        f"{lfwurl}/bbs/sb12m.js",
        f"{lfwurl}/bbs/sdtj.js",
        f"{lfwurl}/bbs/7z4x.js",
        f"{lfwurl}/bbs/4w8m.js",
        f"{lfwurl}/bbs/ptyx.js",
        f"{lfwurl}/bbs/yjxj.js",
        f"{lfwurl}/bbs/jyjex.js",
        f"{lfwurl}/bbs/ptywsew.js",
        f"{lfwurl}/bbs/jrxqj.js",
        f"{lfwurl}/bbs/stzt.js",
        f"{lfwurl}/bbs/bc9x.js",
        f"{lfwurl}/bbs/td1x.js",
        f"{lfwurl}/bbs/yql.js",
        f"{lfwurl}/bbs/jssw.js",
        f"{lfwurl}/bbs/jxzt.js",
        f"{lfwurl}/bbs/cxqd.js",
        f"{lfwurl}/bbs/qw.js",
        f"{lfwurl}/bbs/shzt.js",
        f"{lfwurl}/bbs/jgsx.js",
        f"{lfwurl}/bbs/ssx.js",
        f"{lfwurl}/bbs/set.js",
        f"{lfwurl}/bbs/sbb.js",
    ]
    conn=aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = []
        sem = asyncio.Semaphore(10)
        for i in range(len(lfw)):
            task = asyncio.create_task(download(session, lfw[i], sem, i, lfw))
            tasks.append(task)
        await asyncio.gather(*tasks)
    for content in lfw:
        jscontent = (
            jscontent
            + f'<div><script type="text/javascript" charset="gb2312">{content}</script></div>'
        )
    with open("./Script/Src/lfw.txt", "w") as f:
        f.write(jscontent + "</body></html>")


if __name__ == "__main__":
    asyncio.run(MHCZ())
    asyncio.run(XJW())
    asyncio.run(MRY())
    asyncio.run(ZLW())
    asyncio.run(LFW())
