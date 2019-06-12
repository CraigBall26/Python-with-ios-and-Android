
from qatools.pageobjects.element import Element
from qatools.pageobjects.page import Page
from otrl_utils import *
from config_pack import test_conf
from admin_flow_locators import *

app_id = test_conf['app_id']


class init_page_class(Page):
    def check_on_load(self):
        return [init_page_class.permission_allow,
                ]

    class permission_allow(Element):
        loc = "id", "com.android.packageinstaller:id/permission_allow_button"


class home_page_class(Page):
    def check_on_load(self):
        return [home_page_class.browse_tickets,
                home_page_class.general_menu,
                home_page_class.departure,
                ]

    class browse_tickets(Element):
        loc = "id", "{}fragment_home_browse_tickets_button".format(app_id)

    class departure(Element):
        loc = "id", "{}fragment_home_departures_button".format(app_id)

    class login(Element):
        loc = "id", "{}fragment_home_login".format(app_id)

    class general_menu(Element):
        loc = "class name", "android.widget.ImageButton"

    class wallet_banner_bottom(Element):
        loc = "id", "{}fragment_home_my_wallet_status".format(app_id)

    class journey_planner_button(Element):
        loc = "id", "{}action_drawer_plan_journey_location".format(app_id)

    class my_wallet_button(Element):
        loc = "id", "{}action_drawer_my_tickets".format(app_id)

    class google_map(Element):
        #loc = "xpath", "//android.view.View[@content-desc='Google Map']"
        loc = "id", "{}fragment_explore_map".format(app_id)

class departure_page_class(Page):
    def check_on_load(self):
        return [
            departure_page_class.my_journey_tab,
        ]

    class my_journey_tab(Element):
        loc = "xpath", "//android.widget.TextView[@text='MY JOURNEY']"

    class google_map(Element):
        #loc = "xpath", "//android.view.View[@content-desc='Google Map']"
        loc = "id", "{}fragment_explore_map".format(app_id)

    class bus_stop_icon(Element):
        loc = "class name", "android.view.View"


class browse_page_class(Page):
    def check_on_load(self):
        return [browse_page_class.crawley_group,
                ]

    class crawley_group(Element):
        loc = "id", "{}view_ticket_group_layout".format(app_id)


class crawley_group_page_class(Page):
    def check_on_load(self):
        return [crawley_group_page_class.adult_60_min,
                ]

    class adult_60_min(Element):
        loc = "id", "{}view_buses_row_container".format(app_id)


class ticket_information_page_class(Page):
    def check_on_load(self):
        return [ticket_information_page_class.add_to_basket,
                ]

    class ticket_details(Element):
        loc = "id", "{}fragment_ticket_information_subtitle".format(app_id)

    class add_to_basket(Element):
        loc = "id", "{}view_buses_button_layout".format(app_id)


class basket_page_class(Page):
    def check_on_load(self):
        return [basket_page_class.login,
                ]

    class login(Element):
        loc = "id", "{}fragment_checkout_logout_login".format(app_id)


class payment_page_class(Page):
    def check_on_load(self):
        return [payment_page_class.payment_method,
                ]

    class payment_method(Element):
        loc = "id", "{}fragment_checkout_preferred_option".format(app_id)

    class stored_payment_method(Element):
        loc = "id", "{}view_buses_row_text_top_label".format(app_id)

    class buy_button(Element):
        loc = "id", "{}fragment_journey_options_buy_button".format(app_id)

    class payment_card_number(Element):
        loc = "id", "{}view_buses_row_text_top_label".format(app_id)


class add_payment_page_class(Page):
    def check_on_load(self):
        return [add_payment_page_class.add_btn,
                ]

    class add_btn(Element):
        loc = "id", "{}fragment_payment_methods_add_button".format(app_id)

    class stored_payment_method(Element):
        loc = "id", "{}view_buses_row_container".format(app_id)


class select_payment_page_class(Page):
    def check_on_load(self):
        return [select_payment_page_class.select_card,
                ]

    class select_card(Element):
        loc = "id", "{}fragment_add_payment_card".format(app_id)


class add_card_page_class(Page):
    def check_on_load(self):
        return [add_card_page_class.number,
                add_card_page_class.continue_btn,
                ]

    class number(Element):
        loc = "xpath", "//TextInputLayout[@text='Card number']//android.widget.EditText"

    class continue_btn(Element):
        loc = "id", "{}fragment_add_credit_card_number_continue_button".format(app_id)


class add_card_details_page_class(Page):
    def check_on_load(self):
        return [
                add_card_details_page_class.cvv_number,
                add_card_details_page_class.name,
                add_card_details_page_class.month,
                add_card_details_page_class.year,
                add_card_details_page_class.continue_btn,
                ]

    class cvv_number(Element):
        loc = "xpath", "//TextInputLayout[@text='CCV number']//android.widget.EditText"

    class name(Element):
        loc = "xpath", "//TextInputLayout[@text='Name on card']//android.widget.EditText"

    class month(Element):
        loc = "xpath", "//TextInputLayout[@text='Month']//android.widget.EditText"

    class select_month(Element):
        loc = "xpath", "//android.widget.TextView[@text={}]".format(test_data["expiryMonth"])

    class year(Element):
        loc = "xpath", "//TextInputLayout[@text='Year']//android.widget.EditText"

    class select_year(Element):
        loc = "xpath", "//android.widget.TextView[@text={}]".format(test_data["expiryYear"])

    class continue_btn(Element):
        loc = "id", "{}view_buses_button_layout".format(app_id)


class add_billing_details_page_class(Page):
    def check_on_load(self):
        return [
            add_billing_details_page_class.address,
            add_billing_details_page_class.town,
            add_billing_details_page_class.postcode,
            add_billing_details_page_class.continue_btn,
        ]

    class address(Element):
        loc = "xpath", "//TextInputLayout[@text='First line of address']//android.widget.EditText"

    class town(Element):
        loc = "xpath", "//TextInputLayout[@text='Town']//android.widget.EditText"

    class postcode(Element):
        loc = "xpath", "//TextInputLayout[@text='Postcode']//android.widget.EditText"

    class continue_btn(Element):
        loc = "id", "{}fragment_add_credit_card_billing_button".format(app_id)


class login_page_class(Page):
    def check_on_load(self):
        return [
                login_page_class.email,
                login_page_class.pwd,
                login_page_class.signup,
                ]

    class email(Element):
        loc = "xpath", "//TextInputLayout[@text='Email address']//android.widget.EditText"

    class pwd(Element):
        loc = "xpath", "//TextInputLayout[@text='Password']//android.widget.EditText"

    class btn_continue(Element):
        loc = "id", "{}view_buses_button_layout".format(app_id)

    class signup(Element):
        loc = "xpath", "//android.widget.TextView[@text='SIGN UP']"

    class error_modal_title(Element):
        loc = "id", "{}alertTitle".format(app_id)

    class error_modal_body(Element):
        loc = "id", "android:id/message"

    class reset_password_button(Element):
        loc = "id", "android:id/button1"


class signup_page_class(Page):
    def check_on_load(self):
        return [
                signup_page_class.terms,
                signup_page_class.terms_label,
                signup_page_class.register,
                ]

    class terms(Element):
        loc = "id", "{}fragment_register_terms_title".format(app_id)

    class terms_label(Element):
        loc = "id", "{}fragment_register_terms_label".format(app_id)

    class register(Element):
        loc = "id", "{}fragment_register_button".format(app_id)


class signup_email_page_class(Page):
    def check_on_load(self):
        return [signup_email_page_class.email,
                signup_email_page_class.btn_continue,
                ]

    class email(Element):
        loc = "xpath", "//android.widget.EditText"

    class btn_continue(Element):
        loc = "id", "{}fragment_register_add_email_button".format(app_id)

    class error_text(Element):
        loc = "id", "{}textinput_error".format(app_id)

class signup_name_page_class(Page):
    def check_on_load(self):
        return [signup_name_page_class.name,
                signup_name_page_class.surname,
                signup_name_page_class.btn_continue,
                ]

    class name(Element):
        loc = "xpath", "//TextInputLayout[@text='First name']//android.widget.EditText"

    class surname(Element):
        loc = "xpath", "//TextInputLayout[@text='Surname']//android.widget.EditText"

    class btn_continue(Element):
        loc = "id", "{}view_buses_button_layout".format(app_id)


class signup_pwd_page_class(Page):
    def check_on_load(self):
        return [signup_pwd_page_class.pwd,
                signup_pwd_page_class.btn_continue,
                ]

    class pwd(Element):
        loc = "xpath", "//TextInputLayout[@text='Password']//android.widget.EditText"

    class btn_continue(Element):
        loc = "id", "{}fragment_register_add_password_button".format(app_id)


class signup_news_page_class(Page):
    def check_on_load(self):
        return [signup_news_page_class.no_emails,
                signup_news_page_class.confirm,
                ]

    class no_emails(Element):
        loc = "id", "{}fragment_register_add_news_negative".format(app_id)

    class confirm(Element):
        loc = "id", "{}fragment_register_add_news_button".format(app_id)


class signup_terms_page_class(Page):
    def check_on_load(self):
        return [signup_terms_page_class.agree,
                signup_terms_page_class.confirm,
                ]

    class agree(Element):
        loc = "id", "{}fragment_register_terms_and_conditions_checkbox".format(app_id)

    class confirm(Element):
        loc = "id", "{}fragment_register_terms_and_conditions_button".format(app_id)


class signup_success_page_class(Page):
    def check_on_load(self):
        return [signup_success_page_class.register_label,
                signup_success_page_class.register_desc,
                ]

    class register_label(Element):
        loc = "id", "{}fragment_register_email_header_label".format(app_id)

    class register_desc(Element):
        loc = "id", "{}fragment_register_email_header_description".format(app_id)

    class resend_register(Element):
        loc = "id", "{}fragment_register_code_resend".format(app_id)

    class resend_confirm(Element):
        loc = "id", "{}alertTitle".format(app_id)

    '''class resend_message(Element):
        loc = "id", "{}message".format(app_id)
    class validate_resend(Element):
        loc = "id", "{}button1".format(app_id)'''

    class main_menu(Element):
        loc = "xpath", "//android.widget.ImageButton[@content-desc='Open']"

    class resend_message(Element):
        loc = "id", "android:id/message"

    class validate_resend(Element):
        loc = "id", "android:id/button1"

    class code_entry_field_1(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}fragment_register_code_1']" \
                       "//android.widget.EditText".format(app_id)

    class code_entry_field_2(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}fragment_register_code_2']" \
                       "//android.widget.EditText".format(app_id)

    class code_entry_field_3(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}fragment_register_code_3']" \
                       "//android.widget.EditText".format(app_id)

    class code_entry_field_4(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}fragment_register_code_4']" \
                       "//android.widget.EditText".format(app_id)

    class complete_sign_up_button(Element):
        loc = "id", "{}fragment_register_code_complete_button".format(app_id)

    class snackbar(Element):
        loc = "id", "{}snackbar_text".format(app_id)


class menu_page_class(Page):
    def check_on_load(self):
        return [menu_page_class.home_page,
                menu_page_class.journey_planner,
                ]

    class home_page(Element):
        loc = "id", "{}action_drawer_home".format(app_id)

    class journey_planner(Element):
        loc = "xpath", "//android.widget.TextView[@text='Journey Planner']"


class journey_planner_page_class(Page):
    def check_on_load(self):
        return [journey_planner_page_class.location_from,
                journey_planner_page_class.location_to,
                ]

    class location_from(Element):
        loc = "id", "{}view_journey_search_from".format(app_id)

    class origin(Element):
        loc = "xpath", "//android.widget.EditText[@text='Search origin']"

    class location_to(Element):
        loc = "id", "{}view_journey_search_to".format(app_id)

    class destination(Element):
        loc = "xpath", "//android.widget.EditText[@text='Search destination']"

    class select_route(Element):
        loc = "id", "{}view_journey_search_item_name".format(app_id)

    class select_route_completion(Element):
        loc = "id", "{}view_journey_search_item_info_layout".format(app_id)

    class journey_option(Element):
        loc = "id", "{}view_journey_option_layout".format(app_id)


class journey_option_page_class(Page):
    def check_on_load(self):
        return [journey_option_page_class.fastest_bus,
                journey_option_page_class.fastest_bus_layout,
                ]

    class fastest_bus(Element):
        loc = "id", "{}view_journey_option_bus_route".format(app_id)

    class fastest_bus_layout(Element):
        loc = "id", "{}view_journey_option_layout".format(app_id)


class journey_option_layout_page_class(Page):
    def check_on_load(self):
        return [
            journey_option_layout_page_class.buy_ticket,
                ]

    class buy_ticket(Element):
        loc = "id", "{}fragment_journey_options_map_buy_button".format(app_id)


class wallet_page_class(Page):
    def check_on_load(self):
        return [wallet_page_class.expired_tickets_button,
                wallet_page_class.browse_tickets_button,
                wallet_page_class.plan_a_journey_button]

    class expired_tickets_button(Element):
        loc = "id", "{}fragment_my_wallet_expired_tickets".format(app_id)

    class browse_tickets_button(Element):
        loc = "id", "{}fragment_my_wallet_browse_tickets".format(app_id)

    class plan_a_journey_button(Element):
        loc = "id", "{}fragment_my_wallet_plan_journey".format(app_id)

    class purchased_tickets_quantity(Element):
        loc = "id", "{}view_ticket_quantity_quantity".format(app_id)

    class purchased_ticket(Element):
        loc = "id", "{}fragment_my_wallet_purchased_container".format(app_id)


class send_ticket_information_page_class(Page):
    def check_on_load(self):
        return [send_ticket_information_page_class.ticket_type_and_price]

    class ticket_type_and_price(Element):
        loc = "id", "{}fragment_ticket_information_subtitle".format(app_id)

    class send_ticket_button(Element):
        loc = "id", "{}fragment_ticket_information_transfer_ticket".format(app_id)


class send_tickets_page_class(Page):
    def check_on_load(self):
        return [send_tickets_page_class.send_via_email_button]

    class send_via_email_button(Element):
        loc = "id", "{}fragment_send_ticket_send".format(app_id)


class confirm_recipient_page_class(Page):
    def check_on_load(self):
        return [confirm_recipient_page_class.edit_recipient_details_button,
                confirm_recipient_page_class.confirm_and_send_button]

    class edit_recipient_details_button(Element):
        loc = "id", "{}fragment_send_ticket_confirm_edit".format(app_id)

    class confirm_and_send_button(Element):
        loc = "id", "{}fragment_send_ticket_confirm_send".format(app_id)

    class recipient_name(Element):
        loc = "id", "{}view_buses_row_text_top_label".format(app_id)

    class recipient_email(Element):
        loc = "id", "{}view_buses_row_text_top_label".format(app_id)


class recipients_email_address_page_class(Page):
    def check_element_inheritance(self):
        return [recipients_email_address_page_class.email_address_field,
                recipients_email_address_page_class.continue_button]

    class email_address_field(Element):
        loc = "xpath", "//TextInputLayout[@text='Email address']//android.widget.EditText"

    class continue_button(Element):
        loc = "id", "{}fragment_add_recipient_confirm_button".format(app_id)


class ticket_sent_page_class(Page):
    def check_on_load(self):
        return [ticket_sent_page_class.return_to_my_wallet_button]

    class return_to_my_wallet_button(Element):
        loc = "id", "{}fragment_send_ticket_complete_back_to_wallet".format(app_id)


class password_reset_page_class(Page):
    def check_on_load(self):
        return [password_reset_page_class.email_field,
                password_reset_page_class.send_reset_code_button]

    class reset_password_title(Element):
        loc = "xpath", "//android.widget.TextView[@text='What is your email?']"

    class reset_password_body(Element):
        loc = "xpath", "//android.widget.TextView[@text='We will send a special code to this email address so " \
                       "that you may reset your passsword.']"

    class email_field(Element):
        loc = "xpath", "//TextInputLayout[@text='Your email']//android.widget.EditText"

    class send_reset_code_button(Element):
        loc = "id", "{}fragment_reset_password_button".format(app_id)


class my_journey_page_class(Page):
    def check_on_load(self):
        return [my_journey_page_class.departures_tab]

    class departures_tab(Element):
        loc = "xpath", "//android.widget.TextView[@text='DEPARTURES']"

    class live_bus_icon(Element):
        loc = "class name", "android.view.View"

    class which_bus_message(Element):
        loc = "id", "{}view_buses_journey_my_bus_label".format(app_id)


class live_bus_information_page_class(Page):
    def check_on_load(self):
        return [live_bus_information_page_class.map_tab,
                live_bus_information_page_class.bus_details]

    class map_tab(Element):
        loc = "xpath", "//android.support.v7.app.a$c[1]"

    class bus_details(Element):
        loc = "id", "fragment_explore_bus_details".format(app_id)

    class bus_number(Element):
        loc = "id", "view_rti_buses_row_top_label".format(app_id)

    class stop_name(Element):
        loc = "id", "view_rti_buses_row_bottom_label".format(app_id)


class journey_options_tickets_page_class(Page):
    def check_on_load(self):
        return [journey_options_tickets_page_class.journey_information]

    class journey_information(Element):
        loc = "id", "{}view_journey_option_layout".format(app_id)

    class ticket_option(Element):
        loc = "id", "{}view_buses_row_container".format(app_id)


class bus_stop_information_page_class(Page):
    def check_on_load(self):
        return [bus_stop_information_page_class.three_dot_icon]

    class three_dot_icon(Element):
        loc = "id", "{}view_buses_row_right_layout".format(app_id)

    class travel_to_here_selection(Element):
        loc = "xpath", "//android.widget.TextView[@text='Travel to here']"

    class bus_stop_name(Element):
        loc = "id", "{}view_buses_row_text_top_label".format(app_id)

    class bus_travel_direction(Element):
        loc = "id", "{}view_buses_row_text_bottom_label".format(app_id)

    class next_bus_number(Element):
        loc = "id", "{}view_stop_bus_row_route".format(app_id)

    class next_bus_destination(Element):
        loc = "id", "{}view_stop_bus_top_label".format(app_id)


class choose_bus_company_page_class(Page):
    def check_on_load(self):
        return [choose_bus_company_page_class.bus_company_more_button,
                choose_bus_company_page_class.bus_company_salisbury_reds_button,
                choose_bus_company_page_class.bus_company_unilink_button,
                choose_bus_company_page_class.bus_company_bluestar_button,
                choose_bus_company_page_class.bus_company_swindon_button]

    class bus_company_more_button(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}opco_list_container']" \
                       "//android.widget.ImageView[1]".format(app_id)

    class bus_company_salisbury_reds_button(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}opco_list_container']" \
                       "//android.widget.ImageView[2]".format(app_id)

    class bus_company_unilink_button(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}opco_list_container']" \
                       "//android.widget.ImageView[3]".format(app_id)

    class bus_company_bluestar_button(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}opco_list_container']" \
                       "//android.widget.ImageView[4]".format(app_id)

    class bus_company_swindon_button(Element):
        loc = "xpath", "//android.widget.LinearLayout[@resource-id='{}opco_list_container']" \
                       "//android.widget.ImageView[5]".format(app_id)


class my_account_page_class(Page):
    def check_on_load(self):
        return [my_account_page_class.edit_details_button,
                my_account_page_class.change_password_button,
                my_account_page_class.payment_methods_button,
                my_account_page_class.log_out_button]

    class edit_details_button(Element):
        loc = "id", "{}fragment_my_account_edit_details".format(app_id)

    class change_password_button(Element):
        loc = "id", "{}fragment_my_account_change_password".format(app_id)

    class payment_methods_button(Element):
        loc = "id", "{}fragment_my_account_edit_payment_methods".format(app_id)

    class log_out_button(Element):
        loc = "id", "{}fragment_my_account_logout".format(app_id)


class home_go_south_page_class(Page):
    def check_on_load(self):
        return [home_page_class.browse_tickets,
                home_page_class.general_menu,
                ]

    class browse_tickets(Element):
        loc = "id", "{}fragment_home_browse_tickets_button".format(app_id)

    class departure(Element):
        loc = "id", "{}fragment_home_departures_button".format(app_id)

    class login(Element):
        loc = "id", "{}fragment_home_login".format(app_id)

    class general_menu(Element):
        loc = "class name", "android.widget.ImageButton"

    class wallet_banner_bottom(Element):
        loc = "id", "{}fragment_home_my_wallet_status".format(app_id)

    class journey_planner_button(Element):
        loc = "id", "{}action_drawer_plan_journey_location".format(app_id)

    class my_wallet_button(Element):
        loc = "id", "{}action_drawer_my_tickets".format(app_id)

    class my_account_button(Element):
        loc = "id", "{}action_drawer_account".format(app_id)

    class change_bus_company_button(Element):
        loc = "id", "{}action_drawer_change_operator".format(app_id)


class oxford_journey_options_page_class(Page):
    def check_on_load(self):
        return [oxford_journey_options_page_class.night_owl_adult_ticket_button]

    class night_owl_adult_ticket_button(Element):
        loc = "xpath", "android.widget.TextView[@text='Night Owl']"


class purchase_success_screen_class(Page):
    def check_on_load(self):
        return [purchase_success_screen_class.send_ticket_button,
                purchase_success_screen_class.view_ticket_details_button,
                purchase_success_screen_class.home_button]

    class send_ticket_button(Element):
        loc = "id", "{}fragment_ticket_information_transfer_ticket".format(app_id)

    class view_ticket_details_button(Element):
        loc = "id", "{}fragment_ticket_information_ticket_details".format(app_id)

    class home_button(Element):
        loc = "id", "{}fragment_ticket_information_ticket_home".format(app_id)

    class activate_ticket_button(Element):
        loc = "id", "{}view_buses_row_ticket_bottom_button".format(app_id)

    class modal_activate_button(Element):
        loc = "id", "android:id/button1"

    class ticket_brand(Element):
        loc = "id", "{}view_buses_row_ticket_top_label".format(app_id)

    class ticket_type(Element):
        loc = "id", "{}view_buses_row_ticket_bottom_label".format(app_id)


class activated_ticket_screen_class(Page):
    def check_on_load(self):
        return []

    class brand(Element):
        loc = "id", "{}fragment_activate_ticket_title".format(app_id)

    class ticket_type(Element):
        loc = "id", "{}fragment_activate_ticket_subtitle".format(app_id)

    class time(Element):
        loc = "id", "{}fragment_activate_ticket_time".format(app_id)

    class remaining_time_counter(Element):
        loc = "id", "{}fragment_activate_ticket_counter".format(app_id)

    class activation_details(Element):
        loc = "id", "{}fragment_activate_ticket_footer".format(app_id)

    class my_journey_button(Element):
        loc = "id", "{}fragment_activate_ticket_realtime_data".format(app_id)

    class ticket_information_button(Element):
        loc = "id", "{}fragment_activate_ticket_info".format(app_id)


class forgotten_password_code_page_class(Page):
    def check_on_load(self):
        return [forgotten_password_code_page_class.code_entry_field_1,
                forgotten_password_code_page_class.code_entry_field_2,
                forgotten_password_code_page_class.code_entry_field_3,
                forgotten_password_code_page_class.code_entry_field_4,
                forgotten_password_code_page_class.next_button,
                forgotten_password_code_page_class.resend_code_link
                ]

    class code_entry_field_1(Element):
        loc = "id", "{}fragment_register_code_1".format(app_id)

    class code_entry_field_2(Element):
        loc = "id", "{}fragment_register_code_2".format(app_id)

    class code_entry_field_3(Element):
        loc = "id", "{}fragment_register_code_3".format(app_id)

    class code_entry_field_4(Element):
        loc = "id", "{}fragment_register_code_4".format(app_id)

    class next_button(Element):
        loc = "id", "{}fragment_register_code_complete_button".format(app_id)

    class resend_code_link(Element):
        loc = "id", "{}fragment_register_code_resend".format(app_id)

    class header(Element):
        loc = "id", "{}fragment_register_email_header_label".format(app_id)

    class body(Element):
        loc = "id", "{}fragment_register_email_header_description".format(app_id)


def check_element_inheritance(element):
    return eval(element.expected_page_name + "." + element.element_name)
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.