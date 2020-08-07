from time import sleep

from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('http://rpademo.automationanywhere.com/master-pdf.php')

username = "candidate"
password = "LetMeIn123!"

browser.find_element_by_xpath("/html/body/form/center/table/tbody/tr[1]/td/input").send_keys(username)
browser.find_element_by_xpath("/html/body/form/center/table/tbody/tr[2]/td/input").send_keys(password)
browser.find_element_by_xpath("/html/body/form/center/table/tbody/tr[3]/td[2]/input").click()


sleep(10)
#退出
browser.close()
browser.quit()