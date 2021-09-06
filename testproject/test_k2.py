# Megjegyzés: a weboldal nem a Pitagorasz-tétel szerint számol: 2*2 +3*3 != 10*10
import time

"/html/body/br./text()"
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
driver.get(url)

szinek = {"IndianRed", "Pink", "HotPink", "Coral", "OrangeRed", "DarkOrange", "Yellow", "DarkKhaki", "Violet",
          "MediumOrchid", "DarkMagenta", "Chartreuse", "MediumSpringGreen", "DarkGreen", "DarkCyan", "Turquoise",
          "RoyalBlue", "NavajoWhite", "SaddleBrown", "Gray", "Black", "AliceBlue", "OldLace", "Chocolate"}
id_k = ['randomColorName', 'randomColor', 'testColor', 'start',
        'stop', 'result']  # Színnév, szín, szóközök backgroundos stílussal, startgomb, stopgomb, eredmény

ures_szoveg = "[     ]"


def test_01():  # induláskor
    log = driver.find_element_by_id(id_k[0]).text in szinek  # A színek között van a neve
    log = log and driver.find_element_by_id(id_k[2]).text == ures_szoveg
    assert log


def test_02():  # Elindul, leállítható.
    log = True
    try:
        driver.find_element_by_id(id_k[3]).click()
        time.sleep(3)
        driver.find_element_by_id(id_k[4]).click()
    except:
        log = False
    assert log


def test_03():  # Kijelzi a végén az eredményt
    log = True
    try:
        driver.find_element_by_id(id_k[3]).click()
        time.sleep(2)
        driver.find_element_by_id(id_k[4]).click()
        if driver.find_element_by_id(id_k[1]).get_attribute("style") == driver.find_element_by_id(
                id_k[2]).get_attribute("style"):
            log = log and driver.find_element_by_id(id_k[5]).text == "Correct!"
        else:
            log = log and driver.find_element_by_id(id_k[5]).text == "Incorrect!"

    except:
        log = False
    assert log


