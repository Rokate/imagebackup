import requests
import datetime
import json
import os
from huggingface_hub import HfApi

Lotterytype = ['xg','hk6','a6','la','xa','xa6']
LotterytypeList = [1,2,5]
fiveElementsMap = {'j': '金', 'm': '木', 's': '水', 'h': '火', 't': '土'}
colorMap = {'R': 1, 'G': 3, 'B': 2}
oddEvenMap = {'o': '单', 'e': '双'}
sizeMap = {'b': '大', 's': '小'}
Year = 2026

for ltl in LotterytypeList:
    url = f"https://ocs.ai4funs.com/pwtkprd/gr/{Lotterytype[ltl]}/history/{Year}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"请求接口失败（Type={ltl}）: {e}")
        continue

    # 确保接口返回结构存在
    record_list = data.get("data", {})
    if not record_list:
        print(f"未在接口中找到记录（Type={ltl}）")
        continue

    latest = record_list[0]
    period = int(latest.get("shortIssue"))
    lotteryTime = record_raw.get('openTime') // 1000
    openTime = datetime.datetime.fromtimestamp(lotteryTime).strftime('%Y年%m月%d日')
    number_List = record_raw.get('numInfo', [])
    numberList = []
    for i in range(min(7, len(number_List))):
        numberData = {}
        number = number_List[i].get('num', '')
        shengXiao = number_List[i].get('shengxiao', '')
        color = number_List[i].get('color', '')
        wuXing = number_List[i].get('fiveElements', '')
        daXiao = number_List[i].get('size', '')
        danShuang = number_List[i].get('oddEven', '')
       
        numberData = {
            "color": colorMap.get(color, ''),
            "count": 'null',
            "daXiao": sizeMap.get(daXiao, ''),
            "danShuang": oddEvenMap.get(danShuang, ''),
            "number": number,
            "shengXiao": shengXiao,
            "wuXing": fiveElementsMap.get(wuXing, '')
        }
        numberList.append(numberData)
    record = {
        "period": period,
        "lotteryTime": openTime,
        "numberList": numberList,
    }

    local_path = f"{ltl}-{Year}results.txt"

    # 如果本地文件不存在 -> 直接创建并写入处理后的信息（不用对比长度）
    if not os.path.exists(f"./Script/Data/{local_path}"):
        try:
            with open(f"./Script/Data/{local_path}", "w", encoding="utf-8") as f:
                json.dump([record], f, ensure_ascii=False, indent=4)
            print(f"文件不存在，已创建并写入新文件：{local_path}")
        except Exception as e:
            print(f"创建或写入文件失败：{local_path}，错误：{e}")
        continue

    # 如果文件存在则尝试读取并对比，若解析失败则视为空列表并写入
    try:
        with open(f"./Script/Data/{local_path}", "r", encoding="utf-8") as f:
            try:
                filedata = json.load(f)
                if not isinstance(filedata, list):
                    print(f"警告: 本地文件内容不是列表，重置为列表 - {local_path}")
                    filedata = []
            except json.JSONDecodeError:
                print(f"警告: 无法解析 JSON，文件将被重置 - {local_path}")
                filedata = []
    except Exception as e:
        print(f"读取本地文件失败：{local_path}，错误：{e}")
        filedata = []

    # 如果本地没有该记录或长度小于接口返回的数量则追加（保留原有逻辑的兼容）
    appended = False
    if not filedata:
        filedata.append(record)
        appended = True
    else:
        # 如果最新期号不同，则追加
        try:
            existing_periods = [item.get("period") for item in filedata if isinstance(item, dict)]
            if period not in existing_periods:
                filedata.append(record)
                appended = True
        except Exception:
            # 回退到长度比较（以兼容原脚本）
            filelen = len(filedata)
            reslen = data.get("data", {}).get("pager", {}).get("totalCount", 0)
            if reslen > filelen:
                filedata.append(record)
                appended = True

    if appended:
        try:
            with open(f"./Script/Data/{local_path}", "w", encoding="utf-8") as f:
                json.dump(filedata, f, ensure_ascii=False, indent=4)
            print(f"已获取并追加 {Lotterytype[ltl]} 到 {local_path}")
        except Exception as e:
            print(f"写入文件失败：{local_path}，错误：{e}")
    else:
        print(f"无新记录（{Lotterytype[ltl]}），不需要更新本地文件：{local_path}")

# --- 上传到 Hugging Face Space ---
token = os.getenv("HF_TOKEN")
if token is None:
    raise ValueError("请提供 Hugging Face token 或设置 HF_TOKEN 环境变量")

api = HfApi()
local_files = [
    f"./Script/Data/1-{Year}results.txt",
    f"./Script/Data/2-{Year}results.txt",
    f"./Script/Data/5-{Year}results.txt",
]

repo_files = [
    f"data/1-{Year}results.txt",
    f"data/2-{Year}results.txt",
    f"data/5-{Year}results.txt",
]

for file_path, repo_path in zip(local_files, repo_files):
    try:
        # 检查本地文件是否存在
        if not os.path.exists(file_path):
            print(f"警告: 文件不存在 - {file_path}")
            continue

        print(f"正在上传 {file_path} 到 {repo_path}...")
        api.upload_file(
            path_or_fileobj=file_path,
            path_in_repo=repo_path,
            repo_id="Keron/xamdata",
            repo_type="space",
            token=token,
        )
        print(f"成功上传 {file_path}")

    except Exception as e:
        print(f"上传 {file_path} 时发生错误: {str(e)}")
