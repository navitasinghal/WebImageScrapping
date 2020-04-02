from selenium import webdriver
import os
import urllib.request
import requests
import shutil
searchterms= ['Food'] 
for searchterm in searchterms:
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    browser = webdriver.Chrome(os.getcwd() + "/chromedriver")
    browser.get(url)
    header="Chrome/80.0.3987.149"
    img_count = 0
    extensions = { "jpg", "jpeg", "png"}
    if not os.path.exists(searchterm):
        os.mkdir(searchterm)
    for _ in range(1000):
        browser.execute_script("window.scrollBy(0,10000)")
    html = browser.page_source.split('["')
    k = 1
    imges = []
    for i in browser.page_source.split('["'):   
        if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
            imges.append(i.split('"')[0])
   
    print(len(imges), len(set(imges)) )       
    # for j in imges:
    #     r = requests.get(j,stream=True, headers={'User-agent': 'Chrome/80.0.3987.149'})
    #     if r.status_code == 200:
    #         with open("Food/food{}.jpg".format(k), 'wb') as f:
    #             r.raw.decode_content = True
    #             shutil.copyfileobj(r.raw, f)
    #             k+=1
                
    # print(k)
browser.close()