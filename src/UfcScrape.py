from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Setup
options = Options()
options.add_argument("--headless")
service = Service(r"C:\Users\Johnny Blaze\ChromeDriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Go to UFC events page
driver.get("https://www.ufc.com/events")
time.sleep(2)

# Parse page
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Today's date (for comparison)
today = datetime.today()

# Get all event cards
event_cards = soup.find_all("div", class_="c-card-event--result__info")

for card in event_cards:
    title = card.find("h3", class_="c-card-event--result__headline")
    date_div = card.find("div", class_="c-card-event--result__date")
    location = card.find("div", class_="c-card-event--result__location")
    link_tag = card.find_parent("a")
    href = link_tag["href"] if link_tag and link_tag.has_attr("href") else None
    detail_url = f"https://www.ufc.com{href}" if href else "N/A"

    if date_div:
        date_text = date_div.text.strip().split("/")[0].strip()  # get the first part like "Sat, Apr 6"
        try:
            parsed_date = datetime.strptime(date_text, "%a, %b %d")
            # Add the current year
            parsed_date = parsed_date.replace(year=today.year)
            if parsed_date >= today:
                print("-----------------------------")
                print(f"Title: {title.text.strip() if title else 'N/A'}")
                print(f"Date: {date_div.text.strip()}")
                print(f"Location: {location.text.strip() if location else 'N/A'}")
                print(f"Detail URL: {detail_url}")
        except ValueError:
            pass  # skip if date parsing fails
