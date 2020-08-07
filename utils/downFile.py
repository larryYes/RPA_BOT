import urllib
from time import sleep
from selenium import webdriver


# 下载网页内的文档
def down(url, username=None, password=None):
    browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    browser.get(url)

    # 登陆
    browser.find_element_by_xpath("/html/body/form/center/table/tbody/tr[1]/td/input").send_keys(username)
    browser.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td/input").send_keys(password)
    browser.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[2]/input").click()

    # 匹配所有包括invoice名字的链接
    episodes = browser.find_elements_by_partial_link_text("invoice")

    for i in range(len(episodes)):
        fileUrl = episodes[i].get_attribute('href')
        print(fileUrl)
        filename = r"../bot3/" + fileUrl.split('/')[-1]
        print("保存文件的路径", filename)
        urllib.request.urlretrieve(fileUrl, filename=filename)
        sleep(3)

    # 退出
    browser.close()
    browser.quit()
