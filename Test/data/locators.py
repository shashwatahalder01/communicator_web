from selenium.webdriver.common.by import By


class WhatsAppLocator(object):
    search = (By.XPATH, '//div[@class="_13NKt copyable-text selectable-text"]')

    @staticmethod
    def group_name(group_name):
        group = (By.XPATH, '//span[@title="{group_name}"]')
        return group

    group = (By.XPATH, '//div[@class="_3OvU8"]')
    group_info = (By.XPATH, '//div[@class="_21nHd"]//span[@class="_ccCW FqYAR i0jNr"]')

    total_participants = (By.XPATH, '//span[ @class="_2MNpf VWPRY _1lF7t" and contains(text(), "participants")]')
    show_more = (By.XPATH, '//div[ @class="zoWT4" and contains(text(), "more")]')

    # contact_names = (By.XPATH, '//div[@class="_3m_Xw"]//span[@class="_ccCW FqYAR i0jNr"]')
    contact_names = (By.XPATH, '//div[@class="_2P1rL _1is6W"]//div[@class="_3uIPm WYyr1"]//div[@class="_3m_Xw"]//span[@class="_ccCW FqYAR i0jNr"]')
    exit_group = (By.XPATH, '//span[normalize-space()="Exit group"]')
    report_group = (By.XPATH, '//span[normalize-space()="Report group"]')
    '//div[@class="_3m_Xw"]//span[@class="_ccCW FqYAR i0jNr"]'
    '//div[@class="nBIOd tm2tP copyable-area"]//div[@tabindex="-1"]//div[@data-testid="cell-frame-container"]//span[@class="_3q9s6"]//span[ @class="_ccCW FqYAR i0jNr" ]'
    '//div[@class="nBIOd tm2tP copyable-area"]//span[@class="_3q9s6"]//span[ @class="_ccCW FqYAR i0jNr" ]'

    scroll_element = (By.XPATH, '//div[@class="_3Bc7H KPJpj"]')
