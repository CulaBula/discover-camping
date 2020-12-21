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
#Choose group site(has to be green)
driver.find_element_by_xpath("""//*[@id="number_103"]/div[3]/table/tbody/tr[5]/td[2]/div/div[2]/a""").click()
time.sleep(1)
#Pull out available dates
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'html.parser')
t = soup.find_all("td", {"class":"blue_brd_box"})
print([x['title'].split()[-1] for x in t])
"""
site_date = {}
tmp_list = []
for x in range(len(t)):      
    if t[x]['title'].split()[-5] == t[x-1]['title'].split()[-5]
        
    tmp = x['title'].split()
    if tmp_list:
        tmp_list.append(site_date[tmp[-1]])
        site_date[tmp[-5]] = tmp_list
    else:
        tmp_list = []

print('Site dates are:')
print(site_date)
site_date['Y1']
"""
