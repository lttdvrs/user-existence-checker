from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import soundex

def find_key(data, target_key):
    """
    Recursive search for target_key in the JSON data.

    Input:
        - data: The parsed response data, dictionary or list.
        - target_key: The key to search for in the JSON data.

    Output:
        - True: If the key is found in the JSON data.
        - False: The key is not found in the JSON data.
    """
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                return True
            elif find_key(value, target_key):
                return True
    elif isinstance(data, list):
        for item in data:
            if find_key(item, target_key):
                return True
    return False


async def linkedin(driver): 
    """
    Helper function to use inside scanner function perform_chrome_scan()

    Checks the title of a LinkedIn profile page to determine the existence of a user account.

    Input:
        - driver: WebDriver instance to work with the webpage.

    Output:
        - True: If the account searched on exists.
        - False: If the account does not exist.
    """

    s = soundex.getInstance()
    authwall = driver.find_element(By.XPATH, '//meta[@content="/authwall"]')
    if authwall: return "\033[33mAuthwall Issue\033[0m"
    return s.soundex(driver.title.lower()) != s.soundex("profile not found | linkedin")


async def discord(driver, username):
    """
    Helper function to use inside scanner function perform_chrome_scan()

    Tries the register input field of Discord to fill in the username we are looking for, 
    and determine the existence of a user account.

    Input:
        - driver: WebDriver instance to work with the webpage.

    Output:
        - True: If the account searched on exists.
        - False: If the account does not exist.
    """
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
        )
        username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
        if username_field: 
            username_field.send_keys(username)
            try:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Username is unavailable')]"))
                )
                return True
            except TimeoutException:
                return False
    except TimeoutException:
        return False

        
async def make_return_values(key):
    if key == True:
        return "\033[32mRegistered\033[0m"
    if key == False:
        return "\033[91mUnregistered\033[0m"
    else:
        return f"{key}"