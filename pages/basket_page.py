from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage): 
    
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "В корзине есть товар(ы)!"

    def should_be_empty_basket_alert(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_ALERT), "Алерта о пустой корзине нет"