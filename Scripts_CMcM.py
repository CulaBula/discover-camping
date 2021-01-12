from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

## User Input ##
#year_input = "2022"
month_input = "March"
day_input = "20"
day_count = "2"

#Point to web driver 
    chrome_path = "chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

#Go to site
driver.get("https://www.discovercamping.ca/bccweb/Facilities/SearchViewUnitAvailabity.aspx")

#Select Calendar
driver.find_element_by_id("mainContent_SearchUnitAvailbity_txtArrivalDate").click();
#Setup beatiful soup for date picker
content_date = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content_date, 'html.parser')

#Month
while True:
    if soup.find("span",{"class":"ui-datepicker-month"}).get_text(strip=True) != month_input:
        content_month = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content_month, 'html.parser') 
        driver.find_element_by_xpath("""//*[@id="ui-datepicker-div"]/div[2]/a[2]""").click()        
    else:
        break
#Year
#print(soup.find("span",{"class":"ui-datepicker-year"}).get_text(strip=True))
#Day
driver.find_element_by_link_text(day_input).click()
#Day count
Select(driver.find_element_by_id('ddlNightsSearchUnitAvailbity')).select_by_value(day_count)
#Click Search
driver.find_element_by_xpath("""//*[@id="divPlaceSearchParameter"]/div/div[2]/div[1]/div[5]/a""").click()
time.sleep(1)

#Get list of all locations with available sites
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'html.parser')
loc_list = []
sts_list = []
#Get list of all locations
for loc in soup.find_all("a",{"class":"PlaceName"}):
    loc_list.append(str(loc.get_text()))
#Get list of all location statuses
for sts in soup.find_all("div",{"class":"available_btn_list"}):    
    sts_list.append(str(sts.get_text()))
#Combine the 2 lists
full_list = zip(loc_list,sts_list)
#Output List
park_list = []
fac_list = []
unit_type_list = []
unit_status_list = []
i = 0
main_dict = {}
fac_dict = {'facilities':{}}
#loop through and print Available
print ("The following have sites available:")
for a,b in full_list:
    if b.strip() == "Available":      
        driver.find_element_by_xpath("//a[contains(@class, 'PlaceName') and contains(text(), '"+str(a.strip())+"')]").click()
        time.sleep(0.5)
        content_loc = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content_loc, 'html.parser')
        table_div = soup.find('div' , {'id': 'right_box_data' })
        park_name = table_div.find('div' , {'class': 'right_park_name' }).get_text()
        if park_name != a:
            print("Timeout error")
        park_list.append(park_name)
        # main_dict[park_name] = fac_dict
        for sts in table_div.find_all('tr'):
            for fac in sts.find_all('span'):
                unit_type_list = []
                unit_status_list = []
                if re.search('span_.',str(fac.get_text)):
                    facility = (fac.get_text())
                    fac_list.append(facility)
                    fac_dict['facilities'][facility] = {} 
            for un_type in sts.find_all("div",{"class":"ellipsis_one_lien"}):
                #Strip out unit name
                if un_type.get_text() != "Show Next Date Available":                    
                    unit_type = un_type.get_text().strip()
                    unit_type_list.append(unit_type)                    
                #Strip out status
                unit_status_raw = str(un_type.find('img')['src'])
                if unit_status_raw == "../CommonThemes/Images/round_red.png":
                    unit_status= "Unavailable"
                elif unit_status_raw == "../CommonThemes/Images/round_2.png":
                    unit_status= "Low Availablity"
                elif unit_status_raw == "../CommonThemes/Images/round_1.png":
                    unit_status= "Available"                
                else:
                    unit_status= "Error"
                unit_status_list.append(unit_status)
                fac_dict['facilities'][facility]['type'] = unit_type_list
                fac_dict['facilities'][facility]['status'] = unit_status_list
        main_dict[park_name] = fac_dict

df = pd.DataFrame(data=main_dict)
df.to_csv('cg_data.csv')
print(main_dict)
# print(park_list)
# print(fac_list)
# print(unit_type_list)
# print(unit_status_list)

                
#           print(" ".join(str(sts.get_text()).split()))

            
## Test Code ##



#find_elements_by_xpath(day_xpath).click()

##table =  driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']")
##table.find_elements_by_xpath(".//tr[@class='ui-state-default'][contains(text(),"+day_input+")]").click()
#driver.find_element_by_xpath("//td[@class= ' '/a/"+day_input+"]").click()
    
##    if len([td.text for td in row.find_elements_by_xpath(".//td[@class=' ui-datepicker-week-end ui-datepicker-days-cell-over  ui-datepicker-current-day ui-datepicker-today'][1]")]) >= 1:
##        print([td.text for td in row.find_elements_by_xpath(".//td[@class=' ui-datepicker-week-end ui-datepicker-days-cell-over  ui-datepicker-current-day ui-datepicker-today'][1]")][0])


#    if str([td.text for td in row.find_elements_by_xpath(".//td[@class='ui-state-default'][1]")][0]) == day_input:
#        [td.text for td in row.find_elements_by_xpath(".//td[@class='ui-state-default'][1]")][0].click()
#        print([td.text for td in row.find_elements_by_xpath(".//td[@id='ui-datepicker-div'][1]")])
#        print([td.text for td in row.find_elements_by_xpath(".//td[@class=' ui-datepicker-week-end ui-datepicker-days-cell-over  ui-datepicker-current-day ui-datepicker-today'][1]")][0])
##    if soup.find_all("a",{"class":"ui-state-default"})
##        print(soup.find("span",{"class":"ui-datepicker-month"}).get_text(strip=True))
##    else:
##        driver.find_element_by_xpath("""//*[@id="ui-datepicker-div"]/div[2]/a[2]""").click()
##        content_day = driver.page_source.encode('utf-8').strip()
##        soup = BeautifulSoup(content_day, 'html.parser')
##        break

#Choose July 29th
#driver.find_element_by_xpath("""//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]/a""").click()




###Select Calendar
##driver.find_element_by_id("mainContent_SearchUnitAvailbity_txtArrivalDate").click();
###Choose July 29th
##driver.find_element_by_xpath("""//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[4]/a""").click()
###Click Search
##driver.find_element_by_xpath("""//*[@id="divPlaceSearchParameter"]/div/div[2]/div[1]/div[5]/a""").click()
##time.sleep(1)
###Choose Porpoise Bay Park
##driver.find_element_by_xpath("""//*[@id="down_icn103"]/div[2]/div/div[1]/div/div/div""").click()
##time.sleep(1)
###Choose group site(has to be green)
##driver.find_element_by_xpath("""//*[@id="number_103"]/div[3]/table/tbody/tr[5]/td[2]/div/div[2]/a""").click()
##time.sleep(1)
###Pull out available dates
##content = driver.page_source.encode('utf-8').strip()
##soup = BeautifulSoup(content, 'html.parser')
##t = soup.find_all("td", {"class":"btn_red btn_red_brd"})
##print([x['title'].split()[-1] for x in t])
##site_date = {}
##tmp_list = []
##for x in range(len(t)):      
##    if t[x]['title'].split()[-5] == t[x-1]['title'].split()[-5]:
##        tmp = x['title'].split()
##
##    if tmp_list:
##        tmp_list.append(site_date[tmp[-1]])
##        site_date[tmp[-5]] = tmp_list
##    else:
##        tmp_list = []
##
##print('Site dates are:')
##print(site_date)
##"""site_date['Y1']"""
