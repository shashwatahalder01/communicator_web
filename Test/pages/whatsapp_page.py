from data.data import Data
from pages.base_page import BasePage
from data.locators import WhatsAppLocator
from utils.excel_utils import *
from time import sleep


class WhatApp(BasePage):
    def __init__(self, driver):
        self.locator = WhatsAppLocator
        self.data = Data
        super().__init__(driver)

    def extract_group_contacts(self):
        contacts = []
        sleep(4)
        self.send_data(self.data.group_name, *self.locator.search)
        sleep(1)
        self.click(*self.locator.group)
        sleep(1)
        self.click(*self.locator.group_info)
        sleep(1)
        self.move_cursor_to_element(*self.locator.total_participants)
        sleep(1)
        val = self.get_text(*self.locator.total_participants)
        print(val)
        # self.click(*self.locator.total_participants)
        sleep(4)
        self.move_cursor_to_element(*self.locator.show_more)
        sleep(1)
        self.click(*self.locator.show_more)
        sleep(1)
        element = self.find_element(*self.locator.scroll_element)
        sleep(1)
        vertical_ordinate = 100
        for i in range(0, 40):
            # print(vertical_ordinate)
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, vertical_ordinate)
            sleep(0.2)
            try:
                val = self.get_text_of_multiple_element(*self.locator.contact_names)
                contacts.extend(val)
            except Exception as e:
                pass
                # print(e)
            vertical_ordinate += 400
            sleep(0.2)
            # val = self.element_is_displayed(*self.locator.report_group)
            # print(val)
            # if val is True and i>3:
            #     break
        actual_contacts = list(set(contacts))
        print(*actual_contacts, sep='\n')
        print(len(actual_contacts))
        writesinglecol(self.data.user_data, self.data.whatapp_sheetname, len(actual_contacts), 1, 1, actual_contacts)
