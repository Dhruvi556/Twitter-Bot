from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from getpass import getpass
from PIL import Image,ImageTk
from tkinter import filedialog
from time import sleep
import tkinter as tk
from tkinter import *
import webbrowser
from selenium.webdriver.support.select import Select 

class TBot:
    def __init__(self, username, password, choice, message, filepath, imgDescrp, DescOpt):

        self.driver = webdriver.Chrome("C:\\Users\\DHRUVI\\Desktop\\Twitter\\chromedriver.exe")  
        self.username = username                                            
        self.password = password
        self.choice = choice
        self.message = message
        self.filepath = filepath
        self.imgDescrp = imgDescrp
        self.DescOpt = DescOpt
       
        
        self.driver.get("https://twitter.com/login")                 #To open Twitter Log-in page           
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"session[username_or_email]\"]").send_keys(username)        #To enter username

        self.driver.find_element_by_xpath("//input[@name=\"session[password]\"]").send_keys(password)        #To enter password

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()      #To click Log-in button
        sleep(2)

        if(choice == 0):

            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div").send_keys(message) #To enter message
            sleep(1)

            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span').click() #To click Tweet button

        elif(choice == 1):
            self.driver.execute_script("window.open('');")                                                  #To open a new tab
            self.driver.switch_to.window(self.driver.window_handles[1])                                     #To switch to the new tab
            self.driver.get(filepath)
            img = self.driver.find_element_by_xpath('/html/body/img')
            
            actionChains = ActionChains(self.driver)
            actionChains.move_to_element(img).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  #To copy image to the new tab
            self.driver.switch_to.window(self.driver.window_handles[0])                                             #To switch to original Instagram tab
            sleep(2)

            self.driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(Keys.CONTROL + "v")      #To paste image in the original tab
            sleep(1)

            if (DescOpt.lower() == "Yes".lower()):
                self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div").send_keys(imgDescrp) #To enter image description
            sleep(1)
                
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span').click() #To click Tweet button
        
username = input("Enter username/email/phone: ")
password = getpass("Password: ")
choice = input("Text or Image: ")

if (choice.lower() == "Text".lower()):
    message=input("Enter message: ")
    my_bot = TBot(username,password, 0, message,"", "", "")
elif (choice.lower() == "image".lower()):
    msg = input("Description of image? Yes or No: ")
        
    if (msg.lower() == "Yes".lower()):
        Message1 = input("Description: ")
    else:
        Message1 = ""
        
    root = tk.Tk()
    root.withdraw()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))    #To open dialogbox to select files
    print (root.filename)
    imageName = "file:///" + root.filename
    my_bot = TBot(username,password, 1, "",imageName, Message1, msg)

else:
    print("Please enter valid choice! ")

