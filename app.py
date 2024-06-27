from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path
import requests
import os
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc, options=chrome_options)

# Target URL
url = 'https://www.google.com/search?sca_esv=e2999e5afe90a665&sca_upv=1&sxsrf=ADLYWIKBsC4BnGqt7BcWfLlxfEy5Go3GbQ:1719499177518&q=adobe+stock+photos&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2jpXXSZVlK6C0YPjHbsLu8HQlFjXJu4aVhI_llTnXJ4lFAWdNYSKl18X_OYOML0jevhpDEumYRwaaY1jEa7vKdTgiN-XUHVrwULe1SBpdZ2b2Qdf9JCr6vszwGWtXx6BBaAiRVuZU26XGXcLhLP1MT26u-HDMw&sa=X&ved=2ahUKEwjLn6vNgfyGAxUtkIkEHU-RC5cQtKgLegQIFxAB&biw=1919&bih=958&dpr=1'


driver.get(url)
time.sleep(5)


image_folder = 'downloaded_images'
os.makedirs(image_folder, exist_ok=True)


image_elements = driver.find_elements(By.TAG_NAME, 'img')


for index, image_element in enumerate(image_elements):
    src = image_element.get_attribute('src')
    if src:
        try:
            response = requests.get(src)
            if response.status_code == 200:
                image_path = os.path.join(image_folder, f'image_{index+1}.jpg')
                with open(image_path, 'wb') as file:
                    file.write(response.content)
                print(f'Downloaded: {image_path}')
            else:
                print(f'Failed to download image from {src}')
        except Exception as e:
            print(f'Error downloading image from {src}: {e}')
    else:
        print('No src attribute found for an image element.')


driver.quit()
