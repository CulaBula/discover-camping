from selenium import webdriver
from bs4 import BeautifulSoup
import time
#Point to web driver 
chrome_path = r"C:\My_Files\discover-camping\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
#Go to site
driver.get("https://www.discovercamping.ca/bccweb/Facilities/SearchViewUnitAvailabity.aspx")
#Select Calendar
driver.find_element_by_id("mainContent_SearchUnitAvailbity_txtArrivalDate").click();
#Choose July 29th
driver.find_element_by_xpath("""//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]/a""").click()
#Click Search
driver.find_element_by_xpath("""//*[@id="divPlaceSearchParameter"]/div/div[2]/div[1]/div[5]/a""").click()
time.sleep(1)
#Choose Porpoise Bay Park
driver.find_element_by_xpath("""//*[@id="down_icn103"]/div[2]/div/div[1]/div/div/div""").click()
time.sleep(1)
#Choose standard site(has to be green)
driver.find_element_by_xpath("""//*[@id="number_103"]/div[3]/table/tbody/tr[2]/td[2]/div/div[2]/a""").click()
time.sleep(1)
#Pull out available dates
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'html.parser')
t = soup.find("td", {"class":"blue_brd_box"})['title']
print(t)


