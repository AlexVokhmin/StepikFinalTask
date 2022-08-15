from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'div.basket-mini .btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ALERT_ITEM_NAME_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages  div.alert:nth-child(1) > div.alertinner > strong')
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, '#messages  div.alert:nth-child(3) > div.alertinner > p > strong')

class BasketPageLocators():
    ITEMS = (By.CSS_SELECTOR, 'basket-items')
    NO_ITEMS_ALERT = (By.CSS_SELECTOR, 'div.content > #content_inner > p')