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
    product_page = 1
    number_item = 0
    word_separator = "+"
    link = ""
    Selenium = Selenium()
    Search = "beauty"
    def CrawlingMerchant(self,sub_root_merchant,merchant_format):
        if merchant_format == "css-lksuc9":
            self.Merchant_name = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div/h1/a"]))
            self.Merchant_rate_point = self.Selenium.ExtractElementAttribute("src",''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li[2]/span/span/img"])).replace("https://ecs7.tokopedia.net/img/repsys/","").replace(".gif","").replace("-"," ")
            self.Merchant_location = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[3]/ul/li[2]"]))
            self.Merchant_established = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[3]/ul/li[4]"]))
            follow_elements_count = len(self.Selenium.ExtractElements("//ul[contains(@class,'css-1ewvjcw')]/li[4]/div[1]/span"))
            if follow_elements_count == 1:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li[4]/div/span"])).replace(",",'.'))
            elif follow_elements_count == 2:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li[4]/div/span"])).replace(",",'.'))
                follow_post = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/div[4]/ul/li[4]/div/span[2]"]))
                if follow_post == 'rb':
                    self.Merchant_followers *=1000
                elif follow_post == 'jt':
                    self.Merchant_followers *=1000000
            self.Selenium.Load(''.join([self.Merchant_html_path,"/info"]))
            self.Merchant_sold_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[2]/div/span"]))))
            self.Merchant_succesful_transaction = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li/div/span"]))))
            self.Merchant_showcase = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[3]/div/span"]))))
            self.Merchant_active_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[4]/div/span"]))))
            self.Selenium.ClickIt("//div[contains(@class, 'css-olkhvh')]/button[3]")
            ##time.sleep(1)
            check_transaction = self.Selenium.ExtractElementAttribute("class","//div[contains(@class, 'css-1ejlaeo')]/div")
            if check_transaction == 'css-1l9sqhn':
                self.Merchant_stat_1_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[2]")
                ##time.sleep(1)
                self.Merchant_stat_3_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[3]")
                ##time.sleep(1)
                self.Merchant_stat_12_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
            else:
                self.Merchant_stat_1_month = 0
                self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[2]")
                #time.sleep(1)
                check_transaction = self.Selenium.ExtractElementAttribute("class","//div[contains(@class, 'css-1ejlaeo')]/div")
                if check_transaction == 'css-1l9sqhn':
                    self.Merchant_stat_3_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                    self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[3]")
                    #time.sleep(1)
                    self.Merchant_stat_12_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                    DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
                else:
                    self.Merchant_stat_1_month = 0
                    self.Merchant_stat_3_month = 0
                    self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[3]")
                    #time.sleep(1)
                    check_transaction = self.Selenium.ExtractElementAttribute("class","//div[contains(@class, 'css-1ejlaeo')]/div")
                    if check_transaction == 'css-1l9sqhn':
                        self.Merchant_stat_12_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                        DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
                    else:
                        self.Merchant_stat_1_month = 0
                        self.Merchant_stat_3_month = 0
                        self.Merchant_stat_12_month = 0
                        DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
            self.Selenium.BackPage()
        elif merchant_format == "css-2i715u":
            self.Merchant_name = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div/div/div/h1"]))
            self.Merchant_rate_point = self.Selenium.ExtractElementAttribute("src",''.join([sub_root_merchant,"/div/div/div[1]/div[2]/ul/li[2]/span/span/img"])).replace("https://ecs7.tokopedia.net/img/repsys/","").replace(".gif","").replace("-"," ")
            self.Merchant_location = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div/div/ul/li[2]"]))
            self.Merchant_established = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div/div/ul/li[4]"]))
            follow_elements_count = len(self.Selenium.ExtractElements("//ul[contains(@class,'css-r3r4gj')]/li[4]/div[1]/span"))
            if follow_elements_count == 1:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/ul/li[4]/div/span"])).replace(",",'.'))
            elif follow_elements_count == 2:
                self.Merchant_followers = float(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/ul/li[4]/div/span"])).replace(",",'.'))
                follow_post = self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div/div/div[2]/ul/li[4]/div/span[2]"]))
                if follow_post == 'rb':
                    self.Merchant_followers *=1000
                elif follow_post == 'jt':
                    self.Merchant_followers *=1000000
            self.Selenium.Load(''.join([self.Merchant_html_path,"/info"]))
            self.Merchant_sold_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[2]/div/span"]))))
            self.Merchant_succesful_transaction = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li/div/span"]))))
            self.Merchant_showcase = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[3]/div/span"]))))
            self.Merchant_active_product = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText(''.join([sub_root_merchant,"/div/div[3]/div[2]/ul/li[4]/div/span"]))))
            self.Selenium.ClickIt("//div[contains(@class, 'css-olkhvh')]/button[3]")
            #time.sleep(1)
            check_transaction = self.Selenium.ExtractElementAttribute("class","//div[contains(@class, 'css-1ejlaeo')]/div")
            if check_transaction == 'css-1l9sqhn':
                self.Merchant_stat_1_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[2]")
                #time.sleep(1)
                self.Merchant_stat_3_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[3]")
                #time.sleep(1)
                self.Merchant_stat_12_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
            else:
                self.Merchant_stat_1_month = 0
                self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[2]")
                #time.sleep(1)
                check_transaction = self.Selenium.ExtractElementAttribute("class","//div[contains(@class, 'css-1ejlaeo')]/div")
                if check_transaction == 'css-1l9sqhn':
                    self.Merchant_stat_3_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                    self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[3]")
                    #time.sleep(1)
                    self.Merchant_stat_12_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                    DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
                else:
                    self.Merchant_stat_1_month = 0
                    self.Merchant_stat_3_month = 0
                    self.Selenium.ClickIt("//div[contains(@class,'css-1vfv969')]/li[3]")
                    #time.sleep(1)
                    check_transaction = self.Selenium.ExtractElementAttribute("class","//div[contains(@class, 'css-1ejlaeo')]/div")
                    if check_transaction == 'css-1l9sqhn':
                        self.Merchant_stat_12_month = int(self.Selenium.ExtractElementText("//p[contains(@class, 'css-merchant-2ZRqM3sb')]").replace("Dari ",'').replace(" Transaksi",'').replace('.',''))
                        DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
                    else:
                        self.Merchant_stat_1_month = 0
                        self.Merchant_stat_3_month = 0
                        self.Merchant_stat_12_month = 0
                        DB().InsertDB_Merchant(self.Merchant_name, self.Merchant_rate_point, self.Merchant_location, self.Merchant_established, self.Merchant_sold_product, self.Merchant_succesful_transaction, self.Merchant_showcase, self.Merchant_active_product, self.Merchant_followers, self.Merchant_html_path, self.Merchant_stat_1_month, self.Merchant_stat_3_month, self.Merchant_stat_12_month)
            self.Selenium.BackPage()
        self.Selenium.BackPage()

    def Crawling(self):
        self.Selenium.link = "https://www.tokopedia.com/search?st=product&q="
        self.Selenium.Load(''.join([self.Selenium.link, Concatenate().InfuseSeparator(main=self.Search, separator=self.word_separator)]))
        self.Selenium.root_xpath = "//div[contains(@class, '_1hoMwZCy')]/div"
        while self.product_page == 1 or self.product_page < 101:
            if self.product_page != 1:
                product_paging = "&page="
                self.Selenium.Load(''.join([self.Selenium.link, "&page=", str(self.product_page)]))
            product_elements_count = len(self.Selenium.ExtractElements(self.Selenium.root_xpath))
            element_ordinal = 0
            while (element_ordinal < product_elements_count):
                element_ordinal += 1
                sub_root_xpath = ''.join([self.Selenium.root_xpath, "[", str(element_ordinal), "]"])
                product_wrapper_class_type = self.Selenium.ExtractElementAttribute("class", sub_root_xpath)
                if product_wrapper_class_type == "_33JN2R1i pcr":
                    if(len(self.Selenium.ExtractElements(''.join([sub_root_xpath,"/div/a/div[2]/div/div/div"])))==2):
                        if(self.Selenium.ExtractElementAttribute("class",''.join([sub_root_xpath,"/div/a/div[2]/div/div/div/i"]))!= "_1rxDEEIy _1DJPSYZc _2DPG0hTy"):
                            product_html = self.Selenium.ExtractElementAttribute("href", ''.join([sub_root_xpath,"/div/a"]))
                            self.Selenium.Load(product_html)
                            self.Merchant_html_path = self.Selenium.ExtractElementAttribute("href","//div[contains(@class, 'rvm-merchat-name')]/a")
                            self.Selenium.Load(self.Merchant_html_path)
                            sub_root_merchant = "//div[contains(@id, 'merchant-root')]"
                            merchant_format = self.Selenium.ExtractElementAttribute("class",''.join([sub_root_merchant,"/div/div/div"]))
                            self.CrawlingMerchant(sub_root_merchant,merchant_format)
                            self.number_item +=1
                            print(self.number_item)
                            self.Selenium.BackPage()
                        else:
                            print("skip")
                    else:
                        product_html = self.Selenium.ExtractElementAttribute("href", ''.join([sub_root_xpath,"/div/a"]))
                        self.Selenium.Load(product_html)
                        self.Merchant_html_path = self.Selenium.ExtractElementAttribute("href","//div[contains(@class, 'rvm-merchat-name')]/a")
                        self.Selenium.Load(self.Merchant_html_path)
                        sub_root_merchant = "//div[contains(@id, 'merchant-root')]"
                        merchant_format = self.Selenium.ExtractElementAttribute("class",''.join([sub_root_merchant,"/div/div/div"]))
                        self.CrawlingMerchant(sub_root_merchant,merchant_format)
                        self.number_item +=1
                        print(self.number_item)
                        self.Selenium.BackPage()
            self.product_page += 1
        self.Selenium.Close()
#Run().Create()
DB().CreateDB()
Run().Crawling()
