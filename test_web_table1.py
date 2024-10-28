import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import time


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

@allure.title("TestCase #1 to find a Following-sibling of Yoshi Tannamuri")
@allure.step("Get following sibling of 'Yoshi Tannamuri'")
def test_get_following_sibling(setup):
    driver = setup
    # XPath to locate "Yoshi Tannamuri" and get the following sibling
    following_sibling_xpath = "//td[text()='Yoshi Tannamuri']/following-sibling::td[1]"
    following_sibling = driver.find_element(By.XPATH, following_sibling_xpath)
    print("Following sibling of 'Yoshi Tannamuri':", following_sibling.text)
    allure.attach(following_sibling.text, name="Following Sibling Value", attachment_type=allure.attachment_type.TEXT)

@allure.title("TestCase #2 to find a Following-sibling of Helen Bennet")
@allure.step("Get following sibling of 'Helen Bennet'")
def test_finding_following_sibling(setup):
    driver = setup
    # Locate all rows in the table
    rows = driver.find_elements(By.XPATH, "//table[@id='customers']//tr")
    cols = driver.find_elements(By.XPATH, "//table[@id='customers']//tr[2]/td")
    row_totals = len(rows)
    column_totals = len(cols)

    first_part = '//table[@id = "customers"]/tbody/tr['
    second_part = "]/td["
    third_part = "]"

    for row in range(2,row_totals+1):
        for col in range(1,column_totals+1):
            dynamic_path = f"{first_part}{row}{second_part}{col}{third_part}"
            data = driver.find_element(By.XPATH,dynamic_path).text
            # Attach results to allure report


            if "Helen Bennet" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH,country_path).text
                assert "UK" in country_text, f"Not in the {country_text}"
                print(f"Helen Bennet is in {country_text}")



            """
            following_sibling_xpath = "//td[text()='Yoshi Tannamuri']/following-sibling::td[1]"
            preceding_sibling_xpath = "//td[text()='Yoshi Tannamuri']/preceding-sibling::td[1]"
            print("following_sibling_xpath ", following_sibling_xpath)
            print("preceding_sibling_xpath ", preceding_sibling_xpath)
            following_sibling = driver.find_element(By.XPATH, following_sibling_xpath)
            preceding_sibling = driver.find_element(By.XPATH, preceding_sibling_xpath)
            print("Following sibling of 'Yoshi Tannamuri':", following_sibling.text)
            print("preceding sibling of 'Yoshi Tannamuri':", preceding_sibling.text)
            assert "Canada" in following_sibling.text, "Not matching"
            allure.attach(following_sibling.text, name="Following Sibling Value",
                          attachment_type=allure.attachment_type.TEXT)
            """
    allure.attach(str(row_totals), name="Row Totals", attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(column_totals), name="Column Totals", attachment_type=allure.attachment_type.TEXT)



