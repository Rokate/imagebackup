import requests
import json

LotterytypeList = [1,2,5]
for ltl in LotterytypeList:
    
    url = "https://123tkapi-ali.uvcy88.com/gallerynew/app/lottery/search"
    headers = {
    "Lotterytype": f"{ltl}" #2-la 5-xa 1-xg
    }
    
    params = {
    "pageNum": 1,
    "year": 2025,
    "sort": 1
    }
    response = requests.get(url, headers=headers, params=params).json()
    reslen = response['data']['pager']['totalCount']

    with open(f'./Script/Data/{ltl}-2025results.txt', 'r', encoding='utf-8') as f:
        filedata = json.load(f)
    filelen = len(filedata)

    if reslen > filelen:
        recordList = response['data']['recordList'][0]
        period = recordList['period']
        lotteryTime = recordList['lotteryTime']
        number_List = recordList['numberList']
        
        recordList = {
            "period": period,
            "lotteryTime": lotteryTime,
            "numberList": number_List
            }
        filedata.append(recordList)
        
        result_json = json.dumps(filedata, ensure_ascii=False, indent=4)
        
        print(f"已获取Type：{ltl}")
        
        with open(f"./Script/Data/{ltl}-2025results.txt", "w", encoding="utf-8") as file:
            file.write(result_json)
