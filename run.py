from time_table import screenshot 
from time_table import telegram

import sys
import json
from datetime import date


# global macros
machine = sys.platform  # get the machine type
timetable_name = f"./screenshots/{date.today()}.png"
chromedrivers_path = {
    "linux" :  r"./assests/chromedrivers/linux/chromedriver",
    "win32" : r"./assests/chromedrivers/win32/chromedriver.exe",
    "darwin" : r"./assests/chromedrivers/darwin/chromedriver"
}   # the path of the chromedrivers

# credentials
with open(r"./assests/credentials/credentials.json", "r") as f:
    credentials = json.load(f)
    
if __name__ == "__main__":
    screenshot.take_screenshot(machine, chromedrivers_path, timetable_name, credentials)
    # telegram.send_image(timetable_name, credentials)
    