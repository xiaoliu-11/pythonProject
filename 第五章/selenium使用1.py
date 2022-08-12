from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#1.创建浏览器对象

web= Chrome()
#2.打开一个网址
web.get("https://www.huya.com/")
el = web.find_element(By.XPATH,'//*[@id="player-brower-pause-guide"]/div[2]/div[2]/p')
el.click() #点击事件

time.sleep(1)

#找到输入框 send_keys输入内容
input_text = web.find_element(By.XPATH,'//*[@id="search-bar-input"]').send_keys("大司马",Keys.ENTER)
