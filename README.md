# Craigslist poem generator
created during a workshop with An Mertens at ESAD Saint-Étienne in April 2018

This script in python3 selects random sentences from ads posted on Craigslist to create a poem in a .txt file.
This is a work-in-progress project.

## installation:
The script currently works with python 3.6.5 and on windows 10.

  1) Download python from [here](https://www.python.org/downloads/). 
  2) Double click on the .exe file and don't forget to check the box "Add Python 3.6 to PATH" during the installation process.
  3) Test the installation, by running `python` in your terminal. It should write the version of python that you are using. 
  4) Quit python with the command `quit()`
  5) install all the packages needed from your terminal:
   - [ntlk](http://www.nltk.org/install.html): `pip install ntlk` or `pip3 install nltk` if you are using several versions of python. To test the installation, run `python` and then type `import nltk`.

## how to use it:

The script works (for now) with a database of ads in a json file. 
* You can create a new database by running the `index.js` file which will create a new json file. 
* To add your new json file to the python script, simply modify the file name at the line 10 `with open('yourfilename.json', 'r') as fichier:` in `craigslist-poem-generator.py`.
* Run `craigslist-poem-generator.py` from your terminal after installing all the dependencies.
* Find your new generated poem at the end of all the already existing poems in `testfile.txt`.

## to-do:
- [ ] Create a python script instead of the current one in nodejs.
- [ ] Add additional tags like `postid`, `price`, `location` and `posted on`.
- [ ] Add a prompt/feature to enter one or several keywords to search for instead of having a fixed url in the script.
- [ ] Selecting the two or three most recurring words in the titles instead of just one.
- [ ] Create a script that exports the poem into a pdf file with a nice display.
