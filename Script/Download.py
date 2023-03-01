import requests
import traceback

try:
    respic = requests.get('https://4915552c.com/unite49/h5/picture/detail/latest?pictureTypeId=1087055').json()['data']['largePictureUrl']

except Exception as e:
    print('出错了',traceback.format_exc())
else:
    print(respic)
