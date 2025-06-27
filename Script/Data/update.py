import requests
import json
import time

LotterytypeList = [1,2,5]
for ltl in LotterytypeList:
    # 定义请求的 URL 和请求头
    url = "https://123tkapi-ali.uvcy88.com/gallerynew/app/lottery/search"
    headers = {
    "Lotterytype": f"{ltl}" #2-la 5-xa 1-xg
    }
    
    # 初始化结果列表
    result_list = []

    # 首先获取第一页以确定总页数
    params = {
    "pageNum": 1,
    "year": 2025,
    "sort": 0
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # 提取总页数
    total_page_count = data['data']['pager']['totalPageCount']

    # 循环获取每一页的数据
    for page in range(1, total_page_count + 1):
        params['pageNum'] = page
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        time.sleep(2)
        # 提取记录列表
        record_list = data['data']['recordList']
    
        # 处理每一条记录
        for record in record_list:
            period = record['period']
            lottery_time = record['lotteryTime']
            number_list = record['numberList']
        
            # 将 lotteryTime 和 numberList 拼接成一个字典
            result = {
            "period": period,
            "lotteryTime": lottery_time,
            "numberList": number_list
            }
        
            # 添加到结果列表
            result_list.append(result)
    # 整合数组结果
    resultlist = []
    for i in result_list:
      result = []
      result = [item["number"] for item in i["numberList"]]
      resultlist.append(result)
    with open(f"./Script/Data/{ltl}-2025resultlist.txt", "w", encoding="utf-8") as file:
        file.write(resultlist)
    # 将结果转换为 JSON 格式
    result_json = json.dumps(result_list, ensure_ascii=False, indent=4)

    # 打印结果的数量和第一个元素
    print(f"已获取Type：{ltl}")
    
    # 将结果保存到一个文本文件中
    with open(f"./Script/Data/{ltl}-2025results.txt", "w", encoding="utf-8") as file:
        file.write(result_json)
