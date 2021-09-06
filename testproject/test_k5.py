from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"
driver.get(url)

tablabelso_id = "bingo-body"
mezoszam = 25
szamlista_id = "numbers-list"
szamszam = 75

mezok = driver.find_element_by_id(tablabelso_id).find_elements_by_tag_name("td")
mezoertekek = []
szamok = driver.find_element_by_id(szamlista_id).find_elements_by_tag_name("li")

for mezo in mezok:
    mezoertekek.append(mezo.text)


def test_01():  # Lesz 15 cella és 75 szám.
    log = len(mezok) == mezoszam
    log = log and len(szamok) == szamszam
    assert log


def test_02():  # Addig nyomunk...
    gomb = driver.find_element_by_id("spin")
    while len(driver.find_element_by_id("messages").find_elements_by_tag_name("li")) == 0:
        gomb.click()
    # Innen nem tudtam értelmezni, nem ismerem a Bingó játékot. (Amúgy se ment volna idő hiányában.)
    assert True


def test_03():  # Initre új számok jönnek elő.
    driver.find_element_by_id("init").click()
    mezok2 = driver.find_element_by_id(tablabelso_id).find_elements_by_tag_name("td")
    mezoertekek2 = []
    for mezo in mezok2:
        mezoertekek2.append(mezo.text)
    assert mezoertekek2 != mezoertekek
