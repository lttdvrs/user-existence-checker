# Username Existence Checker

The **Username Availability Checker** is a tool designed for determining the availability of a specific username across a range of online platforms. The tool offers a fast and accurate assessment of the username registration status.

This tool is intended for entertainment and informational purposes only.

## Installation and usage

Install the required dependencies:

> pip install requirements.txt

Running the script:

> python scanner.py

When prompted enter the username to perform the scan on.

## Customization

Users can adapt the script to their needs by altering the `URLS` dictionary in the `utils/constants.py` file. This dictionary should contain the requisite parameters for each website, such as URL format, HTML elements to search for, and key indicators in JSON responses.

### Parameters for URLS

When you add your own website to the URLS dictionary, you can customize it by using parameters, or more accurately, by defining keys and their corresponding values.

| Key | Value |
|-----|-------|
| link | This is the link to the website you want to test. To insert a username into the URL, use '{}' as a placeholder. |
| findable | The tag to search for in the BeautifulSoup `find` query. |
| soup_data | A dictionary for adding attributes to the BeautifulSoup query. |
| key | Used to locate data in the BeautifulSoup response that is difficult to find. |
| headers | A dictionary of headers to include in the aiohttp request. |
| type | Add 1 if you prefer a Chrome scan over an HTTP scan. In this case, you should also create a function with the same name as the dictionary key, including the necessary functionality."


## Future Additions

Plans for future development include transforming this script into an API and expanding its capabilities with more options and websites. This might require **API keys** for the script to run on **your** device.

  
## Disclaimer

 As these methods used are subject to change, regular updates to the script may be necessary to maintain its accuracy and effectiveness across all supported platforms. I will try my best to keep up with these, please feel free to create new **issues** on this.