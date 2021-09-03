<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Facial Emotion Detection Filter" />

  &#xa0;

  <!-- <a href="https://facialemotiondetectionfilter.netlify.app">Demo</a> -->
</div>

<h1 align="center">Facial Emotion Detection Filter</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/cynthiachiu/facial-emotion-detection-filter?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/cynthiachiu/facial-emotion-detection-filter?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/cynthiachiu/facial-emotion-detection-filter?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/cynthiachiu/facial-emotion-detection-filter?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/facial-emotion-detection-filter?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/facial-emotion-detection-filter?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/facial-emotion-detection-filter?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Facial Emotion Detection Filter 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/cynthiachiu" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Takes in live webcam video feed, detects your face using the HAAR Cascade Classifier, detects your emotion from your expression using FER model, and overlays an animal mask on top of your face with the emotion description. Inspired by https://medium.com/analytics-vidhya/creating-snapchat-like-filters-from-scratch-using-computer-vision-techniques-6374cde6a7db and https://www.digitalocean.com/community/tutorials/how-to-apply-computer-vision-to-build-an-emotion-based-dog-filter-in-python-3.

## Demo ##

![Alt Text](demo.gif)

## :sparkles: Features ##

:heavy_check_mark: Python3;\
:heavy_check_mark: OpenCV;\
:heavy_check_mark: Frontal Face Haar Cascade Classifier;\
:heavy_check_mark: Facial Expression Recognition (fer);

## :rocket: Technologies ##

The following tools were used in this project:

- [Python3](https://www.python.org/downloads/)
- [FER](https://pypi.org/project/fer/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Cascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python3](https://www.python.org/downloads/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/cynthiachiu/facial-emotion-detection-filter

# Create Python3 virtual env
$ python3 -m venv facial-emotion-detection-filter

# Access
$ cd facial-emotion-detection-filter

# Activate the virtual env
$ source bin/activate

# Install dependencies
$ pip install fer

# Run the script
$ python emotion_detection_facial_mask.py

# It will access your webcam and a window will appear with the animal mask and description overlayed in the frame in real-time.
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/cynthiachiu" target="_blank">cynthiachiu</a>

&#xa0;

<a href="#top">Back to top</a>
