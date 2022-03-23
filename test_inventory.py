from pages.base_page import BasePage


def test_inventory_standard_user(browser):
    """
    ПРОВЕРКА на https://www.saucedemo.com/inventory.html.
    1) Зайти на главную https://www.saucedemo.com
    # 2)	Зайти под разными пользователями на сайт (standard_user, locked_out_user, problem_user, performance_glitch_user)
    2) Зайти под пользователем standard_user (locked_out_user, problem_user, performance_glitch_user)
    3) Отсортировать товары по возростанию цены
    4) Отсортировать товары по уменьшению цены
    5) Добавить любой товар в корзину
    6) Проверить, что тавар попал в корзину
    6) Удалить товар из корзины
    """
    link = 'https://www.saucedemo.com/'
    page = BasePage(browser, link)
    page.open()
    page.enter_login_standard_user()
    page.sort_products_price_lohi()
    page.sort_products_price_hilo()
    page.add_product_to_cart()
    page.should_be_shopping_cart_full()
    page.remove_from_cart()
    page.should_be_shopping_cart_empty()


def test_inventory_locked_out_user(browser):
    """
    ПРОВЕРКА на https://www.saucedemo.com/inventory.html.
    1) Зайти на главную https://www.saucedemo.com
    2) Зайти под пользователем locked_out_user
    3) Отсортировать товары по возростанию цены
    4) Отсортировать товары по уменьшению цены
    5) Добавить любой товар в корзину
    6) Проверить, что тавар попал в корзину
    6) Удалить товар из корзины
    """
    link = 'https://www.saucedemo.com/'
    page = BasePage(browser, link)
    page.open()
    page.enter_login_locked_out_user()
    page.sort_products_price_lohi()
    page.sort_products_price_hilo()
    page.add_product_to_cart()
    page.should_be_shopping_cart_full()
    page.remove_from_cart()
    page.should_be_shopping_cart_empty()


def test_inventory_problem_user(browser):
    """
    ПРОВЕРКА на https://www.saucedemo.com/inventory.html.
    1) Зайти на главную https://www.saucedemo.com
    2) Зайти под пользователем problem_user
    3) Отсортировать товары по возростанию цены
    4) Отсортировать товары по уменьшению цены
    5) Добавить любой товар в корзину
    6) Проверить, что тавар попал в корзину
    6) Удалить товар из корзины
    """
    link = 'https://www.saucedemo.com/'
    page = BasePage(browser, link)
    page.open()
    page.enter_login_problem_user()
    page.sort_products_price_lohi()
    page.sort_products_price_hilo()
    page.add_product_to_cart()
    page.should_be_shopping_cart_full()
    page.remove_from_cart()
    page.should_be_shopping_cart_empty()

def test_inventory_performance_glitch_user(browser):
    """
    ПРОВЕРКА на https://www.saucedemo.com/inventory.html.
    1) Зайти на главную https://www.saucedemo.com
    2) Зайти под пользователем performance_glitch_user
    3) Отсортировать товары по возростанию цены
    4) Отсортировать товары по уменьшению цены
    5) Добавить любой товар в корзину
    6) Проверить, что тавар попал в корзину
    6) Удалить товар из корзины
    """
    link = 'https://www.saucedemo.com/'
    page = BasePage(browser, link)
    page.open()
    page.enter_login_performance_glitch_user()
    page.sort_products_price_lohi()
    page.sort_products_price_hilo()
    page.add_product_to_cart()
    page.should_be_shopping_cart_full()
    page.remove_from_cart()
    page.should_be_shopping_cart_empty()