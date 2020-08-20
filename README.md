# Image Analyser
Image Analyser is a script which lets you analyse features in your image(s) using different algorithms

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Execution](#execution)
4. [Troubleshooting](#troubleshooting)

## Introduction
I am working on identifying faces in disguise. 
As part of my learning journey, I am starting with first analysing images and detecting features on the image. _Baby steps_

In this project, I have provided implementations of various feature detection algorithms using opencv and python.

This is just meant for learning purposes, hope it can help you as well!

## Setup
The script runs on python 3. To run the script, you first have to install the dependencies.

First, install [pip](https://pip.pypa.io/en/stable/installing/) and [git](https://git-scm.com/downloads) before we proceed to the next steps.
If you don't have [git](https://git-scm.com/downloads), then you can also download this project from this repository as a zip from the `Code` button on the top.
Then, follow the steps below

    cd \path\to\this\repository
    python3 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt


## Execution
We're all set! Just run the following command and it will take care of the rest:

    python analyser.py

![Demo](https://i.imgur.com/HVTeTvw.gif)
## Troubleshooting
1. If you are getting errors running opencv, we suggest you install it from [here](https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/)
2. If you're running Windows, the image prompts might launch but not pop up and go to minimised state. 
The console library prevents image windows to pop out. Please maximise the images manually.
