#Need to install python-pip then install boto3 ,selenium,pillow for PIL using pip.
import boto3
import requests
import logging
from botocore.exceptions import ClientError
from selenium import webdriver
from PIL import Image
link = input ("Enter the Website link:") 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
#chrome = webdriver.Chrome(chrome_options=chrome_options,service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
chrome = webdriver.Remote(
    command_executor='http://localhost:4445/wd/hub',
    options=chrome_options
)
chrome.get(link)
chrome.save_screenshot("image_chrome.png")
chrome.quit()
#driver = webdriver.Firefox()
opts = webdriver.FirefoxOptions()
opts.add_argument('headless')
driver = webdriver.Remote(command_executor = 'http://localhost:4444/wd/hub', 
                                    desired_capabilities = opts.to_capabilities())  
driver.get(link) 
driver.save_screenshot("image_firefox.png")
driver.quit()
client = boto3.client('s3', region_name='us-east-1')
client.upload_file('image_chrome.png', 'test-bucket-cb-2', 'image_chrome.png')
client.upload_file('image_firefox.png', 'test-bucket-cb-2', 'image_firefox.png')
# Get the service client.

# Generate the URL to get 'key-name' from 'bucket-name'
url1 = client.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': 'test-bucket-cb-2',
        'Key': 'image_chrome.png'
    },
    ExpiresIn=1800)
print("\n Generating pre-signed url for chrome. \n")	
print(url1)	
response = requests.get(url1)

url2 = client.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': 'test-bucket-cb-2',
        'Key': 'image_firefox.png'
		},
    ExpiresIn=1800)
print("\n Generating pre-signed url for firefox \n")	
print(url2) 	