<!-- BADGES -->
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/PrathamBhatTech/Mask-Detection?include_prereleases&style=for-the-badge)
<br>
![GitHub contributors](https://img.shields.io/github/contributors/PrathamBhatTech/Mask-Detection?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/PrathamBhatTech/Mask-Detection?style=for-the-badge)
<br>
<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![LinkedIn][linkedin-shield]][linkedin-url]

# Mask-Detection
Detects if the person in front of the camera is wearing a mask or not.<br>
Outlines the face of the person's face making it easy for the person monitoring to discover.<br>
The create dataset ability can be used to create or increase the size of the dataset which will result in a better accuracy when trained later.<br>
<br>

## Detection:
<img src="/DemoImages/Demo_NoMask.png" style="height: 300px; width: 300px;" alt="No Mask IMG"/> |
<img src="/DemoImages/Demo_Mask.png" style="height: 300px; width: 300px;" alt="With Mask IMG"/>
<br><br>

## Creating Dataset:
<!-- <img src="/DemoImages/Demo_CreateDataset.png" alt="DatasetCreator IMG"/> -->
<img src="/DemoImages/Demo_CreatedDataset.png" alt="DatasetCreated IMG"/>
<br>

## Built with:
  * Python
  * OpenCV
  * Mediapipe
  * Tensorflow
  * Tkinter
  * asyncio

<br>

## Prerequisites:
  * For Linux: `sudo apt-get install python3.9 pip`
  * For Windows: Follow these links to install python and pip
    * https://www.python.org/downloads/
    * https://phoenixnap.com/kb/install-pip-windows


## Installation:
  * Clone the repository: `git clone https://github.com/PrathamBhatTech/Mask-Detection.git`
    
  * Change current directory to the repo: `cd Mask-Detection`
  
  * Install requirements: `pip install -r requirements.txt`

<br>

## Usage:
 * To run the mask detection: `python3.9 Run.py`
 * To run the dataset creator: `python3.9 CreateDataset.py`
 * To train a model using the dataset you created:
    * Upload the dataset after zipping(.zip) to your drive. NOTE: Name of folder `data`.
    * open the `train.ipynb` file using google collab. Login to the account you uploaded the dataset.
    * Modify the path of the dataset in the code.
    * Start training.
    * Download the trained model.
<br><br>
Project Link: https://github.com/PrathamBhatTech/Mask-Detection

<!-- Markdown Links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/pratham-bhat-176b34202/
