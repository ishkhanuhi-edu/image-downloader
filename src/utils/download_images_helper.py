from src.image_downloader import ImageDownloader


def download_images_helper(config):
    if config.search_engine == 'safari':
        downloader = ImageDownloader(config.save_path, config.keyword, config.num_images, config.search_engine,
                                     config.srch_safari,
                                     config.second_image)
        downloader.download_images()
        downloader.quit_driver()
    else:
        downloader = ImageDownloader(config.save_path, config.keyword, config.num_images, config.search_engine,
                                     config.srch_chrome,
                                     config.second_image)
        downloader.download_images()
        downloader.quit_driver()
