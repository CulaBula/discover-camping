from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import time
import calendar
import datetime
import os


def scrape(param_dict):

    ## User Input ##
    dt_obj = datetime.datetime.strptime(param_dict["date"], "%Y-%m-%d")
    
    #month_input = "March"
    month_input = calendar.month_name[dt_obj.month]
    day_input = str(dt_obj.day)
    day_count = param_dict["num_nights"]

    #Point to web driver 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#     chrome_path = "chromedriver.exe"
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(chrome_path, chrome_options=options)
#  #   driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    #Go to site
    driver.get("https://www.discovercamping.ca/bccweb/Facilities/SearchViewUnitAvailabity.aspx")

    #BC residency redirect
    if "bcresidency" in driver.current_url: # check if "bcresidency" is in URL
        driver.find_element_by_id("confirm-bc-resident").click()

    #Select Calendar
    driver.find_element_by_id("mainContent_SearchUnitAvailbity_txtArrivalDate").click()
    #Setup beatiful soup for date picker
    content_date = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content_date, 'html.parser')

    #Month
    while True:
        content_month = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content_month, 'html.parser') 
        if soup.find("span",{"class":"ui-datepicker-month"}).get_text(strip=True) != month_input:
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

    #Make sure map is not selected
    if soup.find("a",{"class":"map_icon"}).get_text(strip=True) != "List View":
        driver.find_element_by_id("mainContent_SearchUnitAvailbity_txtArrivalDate").click()

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
    main_list = []
    #loop through and print Available
    print ("The following have sites available:")
    for a,b in full_list:
        if b.strip() == "Available":
            driver.find_element_by_xpath("//a[contains(@class, 'PlaceName') and contains(text(), '"+str(a.strip())+"')]").click()
            time.sleep(0.5)
            content_loc = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content_loc, 'html.parser')
            table_div = soup.find('div' , {'id': 'right_box_data' })
            park_name = table_div.find('h1' , {'class': 'right_park_name' }).get_text()
            if park_name != a:
                print("Timeout error")
            # main_dict[park_name] = fac_dict
            for sts in table_div.find_all('tr'):
                for fac in sts.find_all('span'):
                    if re.search('span_.',str(fac.get_text)):
                        facility = (fac.get_text())                    
                        for un_type in sts.find_all("div",{"class":"ellipsis_one_lien"}):
                            #Strip out unit name
                            if un_type.get_text() != "Show Next Date Available":                    
                                unit_type = un_type.get_text().strip()                  
                            #Strip out status
                            unit_status_raw = str(un_type.find('img')['src'])
                            if unit_status_raw == "../CommonThemes/Images/round_2.png":
                                unit_status= "Low Availability"
                            elif unit_status_raw == "../CommonThemes/Images/round_1.png":
                                unit_status= "Available"                                                 
                            else:
                                unit_status= "Unavailable"
                            fact_dict = {}
                            fact_dict['park_name'] = park_name
                            fact_dict['park_facility'] = facility
                            fact_dict['park_type'] = unit_type
                            fact_dict['park_status'] = unit_status
                            #print(fact_dict)
                            main_list.append(fact_dict)
                        
    return main_list