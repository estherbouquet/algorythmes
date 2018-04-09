# Craigslist poem generator
created during a workshop with An Mertens at ESAD Saint-Étienne in April 2018

This script in python3 selects random sentences from ads posted on Craigslist to create a poem in a .txt file.
This is a work-in-progress project.

## dependencies:
* python3 packages:
  - nltk
  - nltk.data
  - nltk.corpus
  
* nodejs librairy:
  - puppeteer

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

## notice
This script is developed solely for the purpose of research and education. Any commertial use of this script may violate cragslist's [terms of use](https://www.craigslist.org/about/terms.of.use.en)
