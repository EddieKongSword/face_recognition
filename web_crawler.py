import urllib
from bs4 import BeautifulSoup

urlName='https://nba.hupu.com/'
page=urllib.urlopen(urlName)
html=page.read()
soup=BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
images=soup.find_all('img')
imageName=0
page.close()
print('--------------pictures number:    '+str(len(images))+'--------------')
print('\n')
for image in images:
    link =  image.get('src')
    fileFormat=link[-4:]
    head=link[:4]
    if head != 'http':
        link='https:'+link
    if  fileFormat == '.jpg' or fileFormat=='jpeg':
        print(link)
        savePath='C:\Users\Eddie\PycharmProjects/face_recognition\pictures/'+str(imageName)+'.jpg'
        imageName+=1
        urllib.urlretrieve(url=link, filename=savePath)





