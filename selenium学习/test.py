from selenium import webdriver
# 启动浏览器
wd = webdriver.Chrome(r'D:\chromedriver.exe')
# 打开百度网址
wd.get('https://www.baidu.com')
print(wd.title)
 # wd.quit()

# 用程序来控制浏览器

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element_by_id('kw')
# 通过该WebElement对象，就可以对页面元素进行操作了
# 输入字符串到这个输入框中
element.send_keys('网页')
wd.find_element_by_id('su').click()

# 根据元素的class属性选择元素



