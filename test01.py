import wget
import urllib.request
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\\Users\\user\Documents\Develops\\chromedriver.exe")    # current path: open_folder(test)
print(type(driver), driver)

url='https://www.coupang.com/np/search?q=컴퓨터'

# res = requests.get(url)
# print(res.status_code, res.content)
# As HTTP 200

driver.get(url=url)
print(type(driver.page_source), driver.page_source)

elements = driver.find_elements(By.XPATH, '//img[@class="search-product-wrap-img"]')
down_path = './test/pictures/'

for element in elements:
    src = element.get_attribute('src')  # download the image
    img_txt = src.split('/')[-1]
    image_name = down_path + img_txt

    ## first way
    # wget.download(url=src, out=image_name)
    ## HTTP Error 403: Forbidden

    ## second way
    ## Download the file from 'url' and save it locally under 'file_name':
    with urllib.request.urlopen(src) as response, open(image_name, 'wb') as out_file:
        data = response.read()   # a 'bytes' object
        out_file.write(data)