# -*- coding: utf-8 -*-
import os
import unittest
from bok_choy.web_app_test import WebAppTest
from pages import BaiduSearchPage, BaiduSearchResultPage

class TestBaidu(WebAppTest):
    """
    Tests for the Baidu site.
    """
    def setUp(self):
        """
        Instantiate the page object.
        """
        super(TestBaidu, self).setUp()
        self.baidu_search_page = BaiduSearchPage(self.browser)        

    def test_page_existence(self):
        """
        Make sure that the page is accessible.
        """
        self.baidu_search_page.visit()

    def test_search(self):
        test_key = u"学堂在线"
        self.baidu_search_page.visit().search(test_key)
        self.baidu_results_page = BaiduSearchResultPage(self.browser)
        result = self.baidu_results_page.search_results
        assert test_key in result[0]



if __name__ == '__main__':
    os.environ["SELENIUM_BROWSER"] = "chrome"
    unittest.main()