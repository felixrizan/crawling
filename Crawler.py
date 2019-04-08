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
    Merchant_stat_1_month = 0
    Merchant_stat_3_month = 0
    Merchant_stat_12_month = 0
    Product_name = ""
    Product_price = 0
    Product_sold = 0
    Product_rate = ""
    Product_merchant = ""
    product_page = 0
    word_separator = "+"
    link = ""
    Selenium = Selenium()
    Search = "Kecantikan"
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
                self.Selenium.Load(''.join([Product_page_html,str(Product_pages),"?sort=10"]))
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
    def CrawlingMerchant(self,sub_root_merchant,merchant_format):
        if merchant_format == "css-1ip3b2w":
            self.Merchant_name = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div/h1/a"]))
            self.Merchant_rate_point = self.Selenium.ExtractElementAttribute("src",''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li[3]/span/span/img"])).replace("https://ecs7.tokopedia.net/img/repsys/","").replace(".gif","").replace("-"," ")
            self.Merchant_location = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[3]/ul/li[2]"]))
            self.Merchant_established = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[3]/ul/li[4]"]))
            follow_elements_count = len(self.Selenium.ExtractElements("//ul[contains(@class,'css-1ewvjcw')]/li[1]/div[1]/span"))
            if follow_elements_count == 1:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li/div/span"])).replace(",",'.'))
            elif follow_elements_count == 2:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li/div/span"])).replace(",",'.'))
                follow_post = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li/div/span[2]"]))
                if follow_post == 'rb':
                    self.Merchant_followers *=1000
                elif follow_post == 'jt':
                    self.Merchant_followers *=1000000
            self.Selenium.Load(''.join([self.Merchant_html_path,"/info"]))
            self.Merchant_sold_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[2]/div/span"]))))
            self.Merchant_succesful_transaction = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li/div/span"]))))
            self.Merchant_showcase = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[3]/div/span"]))))
            self.Merchant_active_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[4]/div/span"]))))
            DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path)
            self.Selenium.BackPage()
        elif merchant_format == "css-1643rfj":
            self.Merchant_name = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div/div/div/h1"]))
            self.Merchant_rate_point = self.Selenium.ExtractElementAttribute("src",''.join([sub_root_merchant,"/div/div/div[1]/div[2]/ul/li[3]/span/span/img"])).replace("https://ecs7.tokopedia.net/img/repsys/","").replace(".gif","").replace("-"," ")
            self.Merchant_location = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div/div/ul/li[2]"]))
            self.Merchant_established = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div/div/ul/li[4]"]))
            follow_elements_count = len(self.Selenium.ExtractElements("//ul[contains(@class,'css-h7bc2w')]/li[1]/div[1]/span"))
            if follow_elements_count == 1:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/ul/li/div/span"])).replace(",",'.'))
            elif follow_elements_count == 2:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/ul/li/div/span"])).replace(",",'.'))
                follow_post = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/ul/li/div/span[2]"]))
                if follow_post == 'rb':
                    self.Merchant_followers *=1000
                elif follow_post == 'jt':
                    self.Merchant_followers *=1000000
            self.Selenium.Load(''.join([self.Merchant_html_path,"/info"]))
            self.Merchant_sold_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[2]/div/span"]))))
            self.Merchant_succesful_transaction = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li/div/span"]))))
            self.Merchant_showcase = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[3]/div/span"]))))
            self.Merchant_active_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[4]/div/span"]))))
            DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path)
            self.Selenium.BackPage()
        self.CrawlingMerchantProduct(self.Merchant_active_product, self.Merchant_html_path)
        self.Selenium.BackPage()

    def Crawling(self):
        self.Selenium.link = "https://www.tokopedia.com/search?st=product&q="
        self.Selenium.Load(''.join([self.Selenium.link, Concatenate().InfuseSeparator(main=self.Search, separator=self.word_separator)]))
        self.Selenium.ExtractElements("//a")
        for element in self.Selenium.elements:
            if "Hot List" in element.text:
                self.Selenium.link = Manipulate().RemoveParts("&page=2", self.Selenium.ExtractElementAttribute("href", xpath="//a[contains(@class, 'GUHElpkt')]"))
                self.Selenium.root_xpath = "//div[contains(@class, '_29iRsaHv')]/div"
            else:
                self.Selenium.root_xpath = "//div[contains(@class, '_1hoMwZCy')]/div"
        product_last_result_number_in_page = Enumerate().CleanNumber(self.Selenium.ExtractElementText("//div[contains(@class, '_1lUX-bZg')]/span/strong[2]").split()[2])
        product_number_of_results = Enumerate().CleanNumber(self.Selenium.ExtractElementText("//div[contains(@class, '_1lUX-bZg')]/span/strong[3]"))
        while self.product_page == 0 or (int(product_number_of_results) != int(product_last_result_number_in_page) and (self.product_page < 101)):
            self.product_page += 1
            if self.product_page != 1:
                product_paging = "&page="
                remake_paging = product_paging+str(self.product_page - 1)
                self.Selenium.link = Manipulate().RemoveParts(remake_paging, self.Selenium.ExtractElementAttribute("href", xpath="//a[contains(@class, 'GUHElpkt')]"))
                self.Selenium.Load(''.join([self.Selenium.link, "&page=", str(self.product_page)]))
                product_last_result_number_in_page = Enumerate().CleanNumber(self.Selenium.ExtractElementText("//div[contains(@class, '_1lUX-bZg')]/span/strong[2]").split()[2])
                product_number_of_results = Enumerate().CleanNumber(self.Selenium.ExtractElementText("//div[contains(@class, '_1lUX-bZg')]/span/strong[3]"))
            product_elements_count = len(self.Selenium.ExtractElements(self.Selenium.root_xpath))
            element_ordinal = 0
            while (element_ordinal < product_elements_count):
                element_ordinal += 1
                sub_root_xpath = ''.join([self.Selenium.root_xpath, "[", str(element_ordinal), "]"])
                product_wrapper_class_type = self.Selenium.ExtractElementAttribute("class", sub_root_xpath)
                if product_wrapper_class_type == "ta-inventory":
                    ta_product_count = self.Selenium.ExtractElementAttribute("child_item", sub_root_xpath)
                    item = 0
                    while item==0 or item< int(ta_product_count):
                        item+=1
                        subsub_root_xpath = ''.join([sub_root_xpath,"/div[4]/div[",str(item),"]/div/a"])
                        product_html = self.Selenium.ExtractElementAttribute("href", subsub_root_xpath)
                        self.Selenium.Load(product_html)
                        self.Merchant_html_path = self.Selenium.ExtractElementAttribute("href","//div[contains(@class, 'rvm-merchat-name')]/a")
                        self.Selenium.Load(self.Merchant_html_path)
                        sub_root_merchant = "//div[contains(@id, 'merchant-root')]"
                        merchant_format = self.Selenium.ExtractElementAttribute("class",''.join([sub_root_merchant,"/div/div/div"]))
                        self.CrawlingMerchant(sub_root_merchant,merchant_format)
                        self.Selenium.BackPage()
                if product_wrapper_class_type == "_33JN2R1i pcr":
                    product_html = self.Selenium.ExtractElementAttribute("href", ''.join([sub_root_xpath,"/div/a"]))
                    self.Selenium.Load(product_html)
                    self.Merchant_html_path = self.Selenium.ExtractElementAttribute("href","//div[contains(@class, 'rvm-merchat-name')]/a")
                    self.Selenium.Load(self.Merchant_html_path)
                    sub_root_merchant = "//div[contains(@id, 'merchant-root')]"
                    merchant_format = self.Selenium.ExtractElementAttribute("class",''.join([sub_root_merchant,"/div/div/div"]))
                    self.CrawlingMerchant(sub_root_merchant,merchant_format)
                    self.Selenium.BackPage()
                elif product_wrapper_class_type == "ta-inventory child":
                    ta_product_count = self.Selenium.ExtractElementAttribute("child_item", sub_root_xpath)
                    item = 0
                    while item==0 or item< int(ta_product_count):
                        item+=1
                        subsub_root_xpath = ''.join([sub_root_xpath,"/div[2]/div[",str(item),"]/div/a"])
                        product_html = self.Selenium.ExtractElementAttribute("href", subsub_root_xpath)
                        self.Selenium.Load(product_html)
                        self.Merchant_html_path = self.Selenium.ExtractElementAttribute("href","//div[contains(@class, 'rvm-merchat-name')]/a")
                        self.Selenium.Load(self.Merchant_html_path)
                        sub_root_merchant = "//div[contains(@id, 'merchant-root')]"
                        merchant_format = self.Selenium.ExtractElementAttribute("class",''.join([sub_root_merchant,"/div/div/div"]))
                        self.CrawlingMerchant(sub_root_merchant,merchant_format)
                        self.Selenium.BackPage()

        Selenium.Close()
#Run().Create()
DB().CreateDB()
Run().Crawling()
