import bs4
from selenium import webdriver
import time
driver = webdriver.Edge()
driver.get("http://192.168.1.1/index.htm")
def AP_scan(driver):
    driver.execute_script("submit_dhcp_mode();")
    time.sleep(5)
    driver.execute_script("wan_setup_show_connect_info();")
    conection_button = driver.find_element_by_id("wan1_status_id")
    conection_button.click()
    time.sleep(10)
    Status(driver)
def Status(driver):
    time.sleep(5)
    status = driver.find_element_by_id("wan1_statu").text
    if status == "Disconnected":
        print("Connecting...")
        Network_tab = driver.find_element_by_id("left_main_menu_entryinternet_config")
        if Network_tab.text == "Network":
            Network_tab.click()
            AP_scan(driver)
    elif status == "Connected":
        print("You are Connected")
        print("The router's IP is: "+ str(driver.find_element_by_id("wan1_ip").text))
        print("Default GateWay is: " +str(driver.find_element_by_id("wan1_gw").text) )
        driver.close()
    else:
        print("you are conecting...")
        Status(driver)
Status(driver)