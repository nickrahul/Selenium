from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


class Scraping:
    def __init__(self,products) -> None:
        self.data=[]
        self.driver=webdriver.Chrome("chromedriver.exe")
        time.sleep(1)
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()
        time.sleep(1)
        self.search_product(products)
        df=pd.DataFrame(self.data)
        df.to_excel("Flip.xlsx")

    def search_product(self,products):
        product=self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input")
        product.send_keys(products)
        time.sleep(1)
        product.send_keys(Keys.ENTER)
        self.list_page()


    def list_page(self):
        l=[]
        url=self.driver.current_url
        e=1
        while True:
            if e==5:
                break
            e+=1
            self.driver.get(url)
            time.sleep(2)
            links=self.driver.find_elements(By.CLASS_NAME,"tUxRFH")
            for i in self.driver.find_elements(By.CLASS_NAME,"tUxRFH"):
                link=i.find_element(By.CLASS_NAME,"CGtC98").get_attribute("href")
                l.append(link)
            self.detail_page(l)
            if len(links)==24:
                self.driver.get(url)
                time.sleep(2)
                if self.driver.find_elements(By.CLASS_NAME,"_9QVEpD")[-1]:
                    url=self.driver.find_elements(By.CLASS_NAME,"_9QVEpD")[-1].get_attribute("href")
                    print(url)
                else:
                    break
            else:
                break


    def detail_page(self,url):
        for i in url:
            self.driver.get(i)
            try:
                title=self.driver.find_element(By.CLASS_NAME,"_6EBuvT").text
            except:
                title="Not available"
                
            try:
                rating=self.driver.find_element(By.CLASS_NAME,"XQDdHH").text
            except:
                rating="Not available"

            try:
                price=self.driver.find_element(By.CLASS_NAME,"Nx9bqj.CxhGGd").text
            except:
                price="Not available"

            try:
                discount=self.driver.find_element(By.CLASS_NAME,"UkUFwK.WW8yVX").text
            except:
                discount="Not available"

            try:
                variant=[]
                storage=self.driver.find_elements(By.CLASS_NAME,"CDDksN")
                for i in storage:
                    variant.append(i.text)
            except:
                variant="Not available"

            # try:
            #     images_link=[]
            #     images=self.driver.find_elements(By.CLASS_NAME,"YGoYIP.Ueh1GZ")
            #     for i in images:
            #         images_link.append(i.get_attribute("href"))
            # except:
            #     images_link="Not available"

            self.data.append({
                "Title":title,
                "RATING":rating,
                "PRICE":price,
                "DISCOUNT":discount,
                "STORAGE_VARIANT":variant,
                # "IMAGES_LINK":images_link
            })



products=input("Enter product name:-------->")
scr=Scraping(products)


