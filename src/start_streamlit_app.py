import streamlit as st
from omegaconf import DictConfig
from src.utils import download_images_helper

def start_streamlit_app(config: DictConfig):
    st.title("Image Downloader App")

    # Create the configuration form
    with st.form("Configuration"):
        save_path = st.text_input("Save Path", value="/path/to/save/images")
        keyword = st.text_input("Keyword", value="example")
        num_images = st.number_input("Number of Images", value=10, min_value=1, step=1)

        submitted = st.form_submit_button("Download Images")

    # Process the form submission
    if submitted:
        config = DictConfig({
            "save_path": save_path,
            "keyword": keyword,
            "num_images": num_images
        })

        # Download images
        st.text("Downloading images...")
        download_images_helper(config)
        st.text("Image download completed.")
