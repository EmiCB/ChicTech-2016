# Exercises for learning Programming Concepts and Python

Welcome to a short tutorial on the some fundamental programming concepts in the form of short exercises.
We'll go through how to create and use functions, how to use a computer to solve math equations, loops, and advanced functions!

Hopefully, what you learn here can be applied to your own classes and projects. We may even hold some sort of competition where you can test your skills :)

# How to get started on EWS Machines
This part is primarily for the ChicTech retreat where students will be using labs in the basement of Siebel to run through the tutorials.

### Steps

0. Download the zip file for this repository if you haven't done so already (ChicTech students should get this from a given link by the instructors. Unzip the file by double clicking and pressing the extract button in the top right and save it in the same folder that you downloaded it to.
1. Open up terminal on the EWS machine. You can find it in the Applications menu in the top left when you log in under the Utilities sublist.
2. Navigate to the folder were you downloaded the zip file. Most likely, it has ended up in your Downloads folder and you can access that by typing the following: `cd Downloads/python-start` and then pressing enter. Once you are inside the folder, you should see that the bottom line in your terminal should have changed to say `python-start`
3. Inside this folder, type `./setup.sh` and it will start up the notebooks. In case this doesn't work, type `chmod +x setup.sh` and press enter
4. This will open up a web browser where we will be doing all of our Python coding.
5. You will find everything we are working on in the `/notebooks` folder. I would start with the first tutorial!
6. When you are all done, make sure to save your work and press CTRL+C in the terminal and confirm that you want to close the notebook by typing `y` and pressing enter.
7. If you want to open the notebook again, just type `./setup.sh` or you can type `jupyter notebook` when you are inside the folder

## How to get Python installed

### Mac/Linux

Python should come preinstalled on your computer, but you may want to install a different version from the one your operating system uses. In this case, ask an officer or ping me (berwin) to help you out.

### Windows

Follow [this guide](http://docs.python-guide.org/en/latest/starting/install/win/) to install python on your computer, including the section that you run a command in `powershell`. You can look for Powershell on your computer by pressing the Windows key and typing in `powershell`. You should get a blue window terminal where you will paste the command from the guide. Once it is installed, you may have to restart Powershell and by typing `python` + Enter, you should be able to see
if it was successfully installed.

## Saving Your Work and Continuing Later

In your open Jupyter notebook, click File > Download As > Python (.py). This generates Python scripts with all of your code and the tests. If you have Python installed on your computer (follow the instructions in the section above), you can then install Anaconda, which will provide all of the scientific computing / data science libraries we've used for this tutorial right out of the box. Follow [this guide](https://www.continuum.io/downloads).