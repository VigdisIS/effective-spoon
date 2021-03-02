import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import datetime


def create_meeting_agenda(referent):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get('https://online.ntnu.no/auth/login/')

    print("Headless Firefox Initiated...")

    # OW login:

    print("Logging into OW... ")

    f = open("OW_login.txt", "r")
    OWuserName = f.readline().strip()
    OWuserPassw = f.readline().strip()
    f.close()

    userNameField = driver.find_elements_by_name("username")[1]
    time.sleep(0.3)
    # userNameField.send_keys(OWuserName)
    driver.execute_script(f"arguments[0].setAttribute('value', '{OWuserName}')", userNameField);

    passwField = driver.find_elements_by_name("password")[1]
    time.sleep(0.3)
    # passwField.send_keys(OWuserPassw)
    driver.execute_script(f"arguments[0].setAttribute('value', '{OWuserPassw}')", passwField);

    time.sleep(0.3)

    loginBtn = driver.find_elements_by_xpath('/html/body/section[1]/div/div[2]/div/form/button')[0]
    time.sleep(0.3)

    ActionChains(driver).click(loginBtn).perform()

    print("Successfully logged in!")
    print("===============================")
    print("\n")

    time.sleep(1)

    driver.get("https://online.ntnu.no/wiki/komiteer/dotkom/administrativt/motereferater/_create/");

    meeting_date = datetime.date.today() + datetime.timedelta(days=1)  # Tomorrows date

    tittel = f"Møte {meeting_date}"
    print("-------------------------------")
    print("\n")

    # Legger til tittelen på agendaen:

    time.sleep(0.3)

    inputTitle = driver.find_elements_by_xpath('//*[@id="id_title"]')[0]
    time.sleep(0.3)
    driver.execute_script("arguments[0].scrollIntoView();", inputTitle)
    time.sleep(0.3)
    inputTitle.send_keys(tittel)

    time.sleep(0.3)

    # Innhold i selveste agendaen:
    inputContent = driver.find_elements_by_xpath('//*[@id="id_content"]')[0]
    time.sleep(0.3)
    inputContent.send_keys(f"\
📝_Referent_: **{referent}**\n \
    \n\
👁️_Til stede:_\n \
    \n\
😴_Ikke til stede:_\n\
    \n\
🎪_Aktive:_\n\
Tobias, Vigdis, Amund, Johannes, Anna Irene, Julian, Joakim, Thomas, André, Monika, Carl, Anhkha, Gerhard\n\
    \n\
👻_Semi-permitterte:_\n\
Marcel, Aslak, Henrik, August, Storjus, Børge\n\
    \n\
😈_Straffes:_\n\
Hvem som skal straffes ref. [vinstraffregler](https://online.ntnu.no/wiki/komiteer/dotkom/vinstraffregler/), føres opp i [RedWine](https://online.ntnu.no/redwine/dotKom/):\n\
    \n\
- 🍷:\n\
- 🍺:\n\
    \n\
------------\n\
    \n\
# 📣Innsjekk 16:45\n\
    \n\
    \n\
# ☑️Status 16:50\n\
    \n\
    \n\
## ✔️Gjøremål fra sist\n\
    \n\
    \n\
### 📤Mail:\n\
[Mail]\n\
    \n\
### 🔨Andre tasks:\n\
[Andre tasks] \n\
    \n\
## 📌Aktive prosjekter\n\
    \n\
### ⚡OWF\n\
    \n\
### 🍾Vengeful Vineyard\n\
    \n\
### 📑Wiki\n\
    \n\
### 👨‍💻Infrastruktur\n\
    \n\
    \n\
## 📁On hold: Nibble, SDF, Fuzzy Train, Notifier, DS, Splash, Kvittering, Regme, Frank\n\
    \n\
    \n\
# 🧾Saker 17:05\n\
[Saker] \n\
    \n\
    \n\
# 📜HS-saker (feat. styremedlem Monika) 17:30 \n\
    \n\
    \n\
# 💰Cash money updatezz (feat. Mr. Worldwide Thomas) 17:35\n\
    \n\
    \n\
# 📮Mailansvarligs postkassepunkt 17:39\n\
    \n\
_Mailansvarlig forrige uke: **[Forrige mailansvarlig]**_\n\
    \n\
## 🆘Unresolved\n\
    \n\
------------\n\
    \n\
_Mailansvarlig for neste uke: **[Neste mailansvarlig]**_\n\
    \n\
_Ref. [How-to mailansvar](https://online.ntnu.no/wiki/komiteer/dotkom/how-stuff/vaere-mailansvarlig/)_\n\
    \n\
# ⚠️Avviksansvarligs avviksvarslepunkt 17:43\n\
    \n\
    \n\
# 💡Eventuelt 17:46\n\
    \n\
    \n\
# 🤔Til neste gang 17:50\n\
    \n\
    \n\
## 📋Tasks:"

                           )

    slug = driver.find_elements_by_xpath('//*[@id="id_slug"]')[0]
    time.sleep(0.3)
    new_agenda = slug.get_attribute('value')

    time.sleep(0.3)

    createArticleBtn = driver.find_elements_by_xpath('/html/body/section[1]/div/form/div[5]/div[2]/button')[0]
    time.sleep(0.3)
    driver.execute_script("arguments[0].scrollIntoView();", createArticleBtn)
    time.sleep(0.3)

    ActionChains(driver).click(createArticleBtn).perform()

    print("Successfully created new article!")
    print("------------------------------------")
    print("\n")

    time.sleep(1)

    driver.get("https://online.ntnu.no/wiki/komiteer/dotkom/administrativt/motereferater/")

    time.sleep(1)

    editAgendasBtn = driver.find_elements_by_xpath('/html/body/section[1]/div/div[2]/ul/li[5]/a')[0]
    time.sleep(0.3)
    ActionChains(driver).click(editAgendasBtn).perform()
    time.sleep(1.5)

    allAgendasArea = driver.find_elements_by_xpath('//*[@id="id_content"]')[0]
    time.sleep(0.3)
    driver.execute_script("arguments[0].scrollIntoView();", allAgendasArea)
    content = allAgendasArea.get_attribute('value')
    time.sleep(0.3)
    split_val = content.split('\n')
    semester_i = split_val.index("Vår 2021:")

    i_to_insert = semester_i + 2

    meeting_date = datetime.date.today() + datetime.timedelta(days=1)  # Tomorrows date

    line_to_insert = f'- {meeting_date}: [{tittel}]({new_agenda})'

    print("Inserting link to new agenda...")
    print("\n")
    print("This may take a while...")
    print("------------------------------")

    split_val.insert(i_to_insert, line_to_insert)

    new_cont = '\n'.join(split_val)

    time.sleep(0.3)

    allAgendasArea.clear()

    time.sleep(0.3)

    allAgendasArea.send_keys(new_cont)

    time.sleep(0.3)

    saveChangesBtn = driver.find_elements_by_xpath('//*[@id="id_save"]')[0]
    time.sleep(0.3)
    driver.execute_script("arguments[0].scrollIntoView();", saveChangesBtn)
    time.sleep(0.3)

    ActionChains(driver).click(saveChangesBtn).perform()

    time.sleep(1)

    driver.quit()

    motelenke = f"https://online.ntnu.no/wiki/komiteer/dotkom/administrativt/motereferater/{new_agenda}"

    print(
        f"Success! Your new meeting agenda can be found at {motelenke}")

    return referent, motelenke, meeting_date

