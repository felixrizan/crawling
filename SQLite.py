import sqlite3

class DB:
    def CreateDB(self):
        connected = sqlite3.connect('StoreData/DB_Merchant')
        cursors = connected.cursor()
        cursors.execute('''CREATE TABLE IF NOT EXISTS tableMerchant(
                                Merchant_name TEXT PRIMARY KEY NOT NULL,
                                Merchant_rate_point TEXT NOT NULL,
                                Merchant_location TEXT NOT NULL,
                                Merchant_established DATE NOT NULL,
                                Merchant_sold_product INT NOT NULL,
                                Merchant_succesful_transaction INT NOT NULL,
                                Merchant_showcase INT NOT NULL,
                                Merchant_active_product INT NOT NULL,
                                Merchant_followers INT NOT NULL,
                                Merchant_html_path TEXT NOT NULL,
                                Merchant_stat_1_month INT NOT NULL,
                                Merchant_stat_3_month INT NOT NULL,
                                Merchant_stat_12_month INT NOT NULL)''')
        cursors.execute('''CREATE TABLE IF NOT EXISTS tableProduct(
                                Product_name TEXT PRIMARY KEY NOT NULL,
                                Product_price INT NOT NULL,
                                Product_sold  INT NOT NULL,
                                Product_rate TEXT NOT NULL,
                                Product_merchant TEXT,
                                FOREIGN KEY (Product_merchant) REFERENCES tableMerchant (Merchant_html_path))''')
        connected.commit()
        cursors.close()
        connected.close()
    def InsertDB_Merchant(self,Merchant_name, Merchant_rate_point, Merchant_location, Merchant_established, Merchant_sold_product, Merchant_succesful_transaction, Merchant_showcase, Merchant_active_product, Merchant_followers, Merchant_html_path, Merchant_stat_1_month,Merchant_stat_3_month,Merchant_stat_12_month):
        connected = sqlite3.connect('StoreData/DB_Merchant')
        cursors = connected.cursor()
        cursors.execute("INSERT OR IGNORE INTO tableMerchant VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(Merchant_name, Merchant_rate_point, Merchant_location, Merchant_established, Merchant_sold_product, Merchant_succesful_transaction, Merchant_showcase, Merchant_active_product, Merchant_followers, Merchant_html_path, Merchant_stat_1_month,Merchant_stat_3_month,Merchant_stat_12_month))
        connected.commit()
        cursors.close()
        connected.close()
    def InsertDB_Product(self,Product_name, Product_price, Product_sold, Product_rate, Product_merchant):
        connected = sqlite3.connect('StoreData/DB_Merchant')
        cursors = connected.cursor()
        cursors.execute("INSERT OR IGNORE INTO tableProduct VALUES (?,?,?,?,?)",(Product_name, Product_price, Product_sold, Product_rate, Product_merchant))
        connected.commit()
        cursors.close()
        connected.close()
