import requests
import shutil,os
from datetime import datetime

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
currentDir = os.getcwd()
path = os.path.join(currentDir,'Images')#saving images to Images folder

def Image(url):
    attempts = 0
    while attempts < 5:#retry 5 times
        try:
            filename = url.split('/')[-1]
            r = requests.get(url,headers=headers,stream=True,timeout=5)
            if r.status_code == 200:
                with open(os.path.join(path,filename),'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw,f)
            print(filename)
            break
        except Exception as e:
            attempts+=1
            print(e)

if __name__ == '__main__':
    i = [1,2,3,4,5,6,7,8,9,10]
    #print(datetime.now().year)
    now=datetime.today().strftime('%Y-%m-%d')
    yr,mo,dt=now.split("-")
    for val in i:
        url = "http://epaperlokmat.in/eNewspaper/News/LOK/NPLK/"+yr+"/"+mo+"/"+dt+"/"+yr+mo+dt+"_"+str(val)+".jpg"
        #print (url)
        Image(url)
