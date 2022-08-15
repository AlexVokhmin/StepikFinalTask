from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def compare_alert_item_name_with_item_name(self):
        alert_item_name = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_NAME_ADDED_IN_BASKET).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name == alert_item_name, f"Алерт после добавления товара в корзину не содержит имя товара. " \
                                             f"{item_name} != {alert_item_name}"

    def compare_alert_price_with_item_price(self):
        alert_basket_price = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price == alert_basket_price, f"Стоимость корзины в алерте не совпадает с ценой товара." \
                                                 f"{item_price} != {alert_basket_price}"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Отсутсвует кнопка добавления товара в корзину'

    def cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ITEM_NAME_ADDED_IN_BASKET)

    def success_message_desapered(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ITEM_NAME_ADDED_IN_BASKET)



