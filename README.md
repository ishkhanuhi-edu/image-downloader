# image-downloader

## [Table of Contents](#table-of-contents)

- [Image Downloader](#image-downloader)
    - [Table of Contents](#table-of-contents)
    - [Installation](#installation)
    - [Scripts documentation](#scripts-documentation)

## Installation

- Run `conda env update -f environment.yaml` from the command line in the root directory to install all required dependencies.
- Run `export PYTHONPATH="${PYTHONPATH}:/the_path_of_cloned_repository/` to setup the working directory correctly.

## Scripts documentation

- ### **Streamlit Application Script**

  Starts web application whose purpose is to provide UI for code uploading and executing process.  
  _**Running command**_:

  ```bash
  python run.py --config-name=start_streamlit_app 
  ```
  After running, you'll see the path, when you can redirect and use the application.

![alt text](assets/Screen%20Recording%202023-05-28%20at%2023.03.19.gif)


- ### **Desktop Application Script**

  Starts desktop application whose purpose is to provide UI for code uploading and executing process.  
  _**Running command**_:

  ```bash
  python run.py --config-name=start_desktop_app 
  ```
  After running, you'll see a popup and the application is ready to be used.

![alt text](assets/Screen%20Recording%202023-05-28%20at%2022.55.30.gif)


- ### **Script documentation**
  Just starts the script which downloads the images. The required arguments can be passed through command line or be  
  updated in configs/download_images.yaml file.

    _**Running command**_:

   ```bash
    python run.py --config-name=download_images 
    ```