from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Step 1: Setup headless Chrome (remove headless if you want to see browser)
options = Options()
options.add_argument("--headless")  # comment this line out to watch it work in a window

# Step 2: Point to your chromedriver.exe
service = Service("C:/Users/Johnny Blaze/ChromeDriver/chromedriver-win64/chromedriver.exe")

# Step 3: Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Step 4: Go to UFC events page
driver.get("https://www.ufc.com/events")
time.sleep(5)  # Give it time to load the JS

# Step 5: Print the page title
print("Page title:", driver.title)

# Step 6: Close browser
driver.quit()