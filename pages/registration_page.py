from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage
from config.config import BASE_URL


class RegistrationPage(BasePage):

    # ================= LOCATORS =================

    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    ADDRESS = (By.TAG_NAME, "textarea")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PHONE = (By.XPATH, "//input[@type='tel']")

    GENDER_MALE = (By.XPATH, "//input[@value='Male']")
    GENDER_FEMALE = (By.XPATH, "//input[@value='FeMale']")

    HOBBY_CRICKET = (By.ID, "checkbox1")
    HOBBY_MOVIES = (By.ID, "checkbox2")
    HOBBY_HOCKEY = (By.ID, "checkbox3")

    SKILLS = (By.ID, "Skills")
    COUNTRY = (By.ID, "countries")

    SELECT_COUNTRY_CONTAINER = (By.XPATH, "//span[@role='combobox']")
    SELECT_COUNTRY_SEARCH = (By.XPATH, "//input[@type='search']")

    YEAR = (By.ID, "yearbox")
    MONTH = (By.XPATH, "//select[@placeholder='Month']")
    DAY = (By.ID, "daybox")

    PASSWORD = (By.ID, "firstpassword")
    CONFIRM_PASSWORD = (By.ID, "secondpassword")

    SUBMIT = (By.ID, "submitbtn")

    # ================= METHODS =================

    def open(self):
        self.open_url(BASE_URL)

    def enter_first_name(self, value):
        self.type(self.FIRST_NAME, value)

    def enter_last_name(self, value):
        self.type(self.LAST_NAME, value)

    def enter_address(self, value):
        self.type(self.ADDRESS, value)

    def enter_email(self, value):
        self.type(self.EMAIL, value)

    def enter_phone(self, value):
        self.type(self.PHONE, value)

    def select_gender_male(self):
        self.click(self.GENDER_MALE)

    def select_gender_female(self):
        self.click(self.GENDER_FEMALE)

    def select_hobby_cricket(self):
        self.click(self.HOBBY_CRICKET)

    def select_skill(self, value):
        Select(self.find(self.SKILLS)).select_by_visible_text(value)

    def select_country(self, value):
        Select(self.find(self.COUNTRY)).select_by_visible_text(value)

    # def select_searchable_country(self, value):
    #     self.click(self.SELECT_COUNTRY_CONTAINER)
    #     self.type(self.SELECT_COUNTRY_SEARCH, value)
    #     self.click((By.XPATH, f"//li[contains(text(),'{value}')]"))

    def select_searchable_country(self, value):
        wait = WebDriverWait(self.driver, 10)

        element = self.find(self.SELECT_COUNTRY_CONTAINER)

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Wait until clickable
        wait.until(EC.element_to_be_clickable(self.SELECT_COUNTRY_CONTAINER))

        element.click()

        self.type(self.SELECT_COUNTRY_SEARCH, value)

        country_option = (By.XPATH, f"//li[contains(text(),'{value}')]")
        wait.until(EC.element_to_be_clickable(country_option))

        self.click(country_option)

    def select_dob(self, year, month, day):
        Select(self.find(self.YEAR)).select_by_visible_text(year)
        Select(self.find(self.MONTH)).select_by_visible_text(month)
        Select(self.find(self.DAY)).select_by_visible_text(day)

    def enter_password(self, value):
        self.type(self.PASSWORD, value)

    def confirm_password(self, value):
        self.type(self.CONFIRM_PASSWORD, value)

    def submit_form(self):
        self.click(self.SUBMIT)