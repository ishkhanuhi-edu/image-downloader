from omegaconf import DictConfig

from src.utils import download_images_helper


def download_images(config: DictConfig):
    """
        Downloads images based on the provided configuration.

        Args:
            config (DictConfig): A dictionary-like object that contains the configuration parameters.
                It should have the following keys:
                - save_path (str): The path to the directory where the downloaded images will be saved.
                - keyword (str): The keyword or search query for the images to be downloaded.
                - num_images (int): The number of images to download.

        Returns:
            None

        Raises:
            None
        """
    download_images_helper(config)
