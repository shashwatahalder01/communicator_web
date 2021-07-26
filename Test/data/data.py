import os
from pathlib import Path


class Data(object):
    user_data = Path(__file__).parent / "userdata.xlsx"
    base_url = 'https://web.whatsapp.com/'
    group_name = 'QUPS IR2'
    whatapp_sheetname = 'Whatsapp_contacts'
