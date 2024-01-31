import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
from utils.helpers import *
from utils.constants import URLS
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time

async def parser(response, findable, **kwargs):
    """
    Parses HTML response and finds the correct element.

    Input:
        - response: The HTTP response to parse.
        - findable: Tag or search criteria for the find method.
        - **kwargs: Additional arguments.

    Ouput:
        - The HTML element or None.
    """

    text = await response.text()
    soup = BeautifulSoup(text, "html.parser")
    return soup.find(findable, **kwargs)


async def perform_deeper_search(parsed_data, key):
    """
    Checks if a specified key exists in JSON data parsed from an HTTP response.

    This function is used when the server always returns a 200 HTTP status code, 
    making it necessary to tell apart valid data for an existing user 
    and data for a non-existent user.

    Input:
        - parsed_data: The parsed response data.
        - key: The key to search for in the JSON data.

    Output:
        - True: If the key is found in the JSON data.
        - False: The key is not found in the JSON data.
    """

    try:
        jd = json.loads(parsed_data.string)
        return find_key(jd, key)
    except json.JSONDecodeError:
        return False


async def perform_chrome_scan(object_data, username, function_to_call):
    """
    Uses ChromeDriver via Selenium to simulate a web browser for verifying the existence of a user account.

    Input:
        - object_data: Dictionary containing all the parameters to perform the scan.
        - username: The given username to perfom the scan on.

    Output:
        - True: If the account searched on exists.
        - False: If the account does not exist.
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(object_data["link"].format(username))
        func = globals().get(function_to_call) 

        # Call the right function and functionality for the Chrome Scan
        return await func(driver)
    except WebDriverException as e:
        return False
    finally:
        driver.quit()


async def perform_http_scan(object_data, username):
    """
    Checks the output of an HTTP request to determine the existence of a user account.

    Input:
        - object_data: Dictionary containing all the parameters to perform the scan.
        - username: The given username to perfom the scan on.

    Output:
        - True: If the account searched on exists.
        - False: If the account does not exist.
    """

    headers = object_data.get('headers', {})

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get(object_data['link'].format(username)) as response:
                if response.status != 200: return False

                if object_data.get('findable') and object_data.get('soup_data'):
                    parsed_data = await parser(response, object_data['findable'], **object_data['soup_data'])

                    if object_data.get('key'):
                        return await perform_deeper_search(parsed_data, object_data['key'])
                    
                    if not parsed_data: return False
                return True
        except aiohttp.ClientError:
            return False


async def main():
    username = input('\033[1;97mEnter the username you want to search:\033[0m ')
    print("\u001b[34;1mStart Scan \u001b[34;0m\n")
    results = {}    

    # Perform the scan for each URL in the URLS dictionary.
    for url in URLS:
        type = URLS[url].get('type', None)
        if type and type == 1:
            results[url] = await perform_chrome_scan(URLS[url], username, url)
        else:
            results[url] = await perform_http_scan(URLS[url], username)

    # Prints the results from the scan, with the correct values and colors.
    for key in results:
        value = await make_return_values(results[key])
        print(f"\033[1;97m    - {key}:\033[0m {value}")
    print("\n")



if __name__ == "__main__":
    print('''\033[1;95m
   _____            _       _                                           
  / ____|          (_)     | |                                          
 | (___   ___   ___ _  __ _| |___   ___  ___ __ _ _ __  _ __   ___ _ __ 
  \___ \ / _ \ / __| |/ _` | / __| / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
  ____) | (_) | (__| | (_| | \__ \ \__ \ (_| (_| | | | | | | |  __/ |   
 |_____/ \___/ \___|_|\__,_|_|___/ |___/\___\__,_|_| |_|_| |_|\___|_|   
                                                                        
    \033[0m''')

     # Run the main function asynchronously
    start = time.time()
    asyncio.run(main())
    
    print("\u001b[34;1mEnd Scan \u001b[0m")
    print(f"\x1B[3mScan time: {time.time() - start}\x1B[0m")