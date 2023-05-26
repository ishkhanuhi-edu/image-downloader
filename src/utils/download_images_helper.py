from src.image_downloader import ImageDownloader


def download_images_helper(config):
    downloader = ImageDownloader(config.save_path, config.keyword, config.num_images)
    downloader.download_images()
    downloader.quit_driver()
