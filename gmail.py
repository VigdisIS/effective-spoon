import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def send_email(referent, motelenke, meeting_date):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get('https://mail.google.com/mail/u/1/?pli=1#inbox?compose=new')

    print("Headless Firefox Initiated...")

    # Gsuite login:

    print("Logging into gmail... ")

    f = open("Gsuite_login.txt", "r")
    GmailUN = f.readline().strip()
    GmailPW = f.readline().strip()
    f.close()

    time.sleep(0.3)

    ActionChains(driver).send_keys(f"{GmailUN}").perform()
    time.sleep(0.3)

    nesteBtn = driver.find_elements_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')[0]

    time.sleep(0.3)

    ActionChains(driver).click(nesteBtn).perform()

    time.sleep(1)

    ActionChains(driver).send_keys(f"{GmailPW}").perform()

    time.sleep(1)

    nesteBtn = driver.find_elements_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')[0]

    time.sleep(0.2)

    ActionChains(driver).click(nesteBtn).perform()

    time.sleep(3)

    createNewBtn = driver.find_elements_by_xpath(
        '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')[0]
    time.sleep(0.3)

    print("Successfully logged in!")
    print("===========================")
    print("\n")

    ActionChains(driver).click(createNewBtn).perform()
    time.sleep(1)

    print("Writing new email...")
    print("\n")

    print("Sending to Dotkom (dotkom@online.ntnu.no)...")
    time.sleep(1)
    ActionChains(driver).send_keys("dotkom@online.ntnu.no").perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.RETURN).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.TAB).perform()

    print(f"Adding email subject: [Møte] 📣Møteinnkalling {meeting_date}...")
    time.sleep(0.5)
    ActionChains(driver).send_keys(f'[Møte] 📣Møteinnkalling {meeting_date}').perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.TAB).perform()

    content = f" \
Heihei! \n \
    \n \
Her kommer innkalling til ukens onsdagsmøte:)\n\
    \n \
📍Sted: Grønnbygget MA23 / Online-discorden  \n \
⌚Tid: møt opp 16:30, vi starter 16:45 \n \
📝Referent: {referent} \n \
📋Agenda: {motelenke} \n \
    \n \
Som alltid, dersom du ikke har mulighet til å komme, svar på denne mailen eller send dm til meg, Thomas, eller Anhkha =)) (husk grunn!) \n \
    \n \
<3 <3,"

    print(f"Adding email content...")
    ActionChains(driver).send_keys(content).perform()
    time.sleep(0.3)

    print("\n")

    print("Email written successfully!")
    print("==============================")

    driver.quit()
