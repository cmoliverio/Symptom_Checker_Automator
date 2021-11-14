import functools
import selenium
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
import sys

options = Options()
#options.add_argument("--headless")
#options.add_argument('--disable-gpu')

#flag = 0x08000000  # No-Window flag
# flag = 0x00000008  # Detached-Process flag, if first doesn't work
#webdriver.common.service.subprocess.Popen = functools.partial(
#    webdriver.common.service.subprocess.Popen, creationflags=flag)


def doEmail(email):
    email_label = ('//*[@id="QR~QID22~1"]', email)

    doInfo(email_label)
    clickNextButton()


def doNone():
    check_labels = []
    check_labels.append('//*[@id="QID27-1-label"]')  # Radio button on campus yes
    # check_labels.append('//*[@id="QID11-1-label"]')  # Radio button consent yes
    check_labels.append('//*[@id="QID4-5-label"]')  # None of the above
    check_labels.append('//*[@id="QID5-5-label"]')  # None of the above
    check_labels.append('//*[@id="QID6-5-label"]')  # None of the above
    check_labels.append('//*[@id="QID7-7-label"]') # None of the above

    for i in range(len(check_labels)):
        doCheck(check_labels[i])
        # if not i == len(check_labels) - 1:
        clickNextButton()


def doInfo(info):
    while True:
        try:
            label = firefox.find_element_by_xpath(info[0])
            label.send_keys(info[1])
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break


def doCheck(check_label):
    while True:
        try:
            check_none_of_the_above = firefox.find_element_by_xpath(check_label)
            check_none_of_the_above.click()
        except selenium.common.exceptions.NoSuchElementException:
            continue
        except selenium.common.exceptions.ElementNotInteractableException:
            continue
        break


def clickNextButton():
    # Click next button
    while True:
        button_next = firefox.find_element_by_xpath('//*[@id="NextButton"]')
        try:
            button_next.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            continue
        except selenium.common.exceptions.StaleElementReferenceException:
            continue
        break


for i, argument in enumerate(sys.argv):
    if i == 0:
        continue

    firefox = webdriver.Firefox(options=options)

    firefox.get("https://smcmwellness.iad1.qualtrics.com/jfe/form/SV_cvHHRAtvDk7Xu0B")

    doEmail(argument)
    doNone()

    time.sleep(1)

    firefox.close()
    firefox.quit()

    time.sleep(1)
