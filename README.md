# image-downloader

## [Table of Contents](#table-of-contents)

- [Image Downloader](#image-downloader)
    - [Table of Contents](#table-of-contents)
    - [Installation](#installation)
    - [Scripts documentation](#scripts-documentation)

## Installation

- Run `conda env update -f environment.yaml` from the command line in the root directory to install all required dependencies.

## Scripts documentation

- ### **Streamlit Application Script**

  Starts web application whose purpose is to provide UI for code uploading and executing process.  
  _**Running command**_:

  ```bash
  python run.py --config-name=start_streamlit_app 
  ```
  After running, you'll see the path, when you can redirect and use the application.

- ### **Script documentation**
  Just starts the script which downloads the images. The required arguments can be passed through command line or be  
  updated in configs/download_images.yaml file.

    _**Running command**_:

   ```bash
    python run.py --config-name=download_images 
    ```