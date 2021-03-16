import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import sys

# 配置抢购时间
set_time = datetime.datetime(2021,3,15,21,50)

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://www.taobao.com")
driver.find_element_by_link_text("亲，请登录").click()
time.sleep(1)
WebDriverWait(driver, 60).until(lambda x:not x.find_elements("id","login"))
print('登陆完成')

# 检查时间
while(1):
    now = datetime.datetime.now()
    if now > set_time:
        break

driver.get("https://cart.taobao.com/cart.htm")
driver.find_element_by_id("J_SelectAll1").click()

WebDriverWait(driver, 10).until(lambda x:x.find_element_by_link_text('结 算'))
WebDriverWait(driver, 10).until(lambda x:'disabled' not in x.find_element_by_link_text('结 算').get_attribute('class'))
driver.find_element_by_link_text("结 算").click()

WebDriverWait(driver, 10).until(lambda x:x.find_element_by_link_text('提交订单'))
driver.find_element_by_link_text("提交订单").click()