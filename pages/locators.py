from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[value='Register']")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")
    BASKET_TOTAL_MSG = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
