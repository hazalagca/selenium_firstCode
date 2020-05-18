from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()
browser.get("http://urlInformation")
#wait = WebDriverWait(browser, 20)
#buton click işleminde buton üzerinde inspect yapılarak buton komut satırında sağ tık inspectcoy xpath
#değişken tanımlanıp xpath elementi bulunması sağlanır. 
#pathler çift tırnak ile belirtilir. path içerisindeki çift tırnaklar tek tırnak olarak çevirilir.
#degisken=browser.find_element_by_xpath(xpathbilgisi) degisken.click()
print("open Chrome")
name=browser.find_element_by_name("ctl00$ContentPlaceHolder1$txtUsername")
password=browser.find_element_by_name("ctl00$ContentPlaceHolder1$txtPassword")
#send_key$ ile değer girilir.
name.send_keys("username")
password.send_keys("password")
time.sleep(2)
login=browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_btnLogin']")
login.click()
time.sleep(2)
browser.get("http://otherUrlInformatin)
print("Added Campaign")

camp_type=Select(browser.find_element_by_name("ctl00$ContentPlaceHolder1$ddlCampaignTypes"))
camp_type.select_by_index(1)
print("Selected Campaign Type")
time.sleep(2)
#browser.find_element_by_xpath(".//*[contains(text),'Segment Bağımsız Prepaid')]").click()
#browser.find_element_by_xpath(".//*[contains(text),'Segment Bağımsız Postpaid')]").click()
segment=browser.find_element_by_xpath("//*[@id='SegmentTree']/li/span[2]").click()
time.sleep(2)
print("Click Campign Segment Type")
#browser.close()