# Megjegyzés: a weboldal nem a Pitagorasz-tétel szerint számol: 2*2 +3*3 != 10*10
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
driver.get(url)

id_k = ['a', 'b', 'submit', 'results']
adatok = [["", "", ""], ["2", "3", "c: 10"], ["", "", "c: NaN"]]


def vizsgal(a, b, c):
    log = driver.find_element_by_id(id_k[0]).get_attribute("value") == a
    log = log and driver.find_element_by_id(id_k[1]).get_attribute("value") == b
    log = log and driver.find_element_by_id(id_k[3]).text == c
    return log


def tesztel(a, b, c):
    driver.refresh()
    driver.find_element_by_id(id_k[0]).send_keys(a)
    driver.find_element_by_id(id_k[1]).send_keys(b)
    driver.find_element_by_id(id_k[2]).click()
    time.sleep(1)
    return driver.find_element_by_id(id_k[3]).text == c


def test_01():  # Betöltléskor
    assert vizsgal(adatok[0][0], adatok[0][1], adatok[0][2])


def test_02():  # Helyes adatokkal
    assert tesztel(adatok[1][0], adatok[1][1], adatok[1][2])


def test_03():  # Üres adatokkal
    assert tesztel(adatok[2][0], adatok[2][1], adatok[2][2])
    driver.close()
