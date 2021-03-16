import time
from selenium import webdriver
import datetime
import sys
from selenium.webdriver.common.keys import Keys

# 89.0.4389.82


class Spider:
    def __init__(self, url):
        self.__base_url = url
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
    def get_url(self):
        global driver
        driver.get(self.__base_url)
    def login(self):
        global driver
        if driver.find_element_by_link_text("亲，请登录"):
            driver.find_element_by_link_text("亲，请登录").click()
            print("请在30秒内扫描登陆")
            time.sleep(10)
            # driver.get("https://cart.taobao.com/cart.htm")
    def selectAll(self,method):
        global driver
        # 打开购物车列表页面
        driver.get("https://cart.taobao.com/cart.htm")
        time.sleep(3)

        # 是否全选购物车
        if method == 0:
            while True:
                try:
                    if driver.find_element_by_id("J_SelectAll1"):
                        driver.find_element_by_id("J_SelectAll1").click()
                        break
                except:
                    print(f"找不到购买按钮")
                    
                    pass
        if method ==1 :
            print(f"请手动勾选需要购买的商品")
            time.sleep(30)

    def buy(self,times):
        global driver
        driver.get("https://cart.taobao.com/cart.htm")
        driver.find_element_by_id("J_SelectAll1").click()
        driver.find_element_by_link_text("结 算").click()

        while True:
            now = datetime.datetime.now()
            # 对比时间，时间到的话就点击结算
            if now > times:
                print(f"抢购时间已到！！！")
                # 点击结算按钮
                while True:
                    print('111')
                    try:
                        print('112')
                        # print(f'进入结算循环',driver.find_element_by_link_text('提交订单').disabled)
                        jiesuan = driver.find_element_by_link_text("结 算")
                        if jiesuan:

                            # driver.find_element_by_link_text("结 算").send_keys(Keys.ENTER)
                            jiesuan.click()
                            print(f"结算成功，准备提交订单")
                            break
                    except:
                        pass
                print('222')
                # 点击提交订单按钮
                while True:
                    try:

                        if driver.find_element_by_link_text('提交订单'):
                            driver.find_element_by_link_text('提交订单').click()
                            print(f"抢购成功，请尽快付款")
                    except:
                        # print(f"再次尝试提交订单")
                        print(f"提交订单失败")
                        pass
                print('333')
                time.sleep(0.01)


option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
spider = Spider("https://www.taobao.com")
spider.get_url()
spider.login()
#设置0为全选、1为手动
# spider.selectAll(0)

print(f"等待页面交互，即结算按钮可点击...")
# time.sleep(2)
# 设置抢购时间
set_time = datetime.datetime(2021,3,15,21,50)
spider.buy(set_time)