# A jobbra-balra lépést értelemszerűen megcseréltem, úgy lesz helyes a teszt a 3. tesztesetben.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
driver.get(url)

xpath = "/html/body/div/div/p[3]"
ascii_tab = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
hossza = len(ascii_tab)

karakter_id = "chr"
muvelet_id = "op"
operandus = {"+", "-"}
szam_id = "num"
submitgomb = "submit"
eredmeny = "result"


def test_01():
    return driver.find_element_by_xpath(xpath).text == ascii_tab


def test_02():
    log = ascii_tab.find(driver.find_element_by_id(karakter_id).text) > -1  # Benne van.
    log = log and driver.find_element_by_id(muvelet_id).text in operandus
    egesz = str(float(driver.find_element_by_id(szam_id).text))  # Egész, ha .0-ra végződik a floatja.
    log = log and egesz[-2] == "." and egesz[-1] == "0"
    assert log


def test_03():
    driver.find_element_by_id(submitgomb).click()
    hol = int(ascii_tab.find(driver.find_element_by_id(karakter_id).text))  # Hol van?
    mennyivel = int(driver.find_element_by_id(szam_id).text)  # Vigyük arrébb.
    vege = driver.find_element_by_id(eredmeny).text
    if driver.find_element_by_id(muvelet_id).text == "+":
        assert ascii_tab[(hol + mennyivel) % hossza] == vege  # Modulo, mert túlcsordulhat.
    else:
        assert ascii_tab[(hol - mennyivel) % hossza] == vege
    driver.close()