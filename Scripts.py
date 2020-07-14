from selenium import webdriver
chrome_path = r"C:\My_Files\DiscoverCampingProject\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.discovercamping.ca/bccweb/Facilities/SearchViewUnitAvailabity.aspx")
driver.find_element_by_xpath("""//*[@id="down_icn103"]/div[2]/div/div[2]/div[1]/div[2]/div/div""").click()
driver.find_element_by_xpath("""//*[@id="number_3"]/div[3]/table/tbody/tr[8]/td[2]/div/div[2]/a""").click()
from bs4 import BeautifulSoup
import requests
--resp = requests.get('https://www.discovercamping.ca/bccweb/Facilities/SearchViewUnitAvailabity.aspx')
--txt = resp.text
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'html.parser')
t = soup.find("td", {"class":"blue_brd_box"})['title']
print(t)