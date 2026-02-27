import pytest
from pages.registration_page import RegistrationPage


@pytest.mark.smoke
def test_enter_first_name(driver):
    page = RegistrationPage(driver)
    page.open()
    page.enter_first_name("Vipul")
    assert page.find(page.FIRST_NAME).get_attribute("value") == "Vipul"


@pytest.mark.smoke
def test_select_gender(driver):
    page = RegistrationPage(driver)
    page.open()
    page.select_gender_male()
    assert page.find(page.GENDER_MALE).is_selected()


@pytest.mark.smoke
def test_select_skill(driver):
    page = RegistrationPage(driver)
    page.open()
    page.select_skill("Python")
    assert True


@pytest.mark.regression
def test_complete_registration_form(driver):
    page = RegistrationPage(driver)
    page.open()

    page.enter_first_name("Vipul")
    page.enter_last_name("Nimbale")
    page.enter_address("Pune Maharashtra")
    page.enter_email("vipul@test.com")
    page.enter_phone("9876543210")

    page.select_gender_male()
    page.select_hobby_cricket()

    page.select_skill("Python")
    # page.select_country("India")
    page.select_searchable_country("India")

    page.select_dob("1998", "May", "10")

    page.enter_password("Test@123")
    page.confirm_password("Test@123")

    page.submit_form()

    assert "Register" in driver.title