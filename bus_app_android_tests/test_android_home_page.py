import pytest
from bus_app_flow_locators.android_flow_locators import *
from bus_app_android_main.bus_app_config import *
from selenium.webdriver.support.expected_conditions import _find_element
from bus_app_android_main import bus_app_config
import time
from selenium.common.exceptions import ElementNotVisibleException
from math import log
import logging
import threading
import time
import logging

def test_click_deny_button(): #py.test test_android_home_page.py -k 'test_click_deny_button'
    
    generated_email = bus_app_config.get_random_email()
    open_app_splash.deny_gps_button().click()
    home_page.deny_gps_button().click()
    home_page.signup_or_login_button().click()
    login_or_signup_page.signup_tab().click()
    login_or_signup_page.get_started_button().click()
    driver.set_value(signup_process_email_page.enter_email(), generated_email)
    signup_process_email_page.continue_button().click()
    driver.set_value(signup_process_name_page.enter_firstname(), bus_app_config.firstname)
    driver.set_value(signup_process_name_page.enter_surname(), bus_app_config.surname)
    signup_process_name_page.continue_button().click()
    driver.set_value(signup_process_password_page.enter_password(), bus_app_config.password)
    signup_process_password_page.continue_button().click()
    signup_process_age_verifcation.over_16_radio_button().click()
    signup_process_age_verifcation.next_button().click()
    signup_process_promotions.do_send_radio_button().click()
    signup_process_promotions.next_button().click()
    signup_process_travel_updates.please_send_radio_button().click()
    signup_process_travel_updates.next_button().click()
    signup_process_terms_page.agree_radio_button().click()
    signup_process_terms_page.next_button().click()
    time.sleep(5)
    get_code = bus_app_config.get_signup_code(generated_email)
    driver.set_value(confirm_signup_page.code_input_1(), get_code[0])
    confirm_signup_page.code_input_2().clear()
    driver.set_value(confirm_signup_page.code_input_2(), get_code[1])
    confirm_signup_page.code_input_3().clear()
    driver.set_value(confirm_signup_page.code_input_3(), get_code[2])
    confirm_signup_page.code_input_4().clear()
    driver.set_value(confirm_signup_page.code_input_4(), get_code[3])
    confirm_signup_page.complete_button().click()
    thanks_for_signing_up_page.add_card_row().click()
    driver.set_value(add_card_enter_number_page.card_number_field(), "4111111111111111")
    add_card_enter_number_page.next_button().click()
    driver.set_value(add_card_confirm_cvv_page.ccv_field(), "368")
    driver.set_value(add_card_confirm_cvv_page.name_field(), "mr craig ball")
    driver.hide_keyboard()
    add_card_confirm_cvv_page.month_field().click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[7]").click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()
    #add_card_confirm_cvv_page.next_button().click()
    driver.set_value(add_card_billing_address.first_line_field(), "117 test")
    driver.set_value(add_card_billing_address.town_field(), "london")
    driver.hide_keyboard()
    driver.set_value(add_card_billing_address.postcode_field(), "sw11ad")
    driver.keyevent(66)
    add_card_billing_address.done_button().click()
    time.sleep(6)
    bus_app_config.get_method_added_email(generated_email)
    time.sleep(4)
    assert driver.find_element_by_id("com.oxford.bus:id/view_buses_row_text_top_label")
    home_page.open_hamburger_menu().click()
    home_page.login_for_my_account_menu().click()
    my_account_page.logout().click()
    home_page.deny_gps_button().click()
    assert home_page.signup_or_login_button()
 
    


    