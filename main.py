from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open the login page
driver.get("https://performance.pressganey.com/")

# Wait for the page to load
time.sleep(3)

# Find the email input field and enter the email
email_input = driver.find_element_by_id("email")
email_input.send_keys("anil.kumara@pressganey.com")

# Click on the next button
next_button = driver.find_element_by_id("next")
next_button.click()

# Wait for the login to complete
time.sleep(5)

# Check if login was successful
if "performance.pressganey.com/home" in driver.current_url:
    print("Login success")
else:
    print("Login failed")

# Open the links in new tabs
links = [
    "https://reputation-jobs1.consumerism.pressganey.com/admin/resources/RefreshList.jsp",
    "https://reputation-jobs2.consumerism.pressganey.com/admin/resources/RefreshList.jsp",
    "https://reputation-jobs3.consumerism.pressganey.com/admin/resources/RefreshList.jsp",
    "https://reputation-jobs4.consumerism.pressganey.com/admin/resources/RefreshList.jsp"
]

for link in links:
    driver.execute_script(f"window.open('{link}', 'new_window')")
    time.sleep(2)

# Check status codes for each link
for i, link in enumerate(links, start=1):
    driver.switch_to.window(driver.window_handles[i])
    driver.get(link)
    status_code = driver.execute_script("return window.performance.getEntries()[0].response.status;")
    if status_code == 200:
        print(f"Server {i} is good")
    else:
        print(f"Server {i} is having issues (Status code: {status_code})")

# Close the browser
driver.quit()
