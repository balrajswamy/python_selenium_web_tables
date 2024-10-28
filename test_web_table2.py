import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import time


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

#

@allure.title("TestCase #1 to find a table ")
@allure.step("Check the UAE in the Country list")
def test_verify_uae_in_country(setup):
    driver = setup
    # Locate all rows in the table
    rows = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody/tr")
    cols = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody/tr[2]/td")
    row_totals = len(rows)
    column_totals = len(cols)
    with allure.step("Checking UAE is present in the table"):
        for row in rows:
            cols = row.find_elements(By.TAG_NAME,"td")
            for col in cols:
                print("column text is ", col.text)
                if "UAE" in col.text:
                    print("YES")
                break

    allure.attach(str(row_totals), name="Row Totals", attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(column_totals), name="Column Totals", attachment_type=allure.attachment_type.TEXT)