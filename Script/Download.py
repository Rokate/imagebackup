import requests

picurl = requests.get('https://49152c.com/unite49/h5/picture/detail/latest?pictureTypeId=10870').json()['data']['largePictureUrl']
pic02 = requests.get(picurl)
if pic02.headers['Content-Type'] == 'image/jpeg':
    print ('图下02')
    with open('./aomen/11111111111.jpg', 'wb') as f:
        f.write(pic02.content)
