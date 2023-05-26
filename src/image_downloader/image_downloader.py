import os
import time
import base64
import pandas as pd
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ImageDownloader:
    """
    A class to download images from Google Images.

    Parameters:
        path (str): The path to store the downloaded images and CSV file.
        srch (str): The XPath for the search box on the Google Images page.
        second_image (str): The XPath for the second image on the preview page.
        keyword (str): The keyword to search for.
        num_images (int): The number of images to download.
    """

    def __init__(self, path, keyword, num_images, srch):
        self.__path = path
        self.__keyword = keyword
        self.__num_images = num_images
        srch_chrome = '//*[@id="APjFqb"]'
        srch_safari = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]'
        second_image = '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]'  # This should not be changed
        self.__second_image = second_image

        # Tries to run on chrome if encounters an error try safari
        try:

            self.driver = webdriver.Chrome()
            self.srch = srch_chrome
        except:
            self.driver = webdriver.Safari()
            self.srch = srch_safari

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

        self.driver.get("http://www.google.com")  # Go to google.com

        search_box = self.driver.find_element(By.XPATH, self.srch)
        search_box.send_keys(self.__keyword)
        search_box.send_keys(Keys.RETURN)  # In the search bar type the keyword

        time.sleep(2)

        # If the page is in any other language change it to english
        try:
            images_link = self.driver.find_element(By.LINK_TEXT, "Images")  # Go to the Images part of google
        except:
            language_tool = self.driver.find_element(By.XPATH, '//*[@id="Rzn5id"]/div/a[2]')
            language_tool.click()
            images_link = self.driver.find_element(By.LINK_TEXT, "Images")  # Go to the Images part of google

        images_link.click()
        time.sleep(2)
        image_elements = self.driver.find_elements(By.CSS_SELECTOR, '.rg_i')  # Get all items that are images

        image_info = []
        for i, element in enumerate(image_elements):
            if i == self.__num_images:  # check the number of images if we reached the limit of predefined number
                break

            element.click()
            time.sleep(2)
            image_forlink = self.driver.find_element(By.XPATH, self.__second_image)  # Click on the image
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
        self.driver.quit()