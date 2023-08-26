# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time


edge_options = Options()
edge_options.use_chromium = True
edge_options.set_capability("timeouts", {"connect": 5000})  # Set the connect timeout to 5 seconds

driver = webdriver.Edge(service=Service(executable_path='SET DESTINATION EDGEDRIVER'))


# Function to log into the specific website
def login(username, password):
    driver.get("http://wmsu.edu.ph")  # Replace with the URL of the website you want to log in to

    loginbox = driver.find_element(By.ID, "login-button")
    loginbox.click()

    # Locate the email and password fields and submit button
    username_field = driver.find_element(By.ID, "username_id")  # Replace with the actual ID of the email field
    password_field = driver.find_element(By.ID, "password")  # Replace with the actual ID of the password field
    submit_button = driver.find_element(By.ID, "loginbutton")  # Replace with the actual ID of the submit button
    
    # Input email and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click the submit button
    submit_button.click()


    time.sleep(3)
    
    driver.get('http://wmsu.edu.ph/mywmsu/grade/grades.php')

    '''
    # Parsing the HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Print the HTML content
    text = soup.get_text()
    print(text)
    '''

    # Print the site's code
    html_content = driver.page_source

    filename = input("Enter file name you want to create: ")

    fn = filename + ".html"

    f = open(fn, "x")
    f = open(fn, "w")
    f.write(html_content)
    f.close()

    print("Successful task!")

    input()



# Main function
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    login(username, password)
 
if __name__ == "__main__":
    main()
