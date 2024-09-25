from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
import pandas as pd



class Crawl:

    def __init__(self):


        # set chrome options
        options = Options()


        options.add_argument('--ignore-certificate-errors') # Ignore SSL errors
        options.add_argument('--allow-insecure-localhost') # Allow insecure connections
        # options.add_argument('--start-maximized') # Start maximized (optional)
        # options.add_experimental_option("excludeSwitches",["enable-automation"])
        # options.add_experimental_option("useAutomationExtension",False)
        # options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
        # options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
        # options.add_argument("--disable-notifications")  # Disable notifications pop-up
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


        service = Service("D:/Python/Selenium/Selenium_Drivers/chromedriver.exe")

        self.driver = webdriver.Chrome(service=service , options=options)

        self.wait = WebDriverWait(self.driver , 10)

        self.website_main_page()

        self.driver.quit()
    

    def website_main_page(self):
        self.dataaa = []

        self.driver.get("http://yellowpages.in/")

        # self.main_page_url = self.driver.current_url

        main_links = []

        for i in self.driver.find_element(By.ID,"ulCats").find_elements(By.TAG_NAME,"li"):
            urls = (i.find_element(By.TAG_NAME,"a").get_attribute("href"))
            main_links.append(urls)

        for i in main_links:
            self.list_page(i)
        
        df = pd.Series(self.dataaa,name="Urls")
        df.to_excel("yellow.xlsx",index=False)

            

    def list_page(self,urls):

        self.driver.get(urls)

        # for i in self.driver.find_elements(By.CLASS_NAME,"popularTitleTextBlock"):
        #     list_page_ulrs = (i.find_element(By.TAG_NAME,"a").get_attribute("href"))

        self.load_more_btn()


    def load_more_btn(self):

        while True:
            try:
                # btn = self.driver.find_element(By.CLASS_NAME, "loadMoreBtn")  # Find the element you want to scroll to
                # btnn = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"loadMoreBtn")))
                radi = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"loadMoreBtn")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", radi) # Scroll to the element
                sleep(2)
                radi.click()
                sleep(5)
            except StaleElementReferenceException :
                print("Element became stale. Retrying...")
                continue
            except:
                break
                

        links = []

        for i in self.driver.find_elements(By.CLASS_NAME,"popularTitleTextBlock"):
            list_page_ulrs = i.find_element(By.TAG_NAME,"a").get_attribute("href")
            links.append(list_page_ulrs)
        print(len(links))
        self.dataaa.extend(links)
        
        for j in links:
            self.detail_page(j)


    def detail_page(self,j):

        self.driver.get(j)

        try:
            title = self.driver.find_element(By.ID,"MainContent_h1").text
        except:
            title = None

        try:
            review = self.driver.find_element(By.ID,"MainContent_aRev1").text
        except:
            review = None

        try:
            pho_no = self.driver.find_element(By.ID,"MainContent_aTel").text
        except:
            pho_no = None
        
        try:
            address = self.driver.find_element(By.XPATH,"/html/body/form/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div/address").text.replace("\n"," ")
        except:
            address = None

        try:
            timings = {}
            days = self.driver.find_elements(By.CLASS_NAME,"dayDisplay")
            timee = self.driver.find_elements(By.CLASS_NAME,"timeDisplay")

            for i,j in zip(days,timee):
                timings.update({i.text:j.text})
        except:
            timings = None

        try:
            listed = self.driver.find_element(By.ID,"MainContent_ulCats").find_elements(By.TAG_NAME,"a")
            liste = []
            for i in listed:
                liste.append(i.text)
            liste = " , ".join(liste)

        except:
            liste = None

        data = {}
        data.update({"Title":title,"Review":review,"Phone_No":pho_no,"Address":address,"Listed":liste})
        data.update(timings)
        self.dataaa.append(data)
        print(len(self.dataaa))



        

crl = Crawl()


