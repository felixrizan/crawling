from SQLite import DB
from OmniCrawler import Selenium
from datetime import datetime
from DataStructure.StringManipulator import Concatenate, Enumerate, Manipulate
import traceback
import time

class Run:
    Merchant_name = ""
    Merchant_rate_point = ""
    Merchant_location = ""
    Merchant_established = ""
    Merchant_sold_product = 0
    Merchant_succesful_transaction = 0
    Merchant_showcase = 0
    Merchant_active_product = 0
    Merchant_followers = 0
    Merchant_html_path = ""
    Product_name = ""
    Product_price = 0
    Product_sold = 0
    Product_rate = ""
    Product_merchant = ""
    product_page = 0
    word_separator = "+"
    link = ""
    Selenium = Selenium()
    Search = "Beauty"
    def CrawlingMerchantProduct(self, Product_count, Merchant_html):
        Product_page_html = ''.join([Merchant_html,"/page/"])
        Product_counts = 0
        Product_pages = 0
        Back_pages_count = 0
        while(Product_counts < Product_count):
            Product_counting = len(self.Selenium.ExtractElements("//div[contains(@class, 'css-merchant-2onvNofT css-1l533tl')]/div/a"))
            Product_sub_counting =0
            if Product_pages == 0:
                Product_pages +=1
            elif Product_pages != 0:
                Product_pages +=1
                Back_pages_count +=1
                self.Selenium.Load(''.join([Product_page_html,str(Product_pages)]))
            while Product_sub_counting < Product_counting:
                Product_sub_counting +=1
                Product_counts +=1
                subsub_html = "//div[contains(@class, 'css-merchant-2onvNofT css-1l533tl')]/div/a["+str(Product_sub_counting)+"]"
                Product_sub_html = self.Selenium.ExtractElementAttribute("href",xpath=subsub_html)
                self.Selenium.Load(Product_sub_html)
                Product_name = self.Selenium.ExtractElementText("//div[contains(@id,'content-container')]/div[2]/div/div/div/div[2]/h1/span")
                Product_price = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText("//div[contains(@id,'content-container')]/div[2]/div/div/div/div[2]/div[5]/div/span[2]")))
                Product_sold = int(Enumerate().ReformToNumber(self.Selenium.ExtractElementText("//div[contains(@class, 'mt-30')]/div[contains(@class, 'rvm-product-info')]/div[2]/div/div[2]")))
                Product_rate = self.Selenium.ExtractElementText("//div[contains(@id,'content-container')]/div[2]/div/div/div/div[2]/div[2]/div/span")
                DB().InsertDB_Product(Product_name, Product_price, Product_sold, Product_rate, Merchant_html)
                self.Selenium.BackPage()
        for i in range (Back_pages_count):
            self.Selenium.BackPage()

            def Crawling(self):
                self.Selenium.link = "https://shopee.co.id/search?keyword="
                self.Selenium.Load(''.join([self.Selenium.link, Concatenate().InfuseSeparator(main=self.Search, separator=self.word_separator)]))
