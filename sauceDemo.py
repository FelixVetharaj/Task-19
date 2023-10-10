from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Sauce:

    #Constructor parameter
    def __init__(self, url):
        self.url = url
        #Install latest web driver manager
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # method to login 
    def login(self):
        try:
            #get the url
            self.driver.get(self.url)
            sleep(4)
            #Print the title in the url
            print(self.driver.title)
            #print the current url
            print(self.driver.current_url)
            # send the user email Id
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            sleep(4)
            #send the user password. In the Task it is given standard_user which is wrong password in the page correct password secret_sauce is given
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            sleep(4)
            #Click the login button
            self.driver.find_element(By.ID, "login-button").click()
            sleep(4)
            #Get the entire content of webpage
            text = self.driver.find_element(by=By.XPATH, value="/html/body").text
            print(text)

            #store the entire content of webpage in a txt file
            f = open("Webpage_task_11.txt", "w+")
            f.write(text)
            f.close()
        #exception handling. If element used in try is not found it throws a exception
        except NoSuchElementException as error:
            print("Element not found", error)

        #close the last opened webpage
        finally:
            self.driver.close()

url = "https://www.saucedemo.com/"
s = Sauce(url)
s.login()


