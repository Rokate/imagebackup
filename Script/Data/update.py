import requests
import json
import os
from huggingface_hub import HfApi

LotterytypeList = [1, 2, 5]
for ltl in LotterytypeList:

    url = "https://123tkapi-ali.uvcy88.com/gallerynew/app/lottery/search"
    headers = {"Lotterytype": f"{ltl}"}  # 2-la 5-xa 1-xg

    params = {"pageNum": 1, "year": 2025, "sort": 1}
    response = requests.get(url, headers=headers, params=params).json()
    reslen = response["data"]["pager"]["totalCount"]

    with open(f"./Script/Data/{ltl}-2025results.txt", "r", encoding="utf-8") as f:
        filedata = json.load(f)
    filelen = len(filedata)

    if reslen > filelen:
        recordList = response["data"]["recordList"][0]
        period = recordList["period"]
        lotteryTime = recordList["lotteryTime"]
        number_List = recordList["numberList"]

        recordList = {
            "period": period,
            "lotteryTime": lotteryTime,
            "numberList": number_List,
        }
        filedata.append(recordList)

        result_json = json.dumps(filedata, ensure_ascii=False, indent=4)

        print(f"已获取Type：{ltl}")

        with open(
            f"./Script/Data/{ltl}-2025results.txt", "w", encoding="utf-8"
        ) as file:
            file.write(result_json)


token = os.getenv("HF_TOKEN")
if token is None:
    raise ValueError("请提供 Hugging Face token 或设置 HF_TOKEN 环境变量")
api = HfApi()
local_files = [
    "./Script/Data/1-2025results.txt",
    "./Script/Data/2-2025results.txt",
    "./Script/Data/5-2025results.txt",
]

repo_files = [
    "data/1-2025results.txt",
    "data/2-2025results.txt",
    "data/5-2025results.txt",
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
