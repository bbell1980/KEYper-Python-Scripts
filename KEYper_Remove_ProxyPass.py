from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
import time

url = input('Enter the url: ')
passCode = input('Enter the password: ')

browser = webdriver.Firefox(executable_path=r'C:/geckodriver/geckodriver.exe')
browser.get(url)
assert "Administration" in browser.title
elem = browser.find_element_by_name("txtPassword")
elem.clear()
elem.send_keys(passCode)
elem.send_keys(Keys.RETURN)
print(browser.title)

wdw1 = WebDriverWait(browser, 3).until(
    lambda d: d.find_element_by_link_text("Manage Users"))

print(wdw1)

ActionChains(browser).move_to_element(wdw1).perform()

wdw2 = WebDriverWait(browser, 3).until(
    lambda d: d.find_element_by_link_text("Edit Users"))

print(wdw2)
ActionChains(browser).move_to_element(wdw2).click(wdw2).perform()


# Page Count
# pageCount = browser.execute_script(
#     "return document.getElementsByTagName('td').length")
# print(pageCount)

# count of users
wdwUserCount = WebDriverWait(browser, 3).until(
    lambda d: d.find_element_by_id("contentTitle_lblCount"))
userCount = wdwUserCount.text
print(int(userCount))

#pageCount = int(userCount)/35

pages = math.ceil(int(userCount)/35)
leftover = math.remainder(int(userCount), 35)

print("There should be " + str(pages) + " pages.")
print("On page " + str(pages) + " there are only " + str(leftover) + "users.")

pageInc = 1
while pageInc < pages+1:
    print("Start Page " + str(pageInc))

    rowCount = 0

    if pageInc < pages:
        rowsToCount = 35
    elif pageInc == pages:
        rowsToCount = leftover

    while rowCount < rowsToCount:
        print("Start row number " + str(rowCount))

        print("Finding 'EDIT' on page: " +
              str(pageInc) + " row:" + str(rowCount))
        wdw3 = WebDriverWait(browser, 10).until(
            lambda d: d.find_element_by_id("contentMain_listGrid_btnEdit_" + str(rowCount)))
        print("Clicking 'EDIT' on page: " +
              str(pageInc) + " row:" + str(rowCount))
        wdw3.click()
        # wdw3.send_keys(Keys.RETURN)
        # ActionChains(browser).move_to_element(wdw3).click(wdw3).perform()

        print("Finding the prox password box")
        wdw4 = WebDriverWait(browser, 5).until(
            lambda d: d.find_element_by_name("ctl00$contentMain$txtPasswordProx"))
        print("Clearing prox password box")
        wdw4.clear()

        print("Finding the Save Button")
        wdw5 = WebDriverWait(browser, 2).until(
            lambda d: d.find_element_by_name("ctl00$contentMain$imgbtnSave"))
        print("Clicking the Save button")
        wdw5.send_keys(Keys.RETURN)

        print("Finished with page:" + str(pageInc) + ", row:" + str(rowCount))

        rowCount += 1

        print("Current Row Count: " + str(rowCount))

    pageInc += 1

    print("Incriment Page To: " + str(pageInc))

    wdw6 = WebDriverWait(browser, 10).until(
        lambda d: d.find_element_by_xpath("/html/body/form/div[5]/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/table/tbody/tr[37]/td/table/tbody/tr/td[" + str(pageInc) + "]/a"))
    # wdw6.send_keys(Keys.RETURN)
    wdw6.click()

    print("Reseting Row Count")
    rowCount = 0

print(browser.title)

browser.close()
