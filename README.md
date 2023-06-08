<!-- BADGES -->
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/PrathamBhatTech/Mask-Detection?include_prereleases&style=for-the-badge)
<br>
![GitHub contributors](https://img.shields.io/github/contributors/PrathamBhatTech/Mask-Detection?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues-raw/PrathamBhatTech/Mask-Detection?style=for-the-badge)
<br>
<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![LinkedIn][linkedin-shield]][linkedin-url]

# Mask-Detection

## Introduction
During the Covid-19 Pandemic, immense efforts and resources have been put into maintaining protocols like Social Distancing and regulating mass public on usage of Masks. Any lapses on these fronts have resulted in countless fatalities and losses. This project is dedicated to contribute and provide help in regulating these protocols to ensure safety of mass population. Immense military and policing resources have
been spent on regulating a compulsory mask wearing policy, and yet lapses have been found in public spaces. This project addresses this issue and aims to automate the process of checking for the presence of mask and provide support to authorities by issuing a warning.

<br>
<br>

## Detection:
<img src="/DemoImages/Demo_NoMask.png" style="height: 380px; width: 400px;" alt="No Mask IMG"/> |
<img src="/DemoImages/Demo_Mask.png" style="height: 380px; width: 400px;" alt="With Mask IMG"/>
<br><br>

## Creating Dataset:
This component works independently to create the dataset needed to train the model. This component makes use of the Tkinter library to make a Graphical User Interface to take in some parameters to customize the program. The program takes in time delay, no of images and choice to determine the time delay between every frame to be captured, the number of images to be taken into dataset and the option to make a dataset for mask and no mask. This is done to make it easy for the user to create datasets of their own by taking samples of different angles, lighting and conditions to help improve the model quality.
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
