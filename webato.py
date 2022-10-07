from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

PATH="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/login/")
driver.maximize_window()
#For User id autofill
username = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID,"username"))).send_keys('mishrasipun17@gmail.com')
#username = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='username']"))).send_keys('arif@gmail.com')
time.sleep(3)

#For password autofill
password = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='password']")))
time.sleep(3)

with open(r"C:\Users\sipun\Downloads\password.txt",'r') as myfile:
    passw=myfile.read()
password.send_keys(passw)

time.sleep(2)


#For login click
login =  WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='organic-div']/form/div[3]/button"))).click()
time.sleep(2)


#for removing pop up notificataions
#chrome_options = Options()
#chrome_options.add_arguments("--disable-notifications")
#driver = webdriver.Chrome(PATH, options = chrome_options)


#For search
account = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='global-nav-typeahead']/input"))).send_keys("Sequelstring")
acc_click = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='global-nav-typeahead']/input"))).send_keys(Keys.RETURN)
#profile
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='main']/div/div/div[2]/div/a/div/div[1]/div[1]/div/div/span/span/a"))).click()
#about
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/nav/ul/li[2]/a"))).click()
#scroll
driver.execute_script("window.scrollTo(1000, 500)")

#For Take Texts
seq_website = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[1]/a/span"))).text
print("Sequelstring Website",seq_website)
industry = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[3]"))).text
print("industry = ",industry)
headquarters = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[6]"))).text
print("Headquarter = ",headquarters)
c_size = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div/div[1]/section/dl/dd[4]"))).text
print("Company_Size = ",c_size)
#print(username)
#driver.quit()
