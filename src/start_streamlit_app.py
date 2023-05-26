import sys
import json
import streamlit as st

from omegaconf import DictConfig
from src.utils import download_images_helper


def start_streamlit_app():
    dict_config = json.loads(sys.argv[1])
    st.title("Image Downloader APP")
    # Create the configuration form
    with st.form("Configuration"):
        save_path = st.text_input("Save Path", value=dict_config["save_path"])
        keyword = st.text_input("Keyword", value=dict_config["keyword"])
        num_images = st.number_input("Number of Images", value=dict_config["num_images"], min_value=1, step=1)

        submitted = st.form_submit_button("Download Images")

    # Process the form submission
    if submitted:
        config = DictConfig({
            "save_path": save_path,
            "keyword": keyword,
            "num_images": num_images,
            "search_engine": dict_config['search_engine'],
            "srch_chrome": dict_config['srch_chrome'],
            'srch_safari': dict_config['srch_safari'],
            'second_image': dict_config['second_image']
        })

        # Download images
        st.text("Downloading images...")
        download_images_helper(config)
        st.text("Image download completed.")


start_streamlit_app()
