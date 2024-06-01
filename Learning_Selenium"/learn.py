from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

s=Service("chromedriver.exe")

# create instane of webdriver class
driver=webdriver.Chrome(service=s)

# open url in browser through get
driver.get("https://omayo.blogspot.com/")

####################################################################
Some Operation With Selenium


# for maximize browser
driver.maximize_window()

# View the Web Page in Full Screen Mode
driver.fullscreen_window()

# for minimize browser
driver.minimize_window()

# Set the size of a window 
driver.set_window_size(width,height)

# for refresh browser page
driver.refresh()

# go to back page
driver.back()

# got to forward page
driver.forward()

# clearing text from text fields
driver.find_element().clear()

# get current page title
tit=driver.title
print(tit)

# get current page url
url=driver.current_url
print(url)

# Retrieving the HTML Source Code of the Web Page
driver.page_source

####################################################################
Searching element With Different Method ===>


driver.find_element()

# search element by ID
driver.find_element(By.ID,"ta1").send_keys("My Name is Rahul.")

# search element by NAME
driver.find_element(By.NAME,"q").send_keys("Rahul Sharma")

# search element by CLASS_NAME
driver.find_element(By.CLASS_NAME,"dropbtn").click()

# search element by LINK_TEXT
driver.find_element(By.LINK_TEXT,"jqueryui").click()

# search element by XPATH
driver.find_element(By.XPATH,"//input[@value='Login']").click()

# search element by CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"input[value='Login']").click()

# search element by TAG_NAME
driver.find_element(By.TAG_NAME,"a")

####################################################################
Finding multiple elements on the web page  { GIVE RESULT AS A LIST }


# Searching elements by ID
driver.find_elements(By.ID,"ta1").send_keys("My Name is Rahul.")

# Searching elements by NAME
driver.find_elements(By.NAME,"q").send_keys("Rahul Sharma")

# Searching elements by CLASS_NAME
driver.find_elements(By.CLASS_NAME,"dropbtn").click()

# Searching elements by LINK_TEXT
driver.find_elements(By.LINK_TEXT,"jqueryui").click()

# Searching elements by XPATH
driver.find_elements(By.XPATH,"//input[@value='Login']").click()

# Searching elements by CSS_SELECTOR
driver.find_elements(By.CSS_SELECTOR,"input[value='Login']").click()

# Searching elements by TAG_NAME
driver.find_elements(By.TAG_NAME,"a")

eg====>
for i in driver.find_element(By.ID,"multiselect1").find_elements(By.TAG_NAME,"option"):
    print(i.text)

####################################################################
Clicking Drifferent Types of Web Elements Like ===> 


> Button
> Link
> Checkbox field
> Text Fields 
> Dropdown Field
> etc.
  
driver.find_element().click()

####################################################################
Typing Text Into Text Fields Like ===>
  

> Text Box
> Text Area 
> Password

driver.find_element().send_keys("My Name is Rahul.\nI Live in Amritsar.)

###################################################################
> Storing the Element to a varible to perform multiple operations
                                

text_box=driver.find_elements(By.ID,"textbox1")

text_box.clear()

text_box.send_keys("Arun")

text_box.clear()

####################################################################
Retrieving Text from HTML tags


driver.find_element().text

tex=driver.find_element(By.ID,"pah").text
print(tex)

####################################################################
Closing the current browser window  [ If we click on a link and open another tab (its child tab) but my current window is parent window ]


driver.close()

####################################################################
Closing all browser window


driver.quit()

####################################################################
Retrieving the value of any HTML elements attribute [ get attribute value ]


driver.find_element().get_attribute()

tex=driver.find_element(By.ID,"link2").get_attribute("href")
print(tex)

####################################################################
Checking whether the element is displayed on the page 


driver.find_element().is_displayed()

####################################################################
Checking whether the element is enabled or disabled


driver.find_element().is_enabled()

####################################################################
Checking the selection status of radio buttons and check box fields 


driver.find_element().is_selected()

####################################################################
Submitting the form


driver.find_element().submit()

####################################################################
Taking screen shot of the web page


driver.save_screenshot("filename.png")

driver.get_screenshot_as_file()

####################################################################
Retrieving the HTML tag name of Web Element


driver.find_element().tag_name

####################################################################
Finding the size of the web element  [ Result will be return as Dictionary ]


siz=driver.find_element().size

print(siz) [ give both height and width ]

print(siz.get("height"))   [ give only height ]

####################################################################
Finding the location of the Web Element  [ Result will be return as Dictionary ]


loc=driver.fin_element().location

print(loc) [ give both x and y cordinates ]

print(loc.get("x"))   [ give only x cordinates values ]

####################################################################
Finding both size and location of the Web Element


rec=driver.find_element().rect
[ It Consists 4 key value pair ( x,y,height,width )


####################################################################
Setting page load time out for the website to open


driver.set_page_load_timeout(give time in seconds)
[ set before driver.get(url) ]

####################################################################
####################################################################
Handling JavaScript Alerts

Types of alert ===>

> Information Alerts
> Confirmation Alerts
> Prompt Alerts 


info_alert=driver.switch_to.alert
info_alert.text
info_alert.accept()
info_alert.dismiss()


Information Alerts eg = = = >

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

time.sleep(1)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[1]/button").click()

time.sleep(2)

info_alert=driver.switch_to.alert

print(info_alert.text)

info_alert.accept()

###################################

Confirmation Alerts eg = = = >

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[2]/button").click()

time.sleep(2)

aa=driver.switch_to.alert

aa.accept()

aa.dismiss()

NoAlertPresentException [ will come if no alert show on web page ]

###################################

Prompt Alerts eg = = = >

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[3]/button").click()

aa=driver.switch_to.alert

print(aa.text)

aa.send_keys("Rahul Sharma")

aa.accept()

######################################################################
Handing Web Push Notifications   [ where allow and block pop show ]


from selenium.webdriver.chrome.options import Options

s=Service("chromedriver.exe")

opt=Options()

opt.add_argument("--disable-notifications")

driver=webdriver.Chrome(service=s,options=opt)

######################################################################
######################################################################
Handling Bootstrap Model Dialogs 

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://getbootstrap.com/docs/4.0/components/modal/")

time.sleep(3)

driver.find_element(By.XPATH,"/html/body/div/div/main/div[6]/button").click()

wait=WebDriverWait(driver,30)

heading=wait.until(EC.visibility_of_element_located((By.ID,"exampleModalLiveLabel")))

print(heading.text)

text1=driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[5]/div/div/div[2]/p")

print(text1.text)

driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[5]/div/div/div[3]/button[1]").click()

#######################################################################
Default Page Load Timeout for web pages


> selenium wait 5 minutes to load page

#######################################################################
Handling HTML Dropdown  { SELECT CLASS WORKING ON <SELECT> ELEMENT }

  
from selenium.webdriver.support.select import Select


3 commands to select dropdown web element

> select_by_visible_text()
> select_by_index()
> select_by_value()


driver.get("https://omayo.blogspot.com/")

drop_=driver.find_element(By.ID,"drop1")


> create an object for select class

select_=Select(drop_)

select_.select_by_visible_text()


2 more commands   
       
> is_multiple
> options

print(select_.is_multiple)  [ Gives True is selected Multiple items ]
       

ab=select.options

for i in ab:
    if i.text=="doc 4":
        select.select_by_visible_text(i.text)


[ Below code is for get text selected element ]
print(select.first_selected_option.text)

##############################################################################
Handling Multi selection box fields List Box 


commands  = = = >

> select_by_visible_text()
> select_by_index()
> select_by_value()
> deselect_by_index()
> deselect_by_value()
> deselect_all()
> is_multiple
> options
> first_selected_option
> all_selected_options


driver.get("https://omayo.blogspot.com/")

driver.maximize_window()

time.sleep(3)

hey=driver.find_element(By.ID,"multiselect1")

time.sleep(1)

select=Select(hey)

select.select_by_index(1)
select.select_by_value("volvox")
select.select_by_visible_text("Audi")

time.sleep(5)
select.deselect_by_visible_text("Audi")

ab=select.all_selected_options

for j in ab:
  print(j.text)

##################################################################
Handling Bootstrap dropdown fields [ Normal dropdown we can see a <select> tag but in Bootstrap multiple links available in Bootstrap Button ]


driver.get("https://getbootstrap.com/docs/4.0/components/dropdowns/")

driver.find_element(By.ID,"dropdownMenuButton").click()

driver.find_element(By.LINK_TEXT,"Action").click()

##################################################################
Handling JQuery dropdown  [ In jquery dropdown we can see multiple sub options ]


[ IT IS A SIMPLE AS ABOVE WE CAN DO JUST FIND ELEMENT AND CLICK ON IT ]

#################################################################
Handling Radio buttons and Checkbox fields


2 commands  = = = >    

is_selected()
click()


driver.get("https://omayo.blogspot.com/")

btn=driver.find_element(By.ID,"checkbox2")

if btn.is_selected:
  pass
else:
  btn.click()

#################################################################
Handling StaleElementReferenceException


[ WHEN YOU NAVIGATE AWAY FROM THE PAGE WHERE THE ELEMENT IS LOCATED , AFTER COMING BACK TO THE SAME PAGE , THE OBJECT REFERENCE IS NO MORE REFERRING TO THE OBJECT OF WEB ELEMENT . ]

driver.find_element().send_keys()

time.sleep(1)

driver.find_element().click()

time.sleep(1)

driver.back()

time.sleep(1)

[ same element as above ]
driver.find_element().clear

#################################################################
Handling iframes and frames


> Iframes is one of the tags available in html.
> Using Iframes we can embed another html page in a HTML page.


driver.switch_to.frame()
  

Different ways we can switch to the frames

> using id locater of frame
> using name locater of frame
> using webelement of frame
> using index of a frame


driver.get("https://omayo.blogspot.com/")

time.sleep(2)

driver.switch_to.frame("iframe1")

time.sleep(1)

a=driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[2]/div[2]/footer/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/a/img").get_attribute("src")

##########################################################################
Handling Nested Frames


> driver.switch_to.parent_frame() [ it is switch to parent frame ]
> driver.switch_to.default_content() [ we can go easily main outer page ]


driver.get("https://letcode.in/frame")

driver.maximize_window()


time.sleep(2)

driver.switch_to.frame(0)

time.sleep(2)

driver.find_element(By.NAME,"fname").send_keys("rahul")

time.sleep(2)

ab=driver.find_element(By.XPATH,"/html/body/app-root/app-frame-content/div/div/div/iframe")

driver.switch_to.frame(ab)

time.sleep(1)

driver.find_element(By.NAME,"email").send_keys("Rs5537929@gmail.com")

time.sleep(1)

driver.switch_to.parent_frame()

time.sleep(1)

driver.find_element(By.NAME,"fname").clear()

time.sleep(1)

driver.switch_to.default_content()

driver.find_element(By.XPATH,"/html/body/app-root/app-frames/section[1]/div/div/div[2]/app-learning-point/div/footer/a").click()

########################################################################
Handling InfoBar


s=Service("chromedriver.exe")
opt=Options()

opt.add_experimental_option("excludeSwitches",["enable-automation"])

opt.add_experimental_option("useAutomationExtension",False)

opt.add_argument("--disable-blink-features=AutomationControlled")


driver=webdriver.Chrome(service=s,options=opt)


# Disable the Info Bar and Automation Controls:

> opt.add_experimental_option("excludeSwitches", ["enable-automation"]): This removes the "enable-automation" switch, 
which helps in hiding the Chrome is being controlled by automated test software" infobar.

> opt.add_experimental_option("useAutomationExtension", False): This disables the automation extension, 
further preventing the detection of the automated browser.

> This feature, when enabled, indicates that the browser is being controlled by automation software, 
which can lead to the display of messages like "Chrome is being controlled by automated test software." 
Disabling this feature helps in making the browser less detectable as being controlled by automation tools like Selenium.
  
#########################################################################
Handling Mouse Events


from selenium.webdriver import ActionChains

actions=ActionChains(driver)
perform()

driver=webdriver.Chrome(service=s,options=opt)

driver.get("https:tickets.manutd.com/")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.ID,"accept-btn").click()

actions=ActionChains(driver)

tickets=driver.find_element(By.XPATH,"/html/body/div[7]/div[4]/div/ul/li[1]/a")

actions.move_to_element(tickets).perform()

#######################################################################
Hovering Mouse

move_to_element()

driver=webdriver.Chrome(service=s,options=opt)

# driver.get("https://omayo.blogspot.com/")

driver.get("https:tickets.manutd.com/")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.ID,"accept-btn").click()

actions=ActionChains(driver)

tickets=driver.find_element(By.XPATH,"/html/body/div[7]/div[4]/div/ul/li[1]/a")

actions.move_to_element(tickets).perform()

time.sleep(2)

mens_tickets=driver.find_element(By.XPATH,"/html/body/div[7]/div[4]/div/ul/li[1]/ul/li[1]/a")

actions.move_to_element(mens_tickets).perform()

mens_tickets.click()

##################################################################
Mouse Left Click


click()

driver.get("https://omayo.blogspot.com/")

actions=ActionChains(driver)

link=driver.find_element(By.ID,"link1")

time.sleep(3)

actions.click(link).perform()

#################################################################
Handling Slider

actions=ActionChains(driver)

actions.drag_and_drop_by_offset(element_name,x-offset,y-offset)



driver.get("https://omayo.blogspot.com/p/page3.html")

time.sleep(5)

min_slider=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/form/div/div/div[2]/a[1]")

time.sleep(2)

actions=ActionChains(driver)

actions.drag_and_drop_by_offset(min_slider,-100,0).perform()

################################################################
Mouse Right Click


context_click()


driver.get("http://tutorialsninja.com/demo/")

time.sleep(4)

driver.maximize_window()

time.sleep(2)

actions=ActionChains(driver)

inp=driver.find_element(By.XPATH,"/html/body/header/div/div/div[2]/div/input")

actions.context_click(inp).perform()

##############################################################
Mouse Double Click


double_click()


driver.get("https://omayo.blogspot.com/")

time.sleep(4)

driver.maximize_window()

time.sleep(2)

ab=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div[1]/div[17]/div[1]/p[1]")

actions=ActionChains(driver)

time.sleep(5)

actions.double_click(ab).perform()

#############################################################
Mouse Click Hold and Release


click_and_hold()
release()
click_and_hold(element1).move_to_element(element2).release()



actions=ActionChains(driver)


driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

time.sleep(4)

driver.maximize_window()

time.sleep(3)

ele1=driver.find_element(By.ID,"box1")

ele2=driver.find_element(By.ID,"box102")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

time.sleep(5)


ele1=driver.find_element(By.ID,"box2")

ele2=driver.find_element(By.ID,"box104")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

time.sleep(5)

ele1=driver.find_element(By.ID,"box3")

ele2=driver.find_element(By.ID,"box107")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

time.sleep(5)

ele1=driver.find_element(By.ID,"box4")

ele2=driver.find_element(By.ID,"box103")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

time.sleep(5)

ele1=driver.find_element(By.ID,"box5")

ele2=driver.find_element(By.ID,"box105")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

time.sleep(5)

ele1=driver.find_element(By.ID,"box6")

ele2=driver.find_element(By.ID,"box101")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

time.sleep(5)

ele1=driver.find_element(By.ID,"box7")

ele2=driver.find_element(By.ID,"box106")

actions.click_and_hold(ele1).move_to_element(ele2).release().perform()

#########################################################################
Mouse Drag and Drop


[ Above code is lengthy ]

[ Below code is Simple ]

actions=ActionChains(driver)


driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

time.sleep(4)

driver.maximize_window()

time.sleep(3)

ele1=driver.find_element(By.ID,"box2")

ele2=driver.find_element(By.ID,"box104")

time.sleep(5)

actions.drag_and_drop(ele1,ele2).perform()

########################################################################
########################################################################
Keys class


driver.get("http://tutorialsninja.com/demo/index.php?route=account/login")

driver.maximize_window()

driver.find_element(By.ID,"input-email").send_keys("amotooricap9@gmail.com")

driver.find_element(By.ID,"input-password").send_keys("12345")

time.sleep(5)

actions.send_keys(Keys.ENTER).perform()

#######################################################################
key down and key up commands


driver.get("https://omayo.blogspot.com/")
actions=ActionChains(driver)

driver.maximize_window()

time.sleep(5)

link=driver.find_element(By.ID,"LinkList1").find_elements(By.TAG_NAME,"a")

for i in link:
    actions=ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(i).key_up(Keys.CONTROL).perform()

######################################################################
Handling Auto suggestive Dropdowns


driver.get("https://www.makemytrip.com/")

driver.find_element(By.ID,enter id).send_keys("g")

actions=ActionChains(driver)

actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.Enter).perform()

######################################################################
Resizing an element


driver.get("https://www.jqueryui.com/resizable/")

driver.maximize_window()

time.sleep(2)

fr=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[1]/iframe")

time.sleep(2)

driver.switch_to.frame(fr)

actions=ActionChains(driver)

dd=driver.find_element(By.XPATH,"/html/body/div/div[3]")

actions.drag_and_drop_by_offset(dd,80,100).perform()

#####################################################################
Handling JQuery Right Click Menu



