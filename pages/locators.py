from selenium.webdriver.common.by import By


class BasePageLocators():
    INPUT_USER_NAME = (By.CSS_SELECTOR, "#user-name")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "#login-button")
    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, ".product_sort_container")
    PRODUCT_SORT_CONTAINER_LOHI = (By.CSS_SELECTOR, "[value = lohi]")
    PRODUCT_SORT_CONTAINER_HILO = (By.CSS_SELECTOR, "[value = hilo]")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BUTTON_REMOVE_FROM_CART = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")






    # INPUT_BOX = (By.CSS_SELECTOR, "input.input__control.input__input.mini-suggest__input")
    # INPUT_BOX_SUGGEST_LIST = (By.CSS_SELECTOR, "input[aria-activedescendant^='suggest-list']")
    # ID_SEARCH_RESULTS = (By.CSS_SELECTOR, "li#search-results")
    # LINK_SEARCH_RESULT = (By.CSS_SELECTOR, "a[href^='https://tensor.ru']")
    # DATA_CID_1 = (By.CSS_SELECTOR, 'li[data-cid="1"] a[href^="https://tensor.ru"]')
    # DATA_CID_2 = (By.CSS_SELECTOR, 'li[data-cid="2"] a[href^="https://tensor.ru"]')
    # DATA_CID_3 = (By.CSS_SELECTOR, 'li[data-cid="3"] a[href^="https://tensor.ru"]')
    # DATA_CID_4 = (By.CSS_SELECTOR, 'li[data-cid="4"] a[href^="https://tensor.ru"]')
    # DATA_CID_5 = (By.CSS_SELECTOR, 'li[data-cid="5"] a[href^="https://tensor.ru"]')
    #
    # LINK_SEARCH_IMAGES = (By.CSS_SELECTOR, 'a[href^="https://yandex.ru/images"')
    # LINK_CATEGORY_0 = (By.CSS_SELECTOR, 'div.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    # TEXT_CATEGORY_0 = (By.CSS_SELECTOR, 'div.PopularRequestList-SearchText')
    # TEXT_SEARCH_0 = (By.CSS_SELECTOR, 'head title')
    # LINK_IMAGE_0 = (By.CSS_SELECTOR, '.serp-item_pos_0')
    # CIRCLEBUTTON_TYPE_NEXT = (By.CSS_SELECTOR, '.CircleButton_type_next')
    # CIRCLEBUTTON_TYPE_PREV = (By.CSS_SELECTOR, '.CircleButton_type_prev')
