from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class orange:

    url = 'https://opensource-demo.orangehrmlive.com/'

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    sleep(5)

    def login(self):

        #get the  input user lodin data
        username='Admin'
        password='admin123'
        
        #location of elements data

        user_name = 'username'
        password_name ='password'
        login_class ='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

        self.driver.get(self.url)
        sleep(5)
        #find the title of website name
        title = self.driver.title

        print(title)

        self.driver.find_element(By.NAME, value=user_name).send_keys(username)
        self.driver.find_element(By.NAME, value=password_name).send_keys(password)
        login=self.driver.find_element(By.XPATH, login_class)
        login.click()
        sleep(8)
        
        
#---------------------- pim panel button------------------------------------
        
    def add_button(self):

         pim_button=self.driver.find_element(by=By.XPATH, value= "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]")
         pim_button.click()
         print('clicked on pim button')
         sleep(2)
# add_button
         addbutton=self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
         addbutton.click()
        
         sleep(2)
         
#first name form
         self.driver.find_element(by=By.NAME,value='firstName').send_keys('Mohamed')
#second name form        
         self.driver.find_element(by=By.NAME,value='lastName').send_keys('Hilmas')
 #login detAIL button   

         log_detail='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
        
         log_detail=self.driver.find_element(by=By.XPATH,value=log_detail)

         log_detail.click()
         


#create user name  
         username_pim='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
         status_box ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
         creat_pwd ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
         confirm_pwd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
        
         save ="//button[@type='submit']"

         username_pim =self.driver.find_element(by=By.XPATH,value=username_pim)
         username_pim.send_keys('Hilmas')

         status_box= self.driver.find_element(by=By.XPATH,value=status_box)
         status_box.click()
         creat_pwd = self.driver.find_element(by=By.XPATH,value=creat_pwd)
         creat_pwd.send_keys('Admin@123')
         confirm_pwd = self.driver.find_element(by=By.XPATH,value=confirm_pwd)
         confirm_pwd.send_keys('Admin@123')
         save=self.driver.find_element(by=By.XPATH,value=save)
         save.click()
         sleep(2)
         
         print('///////////////////NEW USER CREATED///////////////')

 ####------------------------Admin panel----------------------------------------------------------------------------
    def adminpanel(self): 

         self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
 
        #search username
         sleep(4)

         user_search =self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
         user_search.click()
         name= 'Hilmas'
         user_search.send_keys(name)
        
         #search button
         
         search_button=self.driver.find_element(by=By.XPATH,value=' //*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
         search_button.click()

  
               
         logout_dropdown= self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i')
         logout_dropdown.click()

         logout_dropdown_list =self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')
         logout_dropdown_list.click()
        
        
         
         print('///////////////////USER FOUNDED///////////////')
                
    

    def nlogin(self):
                username='Hilmas'
                password='admin@123'
        
         #location of elements

                user_name = 'username'
                password_name ='password'
                login_class ='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

                

        

                user_name= self.driver.find_element(By.NAME, value=user_name)
                sleep(2)
                user_name.send_keys(username)
                password_name= self.driver.find_element(By.NAME, value=password_name)
                sleep(1)
                password_name.send_keys(password)
                login_class=self.driver.find_element(By.XPATH, login_class)
                sleep(1)
                login_class.click()
                sleep(3)
                self.driver.close()
                L= '---------------------------------------PASSED----------------------------------'        
                print(L)
               
      
o = orange()
o.login()
o.add_button()
o.adminpanel()
o.nlogin()