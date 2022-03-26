from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from time import sleep


def take_screenshot(machine, chromedrivers_path, timetable_name, credentials) -> None: 
    """This function logins into amizone and takes a screenshot of the timetable with the help of Selenium.

    Args:
        machine (string): name of the operating system.
        chromedriver_path (string): path to chrome drivers.
        timetable_name (string): name of the timetable screenshot to be saved.
        credentials (dict): it contains the username and password of the user. This is parsed from credentials.json using json.load().
    """    
    
    # selenium will use headless window
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    if machine == "linux":
        driver = webdriver.Chrome(
            executable_path=chromedrivers_path["linux"], options=options)
    elif machine == "win32":
        driver = webdriver.Chrome(
            executable_path=chromedrivers_path["win32"], options=options)
    elif machine == "darwin":
        driver = webdriver.Chrome(
            executable_path=chromedrivers_path["darwin"], options=options)
        
        

    driver.get("https://s.amizone.net/")
    driver.implicitly_wait(10)

    # filling the credentials
    username = driver.find_element(by=By.NAME, value="_UserName")
    username.click()
    username.send_keys(credentials["username"])
    password = driver.find_element(by=By.NAME, value="_Password")
    password.click()
    password.send_keys(credentials["password"])

    #selecting submit buttom
    driver.find_element(by=By.CLASS_NAME, value="login100-form-btn").click()

    try:
        # closing notice popup
        driver.find_element(by=By.XPATH, value="""//*[@id="MyPopup19"]""").click()
    except:
        pass
    # selecting  the time table tab

    # sleep(1)
    # selecting page content(time table) div
    timetable = driver.find_element(by=By.XPATH, value="""//*[@id="Div_Partial"]/div[1]/div/div[2]/div/div/div/div[7]/div[1]/div/div/div""")
    timetable.screenshot(timetable_name)
