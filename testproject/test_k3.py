from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"
driver.get(url)

input_id = "title"
adatok = [["abcd1234\n", ""], ["teszt233@\n", "Only a-z and 0-9 characters allewed"],
          ["abcd\n", "Title should be at least 8 characters; you entered 4."]]


def teszteld(a, b):
    driver.find_element_by_id(input_id).send_keys(a)
    return driver.find_element_by_tag_name("span").text == b


def test_01():  # Helyes adatokkal
    assert teszteld(adatok[0][0], adatok[0][1])


def test_02():  # Rossz karakterekkel
    driver.refresh()
    assert teszteld(adatok[1][0], adatok[1][1])


def test_03():  # Rövid szöveggel
    driver.refresh()
    assert teszteld(adatok[2][0], adatok[2][1])
    driver.close()