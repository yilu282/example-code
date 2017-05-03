# -*- coding: utf-8 -*-
from bok_choy.page_object import PageObject

class BaiduSearchPage(PageObject):
    """
    Baidu search page
    """

    url = 'https://www.baidu.com/'

    def is_browser_on_page(self):
        return self.q(css='#su').is_present()

    def input_search_key(self, keyword):
        return self.q(css="#kw").fill(keyword)


    def click_search_btn(self):
        self.q(css="#su").click()

    def search(self, keyword):
        self.input_search_key(keyword)
        self.click_search_btn()
        BaiduSearchResultPage(self.browser).wait_for_page()

class BaiduSearchResultPage(PageObject):
    """
    Baidu search page
    """
    url = None

    def is_browser_on_page(self):
        return self.q(css='h3').is_present()
    
    @property
    def search_results(self):
        return self.q(css='h3').first.text