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

driver = webdriver.Edge(service=Service(executable_path='C:/Users/rayvi/Desktop/msedgedriver.exe'))


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

    # Print the site's code
    html_content = driver.page_source

    # Create BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')


    # Print the HTML content
    text = soup.get_text()
    # print(text)
    txt = text

    filename = input("Enter file name you want to create: ")
    fn = filename + ".html"
    fntxt = filename + ".txt"


    id_start = txt.find("STUDENT ID: ") + len("STUDENT ID: ")
    id_end = txt.find("STUDENT NAME: ")
    id = txt[id_start:id_end].strip()

    name_start = id_end + len("STUDENT NAME: ")
    name_end = txt.find("If you")
    name = txt[name_start:name_end].strip()

    print("STUDENT ID:", id)
    print("STUDENT NAME:", name + "\n\n")


    # Find all section elements inside the div
    section_tr = soup.find_all('section')


    t = open(fntxt, "x")
    t = open(fntxt, "w")
    t.write("STUDENT ID: " + id + "\nSTUDENT NAME: " + name + "\n")

    # Iterate through section elements and find tr elements
    for section in section_tr:
        t.write("\n")
        print("\n")
        all_tr = section.find_all('tr')

        # Extract the contents of each section
        for tr in all_tr:
            tr_text = tr.get_text(strip=True)
            if (tr_text == "Subject CodeDescriptionGrade"):
                t.write("Subject Code          Description          Grade\n")
                print("Subject Code          Description          Grade\n")
            else:
                t.write(tr_text + "\n")
                print(tr_text + "\n")
    t.close()

    f = open(fn, "x")
    f = open(fn, "w")
    f.write(html_content)
    f.close()

    print("Successful task!")

    input()



# Main function
def main():
    username = input("Enter username: ")  # Replace with the user's username
    password = input("Enter password: ")  # Replace with the user's password

    login(username, password)
 
if __name__ == "__main__":
    main()
