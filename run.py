import logging
import subprocess
import warnings
import hydra
import dotenv
import os

from omegaconf import DictConfig

dotenv.load_dotenv()

log = logging.getLogger(__name__)


@hydra.main(config_path="configs", config_name="download_images")
def main(config: DictConfig):
    # Imports should be nested inside @hydra.main to optimize tab completion
    # Read more here: https://github.com/facebookresearch/hydra/issues/934

    if config.get("print_config"):
        from src.utils import print_config

        print_config(config, fields=tuple(config.keys()), resolve=True)

    if config.get("ignore_warnings"):
        log.info("Disabling python warnings! <config.ignore_warnings=True>")
        warnings.filterwarnings("ignore")

    if config.name == "download_images":
        from src import download_images
        return download_images(config)

    if config.name == "start_streamlit_app":
        script_dir = os.path.dirname(os.path.abspath(__file__))
        app_script_path = os.path.join(script_dir, "src", "start_streamlit_app.py")
        subprocess.run(["streamlit", "run", app_script_path])


if __name__ == '__main__':
    main()
