import aiohttp
import asyncio
import aiofiles
import time

async def download(session,url,sem):
    async with sem:
        try:
            async with session.get(url) as response:
                data = await response.read()
                filename = './Script/Js/'+url.split('/')[-1]
                async with aiofiles.open(filename, 'wb') as f:
                    await f.write(data)
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

async def main():
    mhczurl = 'https://578866a.com'
    mhcz = [
    f'{mhczurl}/bbs/1x1m.js',
    f'{mhczurl}/bbs/czjx.js',
    f'{mhczurl}/bbs/1ax.js',
    f'{mhczurl}/bbs/sqi.js',
    f'{mhczurl}/bbs/ase.js',
    f'{mhczurl}/bbs/daxiba.js',
    f'{mhczurl}/bbs/qisha.js',
    f'{mhczurl}/bbs/lanw.js',
    f'{mhczurl}/bbs/12m.js',
    f'{mhczurl}/bbs/lczjx.js',
    f'{mhczurl}/bbs/cypt.js',
    f'{mhczurl}/bbs/1x.js',
    f'{mhczurl}/bbs/alg.js',
    f'{mhczurl}/bbs/sb.js',
    f'{mhczurl}/bbs/1anv.js',
    f'{mhczurl}/bbs/jy4x.js',
    f'{mhczurl}/bbs/dszt.js',
    f'{mhczurl}/bbs/tian.js',
    f'{mhczurl}/bbs/gjh.js',
    f'{mhczurl}/bbs/3qbc.js',
    f'{mhczurl}/bbs/jy1x.js',
    f'{mhczurl}/bbs/jy2x.js',
    f'{mhczurl}/bbs/5m.js',
    f'{mhczurl}/bbs/liuao.js',
    f'{mhczurl}/bbs/gs.js',
    f'{mhczurl}/bbs/hong.js',
    f'{mhczurl}/bbs/xx1.js',
    f'{mhczurl}/bbs/xx2.js',
    f'{mhczurl}/bbs/2x.js',
    f'{mhczurl}/bbs/no.js',
    f'{mhczurl}/bbs/dshuang.js',
    f'{mhczurl}/bbs/xiang.js',
    f'{mhczurl}/bbs/ng.js',
    f'{mhczurl}/bbs/bawei.js',
    f'{mhczurl}/bbs/sanhang.js',
    f'{mhczurl}/bbs/shy.js',
    f'{mhczurl}/bbs/10x.js',
    f'{mhczurl}/bbs/hct.js',
    f'{mhczurl}/bbs/2xzt.js',
    f'{mhczurl}/bbs/gjpjm.js',
    f'{mhczurl}/bbs/4x.js',
    f'{mhczurl}/bbs/sob.js',
    f'{mhczurl}/bbs/sofb.js',
    f'{mhczurl}/bbs/yuan.js',
    f'{mhczurl}/bbs/sha.js',]

    async with aiohttp.ClientSession() as session:
        tasks = []
        sem = asyncio.Semaphore(6)
        for url in mhcz:
            task = asyncio.create_task(download(session,url,sem))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'一共耗时：{end - start}')

