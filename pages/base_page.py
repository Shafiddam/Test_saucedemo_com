import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators

current_url = None


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def enter_login_standard_user(self):
        """ вводим user_name и password: """
        name = "standard_user"
        password = "secret_sauce"
        user_name = self.browser.find_element(*BasePageLocators.INPUT_USER_NAME)
        user_name.send_keys(name)
        user_name.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        field_password = self.browser.find_element(*BasePageLocators.INPUT_PASSWORD)
        field_password.send_keys(password)
        field_password.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        button_login = self.browser.find_element(*BasePageLocators.BUTTON_LOGIN)
        button_login.click()
        # time.sleep(2)

    def enter_login_locked_out_user(self):
        """ вводим в поле поиска слово "Тензор": """
        name = "locked_out_user"
        password = "secret_sauce"
        user_name = self.browser.find_element(*BasePageLocators.INPUT_USER_NAME)
        user_name.send_keys(name)
        user_name.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        field_password = self.browser.find_element(*BasePageLocators.INPUT_PASSWORD)
        field_password.send_keys(password)
        field_password.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        button_login = self.browser.find_element(*BasePageLocators.BUTTON_LOGIN)
        button_login.click()
        # time.sleep(2)

    def enter_login_problem_user(self):
        """ вводим в поле поиска слово "Тензор": """
        name = "problem_user"
        password = "secret_sauce"
        user_name = self.browser.find_element(*BasePageLocators.INPUT_USER_NAME)
        user_name.send_keys(name)
        user_name.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        field_password = self.browser.find_element(*BasePageLocators.INPUT_PASSWORD)
        field_password.send_keys(password)
        field_password.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        button_login = self.browser.find_element(*BasePageLocators.BUTTON_LOGIN)
        button_login.click()
        # time.sleep(2)

    def enter_login_performance_glitch_user(self):
        """ вводим в поле поиска слово "Тензор": """
        name = "performance_glitch_user"
        password = "secret_sauce"
        user_name = self.browser.find_element(*BasePageLocators.INPUT_USER_NAME)
        user_name.send_keys(name)
        user_name.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        field_password = self.browser.find_element(*BasePageLocators.INPUT_PASSWORD)
        field_password.send_keys(password)
        field_password.send_keys(Keys.ENTER)  # нажимаем клавишу Enter
        button_login = self.browser.find_element(*BasePageLocators.BUTTON_LOGIN)
        button_login.click()
        # time.sleep(2)

    def sort_products_price_lohi(self):
        """ сортируем товары по цене снизу вверх: """
        btn = self.browser.find_element(*BasePageLocators.PRODUCT_SORT_CONTAINER)
        btn.click()
        time.sleep(2)
        btn = self.browser.find_element(*BasePageLocators.PRODUCT_SORT_CONTAINER_LOHI)
        btn.click()
        time.sleep(2)

    def sort_products_price_hilo(self):
        """ сортируем товары по цене снизу вверх: """
        btn = self.browser.find_element(*BasePageLocators.PRODUCT_SORT_CONTAINER)
        btn.click()
        time.sleep(2)
        btn = self.browser.find_element(*BasePageLocators.PRODUCT_SORT_CONTAINER_HILO)
        btn.click()
        time.sleep(2)

    def add_product_to_cart(self):
        """ добавляем товары в корзину: """
        btn = self.browser.find_element(*BasePageLocators.BUTTON_ADD_TO_CART)
        btn.click()
        time.sleep(5)

    def remove_from_cart(self):
        """ Удаляем товар из корзины: """
        btn = self.browser.find_element(*BasePageLocators.BUTTON_REMOVE_FROM_CART)
        btn.click()
        time.sleep(3)

    def should_be_shopping_cart_full(self):
        """ Проверка, что товар в корзине: """
        assert self.is_element_present(*BasePageLocators.SHOPPING_CART_BADGE), "SHOPPING CART IS EMPTY..."

    def should_be_shopping_cart_empty(self):
        """ Проверка, что корзина пуста: """
        assert self.is_not_element_present(*BasePageLocators.SHOPPING_CART_BADGE), "SHOPPING CART IS EMPTY..."


    def is_element_present(self, how, what):
        """
        Метод, в котором будем перехватывать исключение. В него будем передавать два аргумента:
        как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        Чтобы перехватывать исключение, нужна конструкция try/except:
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Абстрактный метод, который проверяет, ___ЧТО ЭЛЕМЕНТ НЕ ПОЯВЛЯЕТСЯ___
        на странице в течение заданного времени:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Метод, который проверяет, ___ЧТО ЭЛЕМЕНТ ИСЧЕЗАЕТ___
        Следует воспользоваться явным ожиданием вместе с функцией until_not,
        в зависимости от того, какой результат мы ожидаем:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """ Открытие браузера """
        self.browser.get(self.url)
