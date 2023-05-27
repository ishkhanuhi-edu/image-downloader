import os
import time
import base64
import pandas as pd

from PIL import Image
from io import BytesIO
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ImageDownloader:
    """
    A class to download images from Google Images.
    Parameters:
        path (str): The path to store the downloaded images and CSV file.
        xpath (str): The XPath for the search box on the Google Images page.
        srch_engine (str): The engine to use for downloading (Safari or Chrome)
        second_image (str): The XPath for the second image on the preview page.
        keyword (str): The keyword to search for.
        num_images (int): The number of images to download.
    """
    def __init__(self, path, keyword, num_images, xpath_chrome, xpath_safari, second_image):
        self.__path = path
        self.__keyword = keyword
        self.__num_images = num_images
        self.__second_image = second_image

        try:
            self.__driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.__srch = xpath_chrome
        except:
            self.__driver = webdriver.Safari()
            self.__srch = xpath_safari

    def __create_directory(self):
        """
        Create the directory to store the downloaded images and CSV file.
        """
        os.makedirs(self.__path, exist_ok=True)

    def download_images(self):
        """
        Download images based on the specified parameters.
        """
        self.__create_directory()
        self.__driver.get("https://www.google.com")  # Go to google.com
        search_box = self.__driver.find_element(By.XPATH, self.__srch)
        search_box.send_keys(self.__keyword)
        search_box.send_keys(Keys.RETURN)  # In the search bar type the keyword
        time.sleep(2)
        # If the page is in any other language change it to english
        try:
            images_link = self.__driver.find_element(By.LINK_TEXT, "Images")  # Go to the Images part of google
        except:
            language_tool = self.__driver.find_element(By.XPATH, '//*[@id="Rzn5id"]/div/a[2]')
            language_tool.click()
            images_link = self.__driver.find_element(By.LINK_TEXT, "Images")  # Go to the Images part of google
        images_link.click()
        time.sleep(2)
        image_elements = self.__driver.find_elements(By.CSS_SELECTOR, '.rg_i')  # Get all items that are images
        image_info = []
        for i, element in enumerate(image_elements):
            if i == self.__num_images:  # check the number of images if we reached the limit of predefined number
                break
            element.click()
            time.sleep(2)
            image_forlink = self.__driver.find_element(By.XPATH, self.__second_image)  # Click on the image
            url = image_forlink.get_attribute('src')  # get the url of specific image
            image_url = element.get_attribute('src')
            title = element.get_attribute('alt')  # get the title of an image
            if image_url is not None and image_url.startswith('data:image'):
                encoded_data = image_url.split(',')[1]
                image = Image.open(BytesIO(base64.b64decode(
                    encoded_data)))  # transform the link that is available to the format from which we can save the images
                file_path = f'{self.__path}/image_{i}.png'
                image.save(file_path)
                print(f"Image {i + 1} downloaded successfully.")
            image_info.append((title, url))
        df = pd.DataFrame(image_info, columns=['Title', 'URL'])
        df.to_csv(f'{self.__path}/image_info.csv', mode='w', index=False)  # Saving dataframe to csv

    def quit_driver(self):
        """
        Quit the Selenium driver.
        """
        self.__driver.quit()
