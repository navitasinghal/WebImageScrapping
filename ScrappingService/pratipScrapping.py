from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib.request 
import argparse
# searchterms = ["fall armyworm maize", "downymildew maize", "maize stem borer", "maize pink borer", "maize shoot fly", "maydays leaf blight maize","common rust maize","gray leaf spot maize","northern leaf blight maize","healthy leaf maize"] # will also be the name of the folder
searchterms = ["food"]
for searchterm in searchterms:
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    # NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
    browser = webdriver.Chrome(os.getcwd() + "/chromedriver")
    browser.get(url)
    header="Chrome/80.0.3987.149"
    counter = 0
    succounter = 0
    print("hello pratip")
    if not os.path.exists(searchterm):
        print("this " ,searchterm)
        os.mkdir(searchterm)     
    for _ in range(100):
        browser.execute_script("window.scrollBy(0,1000)")
    for x in browser.find_elements_by_xpath('//div[contains(@class,"islir")]'):
        print("Pratip the Jessie", x)
        counter = counter + 1
        print("Total Count:", counter)
        print("Succsessful Count:", succounter)
       # print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
        img = json.loads(x.get_attribute('innerHTML'))["ou"]
        imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
        try:
            req = urllib.request.Request(img, headers={'User-Agent': header})
            raw_img = urllib.request.urlopen(req).read()
            File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
            File.write(raw_img)
            File.close()
            succounter = succounter + 1
        except Exception as e:
            print(e)
    print (succounter, "pictures succesfully downloaded")
browser.close()

