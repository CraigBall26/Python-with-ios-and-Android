import unittest
from config_pack import test_conf # 2. Get test specific config, must be next to test script (same directory)
from qatools.handlers.core_handler import CoreHandler  # 3. Import setup_test
handler = CoreHandler(test_conf, __file__)  # 4. setup the test using setup_test(config, __file__)
from android_flow_locators import *
from appium import webdriver
from selenium import webdriver as s_webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
from qatools.handlers.logging_handler import Logger  # 4. Import new_logger to access logging
from qatools.handlers.config_handler import ConfigHandler  # 5. Import ConfigHandler to access config in your test
log = Logger(__name__) .new_logger # 6. Create a new "logger" for your test script!


def get_loggin(self):
    login_page = admin_login_page_class()
    login_page.email().set(locators_stage['username'])
    login_page.password().set(locators_stage['password'])
    login_page.submit().click()
    dashboard_page = dashboard_page_class()
    dashboard_page.header_select().click()
    if dashboard_page.header_brands().is_element_visible():
        self.driver.find_element_by_css_selector(".header-select-item[id*='{}']".format(self.conf['brand'])).click()


def text_assert(text, text_location):
    try:
        if text != text_location:
            log.error("Text incorrect in element - '{}'".format(text_location))
    except Exception as e:
        log.error(str(e))
        log.error("Problem finding text in element - '{}'".format(text_location))


def element_assert(self, loc):
    try:
        if loc[0] == "xpath":
            self.driver.find_element_by_xpath(loc[1])
        else:
            self.driver.find_element_by_id(loc[1])
    except NoSuchElementException:
        log.error("ELEMENT NOT FOUND: {}".format(loc))
        return False
    return True


def login_account(self, method):
    if method == "Basket":
        basket_page = basket_page_class()
        basket_page.login().click()
    else:
        home_page = home_page_class()
        home_page.login().click()
    login_page = login_page_class()
    log.info("Logging in with account '{}'...".format(self.login))
    login_page.email().set(self.login)
    login_page.pwd().set(self.password)
    self.driver.hide_keyboard()
    login_page.btn_continue().click()
    if method == "Home":
        load_page_for_validation(
    elif method == "Basket":
        load_page_for_validation(payment_page_class)


def add_payment_card(self, card_number):
    self.MoP = card_number
    add_payment_page = add_payment_page_class()
    add_payment_page.add_btn().click()

    select_payment_page = select_payment_page_class()
    select_payment_page.select_card().click()

    add_card_page = add_card_page_class()
    add_card_page.number().set(self.MoP)
    add_card_page.continue_btn().click()

    add_card_details_page = add_card_details_page_class()
    add_card_details_page.cvv_number().set(test_data["cv2"])
    self.driver.hide_keyboard()
    add_card_details_page.name().set(locators_stage['customer_name_GTR'])
    self.driver.hide_keyboard()
    add_card_details_page.month().click()
    add_card_details_page.select_month().click()
    add_card_details_page.select_year().click()
    # add_card_details_page.continue_btn().click()

    add_billing_details_page = add_billing_details_page_class()
    add_billing_details_page.address().set(test_data["address"])
    self.driver.hide_keyboard()
    add_billing_details_page.town().set(test_data["towncity"])
    self.driver.hide_keyboard()
    add_billing_details_page.postcode().set(test_data["postcode"])
    self.driver.hide_keyboard()
    add_billing_details_page.continue_btn().click()
    log.info("Card number {} added to account '{}'".format(self.MoP, self.login))


def return_list_webelement(func):
    def wrapper(browser):
        elem_list = []
        find_elem = func(browser)
        while True:
            (x, y) = next(find_elem)
            if x is None:
                break
            else:
                elem_list.append((x, y))
        return elem_list
    return wrapper


@return_list_webelement
def count_live_buses(browser):
    my_journey_page = my_journey_page_class()
    elems = Element.try_get_element(browser.driver, my_journey_page.live_bus_icon().loc, True)
    if elems is not None:
        for elem in elems:
            if elem.size == live_bus_size:
                yield elem.location['x'], elem.location['y']
        yield None, None


@return_list_webelement
def count_bus_stops(browser):
    departure_page = departure_page_class()
    elems = Element.try_get_element(browser.driver, departure_page.bus_stop_icon().loc, True)
    if elems is not None:
        for elem in elems:
            if elem.size == bus_stop_size:
                yield elem.location['x'], elem.location['y']
        yield None, None


def count_purchased_tickets(self):
    wallet_page = wallet_page_class()
    if Element.test_element_is_present(self, wallet_page.purchased_tickets_quantity.loc):
        self.purchased_tickets_amount = wallet_page.purchased_tickets_quantity().text()
    else:
        self.purchased_tickets_amount = 0
    log.info("Purchased tickets in wallet: {}".format(self.purchased_tickets_amount))


def request_password_reset_email(self):
    login_page = login_page_class()
    login_page.email().set(self.login)
    login_page.pwd().set(locators_stage["incorrect_password"])
    self.driver.hide_keyboard()
    login_page.btn_continue().click()
    text_assert(locators_text["incorrect_password_modal_header"], login_page.error_modal_title().text())
    text_assert(locators_text["incorrect_password_modal_body"], login_page.error_modal_body().text())
    login_page.reset_p assword_button().click()

    password_reset_page = password_reset_page_class()
    text_assert(locators_text["reset_password_header"], password_reset_page.reset_password_title().text())
    text_assert(locators_text["reset_password_body"], password_reset_page.reset_password_body().text())
    text_assert(self.login, password_reset_page.email_field().text())
    password_reset_page.send_reset_code_button().click()


def check_live_bus_information_screen():
    live_bus_information_page = live_bus_information_page_class()
    bus_number = live_bus_information_page.bus_number().text()
    stop_name = live_bus_information_page.stop_name().text()
    if bus_number is not None and stop_name is not None:
        log.info("Bus number: '{}'".format(bus_number))
        log.info("Current stop: '{}'".format(stop_name))
        log.info("Live bus screen appears correctly")
        return True
    else:
        log.error("Live bus screen does not appear correctly")
        return False


def sign_up_account(self):
    signup_start()
    signup_enter_email(self)
    signup_enter_name(self)
    signup_enter_password(self)
    signup_select_news_option()
    signup_select_terms_and_conditions_option()
    log.info("New account signed up using email address '{}'".format(self.login))


def bus_stop_information_check(self):
    try:
        bus_stop_information_page = bus_stop_information_page_class()
        self.bus_stop_name = bus_stop_information_page.bus_stop_name().text()
        bus_travel_direction = bus_stop_information_page.bus_travel_direction().text()
        next_bus_number = bus_stop_information_page.next_bus_number().text()
        next_bus_destination = bus_stop_information_page.next_bus_destination().text()
        log.info("Bus stop information screen appears correctly")
        log.info("Bus stop selected: '{}'".format(self.bus_stop_name))
        log.info("{}".format(bus_travel_direction))
        log.info("Next bus number: '{}'".format(next_bus_number))
        log.info("Next bus destination: '{}'".format(next_bus_destination))
    except Exception as e:
        log.error(str(e))
        log.error("Bus stop information screen does not appear correctly")


def set_journey(self):
    journey_planner_page = journey_planner_page_class()
    journey_planner_page.location_from().click()
    journey_planner_page.origin().set(self.origin)
    self.driver.hide_keyboard()
    elems = Element.try_get_element(self.driver, journey_planner_page.select_route().loc, True)
    journey_planner_page.select_route().click()
    '''for elem in elems:
        if self.origin in elem.text:
            elem.click()
            break'''
    journey_planner_page.location_to().click()
    journey_planner_page.destination().set(self.destination)
    self.driver.hide_keyboard()
    elems = Element.try_get_element(self.driver, journey_planner_page.select_route().loc, True)
    journey_planner_page.select_route().click()
    '''for elem in elems:
        if self.destination in elem.text:
            elem.click()
            break'''


def add_journey_to_basket(self):
    home_page = home_page_class()
    home_page.general_menu().click()

    menu_page = menu_page_class()
    menu_page.journey_planner().click()
    set_journey(self)

    journey_option_page = journey_option_page_class()
    log.info("Bus number selected: {}".format(journey_option_page.fastest_bus().text()))
    journey_option_page.fastest_bus_layout().click()

    journey_option_layout_page = journey_option_layout_page_class()
    journey_option_layout_page.buy_ticket().click()

    crawley_group_page = crawley_group_page_class()
    crawley_group_page.adult_60_min().click()

    ticket_information_page = ticket_information_page_class()
    log.info("Ticket information: '{}'".format(ticket_information_page.ticket_details().text()))
    ticket_information_page.add_to_basket().click()


def activation_screen_check():
    activated_ticket_screen = activated_ticket_screen_class()
    brand = activated_ticket_screen.brand().text()
    ticket_type = activated_ticket_screen.ticket_type().text()
    time = activated_ticket_screen.time().text()
    remaining_time = activated_ticket_screen.remaining_time_counter().text()
    details = activated_ticket_screen.activation_details().text()
    log.info("Ticket activation screen appears correctly")
    log.info("Brand: '{}'".format(brand))
    log.info("Ticket: '{}'".format(ticket_type))
    log.info("Current time: '{}'".format(time))
    log.info("Remaining time on ticket: '{}'".format(remaining_time))
    log.info("Details:\n{}".format(details))


def pay_with_card(self):
    payment_page = payment_page_class()
    if locators_text["choose_payment_method"] in payment_page.stored_payment_method().text():
        log.info("No stored payment method found")
        payment_page.stored_payment_method().click()
        add_payment_card(self, self.MoP)
    else:
        card_number = payment_page.payment_card_number().text()
        payment_page.stored_payment_method().click()
        add_payment_page = add_payment_page_class()
        add_payment_page.stored_payment_method().click()
        log.info("Stored card ending in '{}' selected".format(card_number[-4:]))
    payment_page = payment_page_class()
    payment_page.buy_button().click()


def purchase_success_screen_check():
    purchase_success_screen = purchase_success_screen_class()
    ticket_brand = purchase_success_screen.ticket_brand().text()
    ticket_type = purchase_success_screen.ticket_type().text()
    log.info("Purchase successful")
    log.info("Ticket information")
    log.info("Brand: '{}'".format(ticket_brand))
    log.info("Ticket type: '{}'".format(ticket_type))


def activate_ticket(self, page):
    if page == "Purchase Success Screen":
        activate_ticket_purchase_success_screen(self)


def activate_ticket_purchase_success_screen(self):
    purchase_success_screen = purchase_success_screen_class()
    if Element.test_element_is_present(self, purchase_success_screen.activate_ticket_button.loc):
        log.info("Activating ticket...")
        purchase_success_screen.activate_ticket_button().click()
        purchase_success_screen.modal_activate_button().click()
        activation_screen_check()
    else:
        log.info("Unable to activate ticket")


def allow_app_permission():
    init_page = init_page_class()
    init_page.permission_allow().click()
    log.info("App permission granted")


def add_ticket_to_basket():
    home_page = home_page_class()
    home_page.browse_tickets().click()

    browse_page = browse_page_class()
    browse_page.crawley_group().click()

    crawley_group_page = crawley_group_page_class()
    crawley_group_page.adult_60_min().click()

    ticket_information_page = ticket_information_page_class()
    log.info("Ticket information: '{}'".format(ticket_information_page.ticket_details().text()))
    ticket_information_page.add_to_basket().click()


def signup_success_check(self):
    try:
        signup_success_page = signup_success_page_class()
        text_assert(locators_text["confirm_header"], signup_success_page.register_label().text())
        text_assert(locators_text["confirm_body"], signup_success_page.register_desc().text())
        log.info("'{}' signed up".format(self.login))
        log.info("Account activation code sent to '{}'".format(self.login))
        return True
    except:
        return False


def split_signup_code(self):
    self.signup_code_1 = self.signup_code[:1]
    self.signup_code_2 = self.signup_code[1:2]
    self.signup_code_3 = self.signup_code[2:3]
    self.signup_code_4 = self.signup_code[3:4]


def signup_code_entry(self, correct=True):
    if not correct:
        self.signup_code = "0000"
    split_signup_code(self)
    signup_success_page = signup_success_page_class()
    signup_success_page.code_entry_field_1().set(self.signup_code_1)
    signup_success_page.code_entry_field_2().set(self.signup_code_2)
    signup_success_page.code_entry_field_3().set(self.signup_code_3)
    signup_success_page.code_entry_field_4().set(self.signup_code_4)
    self.driver.hide_keyboard()
    signup_success_page.complete_sign_up_button().click()
    if not correct:
        load_page_for_validation(signup_success_page_class)
    else:
        load_page_for_validation(select_payment_page_class)


def navigate_home(from_page):
    if from_page == "Signup Success":
        signup_success_page = signup_success_page_class()
        signup_success_page.main_menu().click()

        menu_page = menu_page_class()
        menu_page.home_page().click()


def resend_confirmation_code(self):
    try:
        signup_success_page = signup_success_page_class()
        signup_success_page.resend_register().click()
        text_assert(locators_text["confirm_resend_modal_header"], signup_success_page.resend_confirm().text())
        if locators_text["confirm_resend_modal_body"] in signup_success_page.resend_message().text():
            signup_success_page.validate_resend().click()
        log.info("Confirmation code resent to '{}'".format(self.login))
        return True
    except:
        return False


def resend_password_check(self):
    try:
        forgotten_password_code_page = forgotten_password_code_page_class()
        text_assert(locators_text["confirm_password_reset_header"], forgotten_password_code_page.header().text())
        text_assert(locators_text["confirm_password_reset_body"], forgotten_password_code_page.body().text())
        log.info("Password reset code sent to '{}'".format(self.login))
        return True
    except:
        return False


def signup_enter_email(self, email=True):
    if not email:
        self.login = locators_stage["invalid_email"]
    signup_email_page = signup_email_page_class()
    signup_email_page.email().set(self.login)
    log.info("'{}' entered into Sign Up email field".format(self.login))
    self.driver.hide_keyboard()
    signup_email_page.btn_continue().click()
    load_page_for_validation(signup_name_page_class)


def signup_start():
    home_page = home_page_class()
    home_page.login().click()

    login_page = login_page_class()
    login_page.signup().click()

    signup_page = signup_page_class()
    text_assert(locators_text["sign_up_header"], signup_page.terms().text())
    text_assert(locators_text["sign_up_body"], signup_page.terms_label().text())
    signup_page.register().click()


def signup_enter_name(self, name=True):
    if not name:
        self.first_name = ""
        self.surname = ""
    signup_name_page = signup_name_page_class()
    signup_name_page.name().set(self.first_name)
    log.info("'{}' entered into First name field".format(self.first_name))
    signup_name_page.surname().set(self.surname)
    log.info("'{}' entered into Surname field".format(self.surname))
    self.driver.hide_keyboard()
    if signup_name_page.btn_continue().get("enabled") == "true":
        signup_name_page.btn_continue().click()
        load_page_for_validation(signup_pwd_page_class)


def page_validation(func):
    def wrapper(my_page):
        try:
            instance = my_page.__new__(my_page)
            return True
        except:
            return False
    return wrapper


@page_validation
def load_page_for_validation(my_page):
    return my_page


def signup_enter_password(self):
    signup_pwd_page = signup_pwd_page_class()
    signup_pwd_page.pwd().set(self.password)
    log.info("Password entered into Password field")
    self.driver.hide_keyboard()
    signup_pwd_page.btn_continue().click()
    load_page_for_validation(signup_news_page_class)


def signup_select_news_option():
    signup_news_page = signup_news_page_class()
    signup_news_page.no_emails().click()
    log.info("No news emails selected")
    signup_news_page.confirm().click()
    load_page_for_validation(signup_terms_page_class)


def signup_select_terms_and_conditions_option(tick=True):
    signup_terms_page = signup_terms_page_class()
    if not tick:
        if signup_terms_page.agree().get("checked") == "true":
            signup_terms_page.agree().click()
            log.info("Terms and Conditions checkbox is not checked")
    else:
        if signup_terms_page.agree().get("checked") == "false":
            signup_terms_page.agree().click()
            log.info("Terms and Conditions checkbox is checked")
    if signup_terms_page.confirm().get("enabled") == "true":
        signup_terms_page.confirm().click()
        load_page_for_validation(signup_success_page_class)


def pinch_map(func):
    def wrapper(browser):
        # todo to adapt for other webelements/iOS but not urgent
        positions = func(browser)
        return browser.driver.tap(positions, 10000)
    return wrapper

zoom_out = 500


@pinch_map
def pinch_google_map(browser):
    google_map = browser.driver.find_element_by_accessibility_id("Google Map")
    positions = []
    positions.append((google_map.location['x'] + google_map.size['width']/2,
                      google_map.location['y'] + google_map.size['height']/2))
    positions.append((positions[0][0]-zoom_out, positions[0][1]-zoom_out))
    return positions


class main_android_app(unittest.TestCase):

    conf = ConfigHandler().get_conf()

    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'automationName': 'uiautomator2',
                        'platformVersion': self.conf['android']['platformVersion'],
                        'deviceName': self.conf['android']['deviceName'],
                        'avd': self.conf['android']['deviceName'],
                        'app': return_path_to_app("apk/{}".format(self.conf['android']['app']))}

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.set_location(test_data[self.conf['brand']]['latitude'],
                                 test_data[self.conf['brand']]['longitude'],
                                 0)

        Page._set_cls_drivers(self.driver)
        Element._set_test_inheritance_func(check_element_inheritance)

        self.login = locators_stage["registered_email"]
        self.password = locators_stage["password_will_preston"]
        self.MoP = test_data["test_card"]
        self.bus_stop_name = None
        self.purchased_tickets_amount = None
        self.ticket_type_and_price = None
        self.second_login = None
        self.origin = test_data[self.conf['brand']]["test_location1"]
        self.destination = test_data[self.conf['brand']]["test_location2"]
        self.signup_code = None
        self.signup_code_1 = None
        self.signup_code_2 = None
        self.signup_code_3 = None
        self.signup_code_4 = None
        self.first_name = locators_stage["firstname"]
        self.surname = locators_stage["surname"]

    def tearDown(self):
        handler.update_results(self)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        handler.end_test()

    def test_android_1_sign_up_1(self):
        log.info("*********** Test 1 - Able to sign up with valid credentials ***********")
        self.login = get_email()
        allow_app_permission()
        sign_up_account(self)
        if signup_success_check(self):
            log.info("*********** Test 1 Passed! ***********")
        else:
            raise Exception

    def test_android_1_sign_up_2(self):
        log.info("*********** Test 1 - Unable to sign up with an invalid email address ***********")
        allow_app_permission()
        signup_start()
        if not signup_enter_email(self, False):
            log.info("'{}' is an invalid email and has not been accepted".format(self.login))
            log.info("*********** Test 1 Passed! ***********")
        else:
            log.error("'{}' is an invalid email but has been accepted".format(self.login))
            raise Exception

    def test_android_1_sign_up_3(self):
        log.info("*********** Test 1 - Unable to sign up new account with no name ***********")
        self.login = get_email()
        allow_app_permission()
        signup_start()
        signup_enter_email(self)
        if not signup_enter_name(self, False):
            log.info("No names entered and not allowed to continue with sign up process")
            log.info("*********** Test 1 Passed! ***********")
        else:
            log.error("No names entered but allowed to continue with sign up process")
            raise Exception

    def test_android_1_sign_up_4(self):
        log.info("*********** Test 1 - Unable to sign up account without ticking T&Cs tickbox ***********")
        self.login = get_email()
        allow_app_permission()
        signup_start()
        signup_enter_email(self)
        signup_enter_name(self)
        signup_enter_password(self)
        signup_select_news_option()
        if not signup_select_terms_and_conditions_option(False):
            log.info("Terms and Conditions box is not checked and not allowed to continue with sign up process")
            log.info("*********** Test 1 Passed! ***********")
        else:
            log.error("Terms and Conditions box is not checked but allowed to continue with sign up process")
            raise Exception

    def test_android_1_sign_up_5(self):
        log.info("*********** Test 1 - Unable to register an account using an email that is already registered ***********")
        allow_app_permission()
        signup_start()
        signup_enter_email(self)
        signup_enter_name(self)
        signup_enter_password(self)
        signup_select_news_option()
        if signup_select_terms_and_conditions_option():
            log.error("Able to sign up a new account using '{}' despite registered account using this email".
                      format(self.login))
            raise Exception
        else:
            log.info("Unable to sign up as there is already an account using '{}'".format(self.login))
            log.info("*********** Test 1 Passed! ***********")

    def test_android_1_sign_up_6(self):
        log.info("*********** Test 1 - Unable to confirm registered account using invalid confirmation code ***********")
        self.login = get_email()
        allow_app_permission()
        sign_up_account(self)
        signup_success_check(self)
        if not signup_code_entry(self, False):
            log.info("Unable to sign up new account using invalid activation code")
            log.info("*********** Test 1 Passed! ***********")
        else:
            log.error("Able to sign up new account using invalid activation code")
            raise Exception

    def test_android_1_sign_up_7(self):
        log.info("*********** Test 1 - Unable to log in with account that has been registered but not confirmed ***********")
        self.login = get_email()
        allow_app_permission()
        sign_up_account(self)
        signup_success_check(self)
        navigate_home("Signup Success")
        if not login_account(self, "Home"):
            log.info("Unable to log in with account that has not been activated")
            log.info("*********** Test 1 Passed! ***********")
        else:
            log.error("Able to log in with account that has not been activated")
            raise Exception

    def test_android_1_sign_up_8(self):
        log.info("*********** Test 1 - Confirm code can be resent ***********")
        self.login = get_email()
        allow_app_permission()
        sign_up_account(self)
        signup_success_check(self)
        if resend_confirmation_code(self):
            log.info("*********** Test 1 Passed! ***********")
        else:
            log.error("Confirmation code not resend to '{}'".format(self.login))
            raise Exception

    def test_android_2_browse_tickets(self):
        log.info("*********** Test 2 - Browse tickets ***********")
        allow_app_permission()
        add_ticket_to_basket()
        login_account(self, "Basket")
        pay_with_card(self)
        purchase_success_screen_check()
        activate_ticket(self, "Purchase Success Screen")
        log.info("*********** Test 2 Passed! ***********")

    def test_android_3_request_forgotten_password(self):
        log.info("*********** Test 3 - Request Forgotten Password ***********")
        allow_app_permission()
        request_password_reset_email(self)
        if resend_password_check(self):
            log.info("*********** Test 3 Passed! ***********")
        else:
            log.error("Password reset has not been requested")
            raise Exception

    def test_android_4_home_page_live_bus(self):
        # todo 4 NOT FINISHED - check_live_bus_information_screen
        # Also, set_location function isn't working.

        log.info("*********** Test 4 - Home Page Live Bus ***********")
        live_bus_list = []
        allow_app_permission()

        home_page = home_page_class()
        home_page.departure().click()

        departure_page = departure_page_class()
        pinch_google_map(self)
        # pinch_google_map(self)
        departure_page.my_journey_tab().click()

        # Test doesn't work beyond this point until Google Maps issue is solved

        my_journey_page = my_journey_page_class()

        live_bus_list = count_live_buses(self)
        log.info("Number of live bus: {}".format(len(live_bus_list)))
        self.driver.tap([live_bus_list[random.randint(0, len(live_bus_list)-1)]])

        if check_live_bus_information_screen():
            log.info("*********** Test 4 Passed! ***********")
        else:
            #log.error("*********** Test 4 Failed! ***********")
            raise Exception

    def test_android_5_explore_bus_stop(self):
        # todo 5 NOT FINISHED - bus_travel_direction problem

        log.info("*********** Test 5 - Online/offline into Explore - Bus stop ***********")
        bus_stop_list = []
        allow_app_permission()

        home_page = home_page_class()
        home_page.departure().click()

        departure_page = departure_page_class()
        bus_stop_list = count_bus_stops(self)
        log.info("Number of bus stops: {}".format(len(bus_stop_list)))
        self.driver.tap([bus_stop_list[random.randint(0, len(bus_stop_list)-1)]])

        #departure_page.bus_stop_icon().click()
        bus_stop_information_check(self)
        bus_stop_information_page = bus_stop_information_page_class()
        bus_stop_information_page.three_dot_icon().click()
        bus_stop_information_page.travel_to_here_selection().click()
        journey_planner_page = journey_planner_page_class()
        if self.bus_stop_name in journey_planner_page.location_to().text():
            log.info("{} appears in Destination field".format(self.bus_stop_name))
            log.info("*********** Test 5 Passed! ***********")
        else:
            log.error("'{}' does not appear in Destination field".format(self.bus_stop_name))
            log.error("*********** Test 5 Failed! ***********")
            raise Exception

    def test_android_6_send_ticket(self):

        # todo 6 TBC

        log.info("*********** Test 6 - Send ticket ***********")

    def test_android_7_tickets_on_different_device(self):


        # todo 7 NOT FINISHED

        log.info("*********** Test 5 - Tickets on different device ***********")
        self.login = locators_stage["registered_email"]
        allow_app_permission()
        login_account(self, "Home")
        add_journey_to_basket(self)

        payment_page = payment_page_class()
        payment_page.payment_method().click()
        add_payment_card(self, test_data["Visa_debit_no3DS"])

        # FINISH REST OF THE PAYMENT PROCESS HERE

        # SWITCH TO DEVICE B HERE

        allow_app_permission()
        login_account(self, "Home")
        home_page = home_page_class()
        home_page.general_menu().click()
        home_page.my_wallet_button().click()

        # CHECK FOR PURCHASED TICKET HERE

    def test_android_8_finding_bus_on_map(self):
        log.info("*********** Test 8 - Finding bus on map ***********")
        allow_app_permission()

        home_page = home_page_class()
        home_page.departure().click()
        pinch_google_map(self)
        pinch_google_map(self)
        departure_page = departure_page_class()
        departure_page.my_journey_tab().click()

        my_journey_page = my_journey_page_class()
        count_live_buses(self)
        my_journey_page.live_bus_icon().click()
        if live_bus_information_page_class():
            log.info("*********** Test 8 Passed! ***********")
        else:
            # log.error("*********** Test 8 Failed! ***********")
            raise Exception

    def test_android_9_journey_planner(self):
        log.info("*********** Test 9 - Journey Planner ***********")
        self.login = locators_stage["registered_email"]
        allow_app_permission()
        add_journey_to_basket(self)
        login_account(self, "Basket")
        pay_with_card(self)
        purchase_success_screen_check()
        activate_ticket(self, "Purchase Success Screen")
        log.info("*********** Test 9 Passed! ***********")

    def test_android_10_send_ticket(self):

        # todo 10 This test can only work if a purchase is made at the start of the automation test.
        # Waiting on test payment method.

        log.info("*********** Test 10 - Send Ticket ***********")
        allow_app_permission()
        login_account(self, "Home")

        home_page = home_page_class()
        home_page.wallet_banner_bottom().click()

        wallet_page = wallet_page_class()
        count_purchased_tickets(self)
        wallet_page.purchased_ticket().click()

        send_ticket_information_page = send_ticket_information_page_class()
        self.ticket_type_and_price = send_ticket_information_page.ticket_type_and_price().text()
        log.info("Ticket: '{}'".format(self.ticket_type_and_price))
        send_ticket_information_page.send_ticket_button().click()

        send_tickets_page = send_tickets_page_class()
        send_tickets_page.send_via_email_button().click()

        confirm_recipient_page = confirm_recipient_page_class()
        confirm_recipient_page.edit_recipient_details_button().click()

        recipients_email_address_page = recipients_email_address_page_class()
        recipients_email_address_page.email_address_field().set(self.second_login, True)

        confirm_recipient_page = confirm_recipient_page_class()
        text_assert(self.second_login, confirm_recipient_page.recipient_email().text())
        confirm_recipient_page.confirm_and_send_button().click()

        ticket_sent_page = ticket_sent_page_class()
        ticket_sent_page.return_to_my_wallet_button().click()
        old_purchased_tickets_amount = self.purchased_tickets_amount
        count_purchased_tickets(self)
        if old_purchased_tickets_amount != self.purchased_tickets_amount:
            log.info("Ticket removed from account belonging to {} and has been sent to {}".format(self.login, self.second_login))
            log.info("*********** Test 10 Passed! ***********")
        else:
            log.error("Ticket has not been removed from account belonging to {}".format(self.login))
            raise Exception

    def test_oxford_11_activate_night_owl_early(self):

        # Not completed

        log.info("*********** Test 11 - Activate Night Owl Early ***********")
        self.login = locators_stage["registered_email"]
        self.origin = "Oxford"
        self.destination = "London"
        log.info("Email used for test: '{}'".format(self.login))
        init_page = init_page_class()
        init_page.permission_allow().click()

        home_page = home_page_class()
        home_page.login().click()

        login_account(self)

        add_journey_to_basket(self)

        payment_page = payment_page_class()
        payment_page.payment_method().click()

        add_payment_card(self, test_data["Visa_debit_no3DS"])

        # FINISH REST OF PAYMENT PROCESS

        home_page = home_page_class()
        home_page.general_menu().click()
        home_page.my_wallet_button().click()

        wallet_page = wallet_page_class()
        wallet_page.expired_tickets_button().click()

    def test_android_12_allow_tickets_to_expire(self):

        # todo 12 TBC

        log.info("*********** Test 12 - Allow ticket to expire ***********")

    def test_android_13_hotlist_active_ticket(self):
        # todo 13 NOT FINISHED - hotlist
        log.info("*********** Test 13 - Hotlist active ticket ***********")
        log.info("Email used for test: '{}'".format(self.login))
        allow_app_permission()
        login_account(self, "Home")
        add_journey_to_basket(self)
        pay_with_card(self)
        purchase_success_screen_check()
        # activate_ticket(self, "Purchase Success Screen")

        admin_page = busapp_admin_web(self.conf)
        admin_page.test_hotlist_ticket()
        time.sleep(300)

        home_page = home_page_class()
        home_page.general_menu().click()
        home_page.my_wallet_button().click()

        wallet_page = wallet_page_class()
        wallet_page.expired_tickets_button().click()

        # CHECK TICKET HAS EXPIRED

    def test_android_14_logout_multi_app(self):

        # todo 14 TBC

        log.info("*********** Test 14 - Log out Multi app ***********")

    def test_android_10(self):
        log.info("*********** Test 10 - Send Ticket ***********")
        self.login = locators_stage["craig_email_first"]
        self.second_login = locators_stage["craig_email_second"]
        self.password = locators_stage["password"]
        init_page = init_page_class()
        init_page.permission_allow().click()

        home_page = home_page_class()
        home_page.login().click()

        login_account(self)

        home_page = home_page_class()
        home_page.wallet_banner_bottom().click()

        wallet_page = wallet_page_class()
        count_purchased_tickets(self)
        wallet_page.purchased_ticket().click()

        send_ticket_information_page = send_ticket_information_page_class()
        self.ticket_type_and_price = send_ticket_information_page.ticket_type_and_price().text()
        log.info("Ticket: '{}'".format(self.ticket_type_and_price))
        send_ticket_information_page.send_ticket_button().click()

        send_tickets_page = send_tickets_page_class()
        send_tickets_page.send_via_email_button().click()

        confirm_recipient_page = confirm_recipient_page_class()
        confirm_recipient_page.edit_recipient_details_button().click()

        recipients_email_address_page = recipients_email_address_page_class()
        recipients_email_address_page.email_address_field().set(self.second_login, True)

        confirm_recipient_page = confirm_recipient_page_class()
        text_assert(self.second_login, confirm_recipient_page.recipient_email().text())
        confirm_recipient_page.confirm_and_send_button().click()

        ticket_sent_page = ticket_sent_page_class()
        ticket_sent_page.return_to_my_wallet_button().click()
        old_purchased_tickets_amount = self.purchased_tickets_amount
        count_purchased_tickets(self)
        if old_purchased_tickets_amount != self.purchased_tickets_amount:
            log.info("Ticket removed from account belonging to {} and has been sent to {}".format(self.login, self.second_login))
            log.info("*********** Test 10 Passed! ***********")
        else:
            log.error("Ticket has not been removed from account belonging to {}".format(self.login))
            raise Exception


class busapp_admin_web():

    def __init__(self, conf):
        self.conf = conf
        if conf["run"] == 'local':
            self.driver = s_webdriver.Chrome()
            # self.driver = s_webdriver.Firefox()
            # self.driver = s_webdriver.Safari()


        Page._set_cls_drivers(self.driver)
        Element._set_test_inheritance_func(check_element_inheritance)
        self.driver.get('https://admin-staging.otrl-bus.io/dashboard')
        self.driver.maximize_window()

    def tearDown(self):
        """ This is a function that runs after each test case. You should include actions you want to complete after
        every test is finished (regardless of result). Having this function with the call to handler.update_results(self)
        is mandatory (required for ensuring test results are written as expected)"""
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        """ Like tearDown but runs once after the test class (after all test cases), this is mandatory. This
        is the bit that collates all of the test results and has them written to file(s) """
        handler.end_test()

    def test_hotlist_ticket(self):
        get_loggin(self)
        dashboard_page = dashboard_page_class()
        dashboard_page.customers().click()
        customer_page = customer_page_class()
        customer_page.customer_search().set("will.preston@ontrackretail.co.uk")
        customer_page.customer_search_completion().click()
        customer_page.active_tickets_tab().click()
        customer_page.edit_tickets().click()
        customer_page.select_first_ticket_inlist().click()
        customer_page.validate_selection().click()

        # page validation
        hotlisting_page = hotlisting_page_class()
        hotlisting_page.hotlisting_reason().select_by_text("Refunded ticket")
        hotlisting_page.hotlisting_details().set(
            "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
            "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
            "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
            "1234567890")
        hotlisting_page.hotlisting_validation().click()

        # log-out
        '''customer_page = customer_page_class()
        customer_page.logout_button().click()'''


if __name__ == '__main__':
    test_loader = unittest.TestLoader()

    test_names = test_loader.getTestCaseNames(main_android_app)
    # ****************************************************

    test_names = [
                  "test_android_13_hotlist_active_ticket"]

    # test_names = [test_android_10,
    # test_android_1_sign_up_1,
    # test_android_1_sign_up_2,
    # test_android_1_sign_up_3,
    # test_android_1_sign_up_4,
    # test_android_1_sign_up_5,
    # test_android_1_sign_up_6, test_android_1_sign_up_7,
    # test_android_1_sign_up_8,
    # test_android_2_browse_tickets,
    # test_android_4_home_page_live_bus,
    # test_android_8_finding_bus_on_map,
    # test_android_9_journey_planner,
    # test_android_10

    # ****************************************************
    suite = unittest.TestSuite()
    for test_name in test_names:
        suite.addTest(main_android_app(test_name))
    result = unittest.TextTestRunner().run(suite)
