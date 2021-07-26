from pages.whatsapp_page import WhatApp
from testcase.base_test import BaseTest


class TestWhatsApp(BaseTest):

    def test_extract_group_contacts(self):
        page_signin = WhatApp(self.driver)
        page_signin.extract_group_contacts()

# python3 -m unittest testcase.test1
# python3 -m pytest -s testcase/test1.py --alluredir=ReportAllure &&  allure serve ReportAllure/
