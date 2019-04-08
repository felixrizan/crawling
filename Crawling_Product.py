from SQLite import DB
from OmniCrawler import Selenium
from datetime import datetime
from DataStructure.StringManipulator import Concatenate, Enumerate, Manipulate
import traceback
import time


class Run:
    Merchant_active_product = 160
    Merchant_html_path = "https://www.tokopedia.com/beautyforever99"
    Product_name = ""
    Product_price = 0
    Product_sold = 0
    Product_rate = ""
    Selenium = Selenium()
    def CrawlingMerchantProduct(self):
        self.Selenium.Load(''.join([self.Merchant_html_path,"?sort=7"]))
        Product_page_html = ''.join([self.Merchant_html_path,"/page/"])
        Product_counts = 0
        Product_pages = 0
        while(Product_counts < self.Merchant_active_product):
            Product_counting = len(self.Selenium.ExtractElements("//div[contains(@class, 'css-merchant-2onvNofT css-1l533tl')]/div/a"))
            Product_sub_counting = 0
            if Product_pages == 0:
                Product_pages +=1
            else:
                Product_pages +=1
                self.Selenium.Load(''.join([Product_page_html,str(Product_pages),"?sort=7"]))
            while Product_sub_counting < Product_counting:
                Product_sub_counting +=1
                Product_counts +=1
                subsub_html = "//div[contains(@class, 'css-merchant-2onvNofT css-1l533tl')]/div/a["+str(Product_sub_counting)+"]"
                Product_sub_html = self.Selenium.ExtractElementAttribute("href",xpath=subsub_html)
                self.Selenium.Load(Product_sub_html)
                self.Product_name = self.Selenium.ExtractElementText("//div[contains(@id,'content-container')]/div[2]/div/div/div/div[2]/h1/span")
                self.Product_price = int(Enumerate().CleanNumber(self.Selenium.ExtractElementText("//div[contains(@id,'content-container')]/div[2]/div/div/div/div[2]/div[5]/div/span[2]")))
                self.Product_sold = int(Enumerate().ReformToNumber(self.Selenium.ExtractElementText("//div[contains(@class, 'mt-30')]/div[contains(@class, 'rvm-product-info')]/div[2]/div/div[2]")))
                self.Product_rate = self.Selenium.ExtractElementText("//div[contains(@id,'content-container')]/div[2]/div/div/div/div[2]/div[2]/div/span")
                DB().InsertDB_Product(self.Product_name, self.Product_price, self.Product_sold, self.Product_rate, self.Merchant_html_path)
                self.Selenium.BackPage()
                print("insert")
        self.Selenium.Close()

def main():
    connected = sqlite3.connect('StoreData/DB_Merchant')
    cursors = connected.cursor()
    query = 'SELECT Merchant_html_path, Merchant_active_product FROM tableMerchant'
    cursors.execute(query)
    for row in cursors.fetchall():
        Run().CrawlingMerchantProduct()
    cursors.close()
    connected.close()
main()
