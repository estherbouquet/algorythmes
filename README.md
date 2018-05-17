 # Craigslist poem generator
created during a workshop with An Mertens at ESAD Saint-Étienne in April 2018

This script in python3 selects random sentences from ads posted on Craigslist to create a poem in a .txt file.
This is a work-in-progress project.

## using windows 10
### installation:
The script currently works with python 3.6.5 and on windows 10.

  1) Download python from [here](https://www.python.org/downloads/). 
  2) Double click on the .exe file and don't forget to check the box "Add Python 3.6 to PATH" before clicking on 'install'. If the box does not appear, install python and then execute the install file again and click on modify to check the box.
  3) Test the installation, by running `python` in your terminal. It should write the version of python that you are using. 
  4) Install all the dependencies needed from your terminal (on Windows, I used Windows PowerShell):
   - [ntlk](http://www.nltk.org/install.html): type `pip install ntlk` or `pip3 install nltk` (if you are using several versions of python). To test the installation, run `python` and then type `import nltk`.
   - [nltk data](http://www.nltk.org/data.html): after typing `import nltk` then type `nltk.download()`. This should open a new window, showing the NLTK Downloader. 
      * In 'copora', double click on 'stopwords' to download it. (it will be used to delete all the stopwords in the titles)
      * In 'models', download 'punkt'. (it will be used to tokenize the words contained in the titles of the ads)
   - You should not need to import manually the other packages like `operator`, `random` and `json` because they are here in python.
   5) Quit the python interpreter with the command `quit()`.

### how to use it:

The script works (for now) with a database of ads in a json file. 
* You can create a new database by running the `index.js` file which will create a new json file. Make sure you installed [puppeteer](https://github.com/GoogleChrome/puppeteer) before and that you are running one of the last version of nodejs.
* To add your new json file to the python script, simply modify the file name at the line 10 `with open('yourfilename.json', 'r') as fichier:` in `craigslist-poem-generator.py`.

1) Open your terminal.
2) Install all the dependencies as detailed before.
3) From your terminal, move into the folder which contains `craigslist-poem-generator.py` (using `cd`).
4) Run the file from your terminal typing the command: `python craigslist-poem-generator.py`.
5) Find your new generated poem at the end of the already existing poems in `testfile.txt`.

## using fedora 27

```
sudo dnf install -y python3 python3-pip git
git clone https://github.com/estherbouquet/craigslist-poem-generator
cd craigslist-poem-generator/
pip3 install --user nltk
echo "import nltk; nltk.download()"|python3
# Choose 'stopwords' and 'punkt' in the list and then close the window
cd craigslist-poem-generator/
python3 craigslist-poem-generator.py
```

Note 1: the package ```python3-pip``` may not install itself automatically/correctly. You may have to check the version of pip3 in ```usr/bin``` and then type in your terminal ```pip-3.x install --user nltk```. You will then be asked if you want to install the package ```python3-pip``` which provides ```pip-3.6``` and this should work, installing then nltk.

Note 2: the command ```echo "import nltk; nltk.download()"|python3``` may not work neither. You can manually install the packages by running ```python3``` and then writing in the prompt
```
import nltk;
nltk.download()
```
For the prompt ```Downloader>```, type ```d``` and press enter, and for ```Identifier>```, type ```stopwords``` and press enter. 
Do the exact same thing for ```punkt```.
When it is done, type ```q``` to quit NLTK Downloader and then ```quit()``` to quit python3.

And if you want to create your own json file:
```
sudo dnf install -y nodejs npm
npm install puppeteer
node index.js
```
Note: you may have to download first chromium and then install ```puppeteer```.

## to-do:
- [ ] Create a python script instead of the current one in nodejs.
- [ ] Add additional tags like `postid`, `price`, `location` and `posted on`.
- [ ] Add a prompt/feature to enter one or several keywords to search for instead of having a fixed url in the script.
- [ ] Selecting the two or three most recurring words in the titles instead of just one.
- [ ] Create a script that exports the poem into a pdf file with the right layout.
