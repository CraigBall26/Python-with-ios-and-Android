from bus_app_android_main.bus_app_config import *


class open_app_splash:
    
    def deny_gps_button():
        return (driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button"))
    
    def allow_gps_button():
        return (driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))
    
class home_page:
    
    def allow_gps_button():
        return (driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))
    
    def deny_gps_button():
        return (driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button"))
    
    def do_not_ask_again_checkbox():
        return (driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox"))
    
    def browse_button():
        return (driver.find_element)
    
    def signup_or_login_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_home_login"))
    
    def open_hamburger_menu():
        return (driver.find_element_by_accessibility_id("Open"))
    
    def close_hamburger_menu():
        return (driver.find_element_by_accessibility_id("Close"))
    
    def login_for_my_account_menu():
        return (driver.find_element_by_id("com.oxford.bus:id/action_drawer_account"))
    
class login_or_signup_page():
    
    def signup_tab():
        return (driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]"))
    
    def get_started_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_button"))
    
    def enter_email():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_login_ed_address"))
    
    def enter_password():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_login_ed_password"))
    
    def login_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_login_button"))
    
class signup_process_email_page():
    
    def enter_email():
        return (driver.find_element_by_id("com.oxford.bus:id/view_password_input_layout"))
        
    def continue_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_email_button"))
    
class signup_process_name_page():
    
    def enter_firstname():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_name_first_name"))
    
    def enter_surname():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_name_surname"))
    
    def continue_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_name_button"))

class signup_process_password_page():
    
    def enter_password():
        return (driver.find_element_by_id("fragment_register_add_password_et"))
    
    def continue_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_password_button"))
    
class signup_process_age_verifcation():
    
    def under_16_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_negative"))
    
    def over_16_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_positive"))
    
    def next_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_button"))

class signup_process_promotions():
    
    def do_not_send_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_negative"))
    
    def do_send_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_positive"))
    
    def next_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_button"))

class signup_process_travel_updates():
    
    def do_not_send_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_negative"))
    
    def please_send_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_positive"))
    
    def next_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_add_news_button"))

class signup_process_terms_page():
    
    def agree_radio_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_terms_and_conditions_checkbox"))

    def next_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_terms_and_conditions_button"))

class confirm_signup_page():
    
    def complete_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_code_complete_button"))
    
    def resend_code():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_code_resend"))
    
    def code_input_1():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_code_1"))
    
    def code_input_2():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_code_2"))
    
    def code_input_3():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_code_3"))
    
    def code_input_4():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_code_4"))
    
    
class thanks_for_signing_up_page():
    
    def add_card_row():
        return(driver.find_element_by_id("com.oxford.bus:id/fragment_register_confirmation_add_card"))
               
    def add_paypal_row():
        return(driver.find_element_by_id("com.oxford.bus:id/fragment_register_confirmation_add_paypal"))
               
    def skip_row():
        return(driver.find_element_by_id("com.oxford.bus:id/fragment_register_confirmation_skip"))
               
        
class add_card_enter_number_page():
    
    def card_number_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_number_input"))
    
    def next_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_number_continue_button"))
    
class add_card_confirm_cvv_page():
    
    def card_number_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_confirm_number_input"))
    
    def next_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_confirm_button"))
    
    def ccv_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_confirm_cvv_input"))
    
    def name_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_confirm_name_input"))
    
    def month_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_monthspin"))
                
    def year_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_yearspin"))
    
class add_card_billing_address():
    
    def first_line_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_billing_street_input"))
    
    def town_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_billing_town_input"))
    
    def postcode_field():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_billing_post_input"))
    
    def done_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_credit_card_billing_button"))
    
class my_account_page():
    
    def login_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_my_account_logout_login_button"))
    
    def edit_personal_details():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_my_account_edit_details"))
    
    def edit_password():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_my_account_change_password"))
    
    def edit_payment_methods():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_my_account_edit_payment_methods"))
    
    def logout():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_my_account_logout"))
    
class payment_method_add():
    
    def add_new_method_button():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_payment_methods_add_button"))
    
    def add_card_row():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_payment_card"))
               
    def add_paypal_row():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_payment_paypal"))
    
    def add_gpay_row():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_add_google_pay")) 
    
    
    def skip_row():
        return (driver.find_element_by_id("com.oxford.bus:id/fragment_register_confirmation_skip"))
               
