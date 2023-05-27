import json
import logging
import subprocess
import warnings
import hydra
import dotenv
import os
from omegaconf import DictConfig, OmegaConf

dotenv.load_dotenv()

log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="configs", config_name="start_streamlit_app")
def main(config: DictConfig):
    # Imports should be nested inside @hydra.main to optimize tab completion
    # Read more here: https://github.com/facebookresearch/hydra/issues/934

    # if config.get("print_config"):
    #     from src.utils import print_config
    #
    #     print_config(config, fields=tuple(config.keys()), resolve=True)

    if config.get("ignore_warnings"):
        log.info("Disabling python warnings! <config.ignore_warnings=True>")
        warnings.filterwarnings("ignore")

    if config.name == "download_images":
        from src import download_images
        return download_images(config)

    if config.name == "start_streamlit_app":
        app_script_path = os.path.join("src", "start_streamlit_app.py")
        config_dict = OmegaConf.to_container(config)

        # os.chdir(hydra.utils.get_original_cwd())
        subprocess.run(["streamlit", "run", app_script_path, '--', json.dumps(config_dict)])


if __name__ == '__main__':
    main()
