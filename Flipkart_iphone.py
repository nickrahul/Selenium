from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

lis=[]
class crawl:
    def __init__(self) -> None:
        driver=webdriver.Chrome("K:/Rahul_sharma/python/python/New folder/chromedriver.exe")
        driver.get("https://www.google.com")
        self.driver=driver
        time.sleep(2)
        # self.driver.maximize_window()
        self.search_website()

    def search_website(self):
        website=self.driver.find_element(By.CLASS_NAME,"gLFyf")
        website.send_keys("flipkart")
        time.sleep(1)
        website.submit()
        
        enter_website=self.driver.find_element(By.CLASS_NAME,"LC20lb.MBeuO.DKV0Md")
        enter_website.click()

        search_product=self.driver.find_element(By.CLASS_NAME,"Pke_EE")
        search_product.send_keys("iphone")
        time.sleep(1)
        search_product.submit()

        self.list_page()

    def list_page(self):
        links=self.driver.find_elements(By.CLASS_NAME,"tUxRFH")
        l=[]
        for i in links:
            link=i.find_element(By.CLASS_NAME,"CGtC98")
            link=link.get_attribute("href")
            l.append(link)
        self.detail_page(l)

    def detail_page(self,link):
        for i in link:
            self.driver.get(i)
            try:
                title=self.driver.find_element(By.CLASS_NAME,"_6EBuvT")
                title=title.text
            except:
                title="Not available"

            try:
                rating=self.driver.find_element(By.CLASS_NAME,"XQDdHH")
                rating=rating.text
            except:
                rating="Not available"

            try:
                price=self.driver.find_element(By.CLASS_NAME,"Nx9bqj.CxhGGd")
                price=price.text
            except:
                price="Not available"

            try:
                discount=self.driver.find_element(By.CLASS_NAME,"UkUFwK.WW8yVX")
                discount=discount.text
            except:
                discount="Not available"

            lis.append({
                "TITLE":title,
                "RATING":rating,
                "PRICE":price,
                "DISCOUNT":discount,
            })
        df=pd.DataFrame(lis)
        df.to_excel("K:/Rahul_sharma/python/python/flip.xlsx",index=False)
        self.driver.close()


crl=crawl()
