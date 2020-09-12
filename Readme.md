# lidkaart-stickers
A script to help generating a file to print on sticker paper from a list of registration codes.

# Instructions
## Get the codes
Generate the codes from the site and paste the output in `codes.txt`. Be sure every code is somewhere in the file between brackets. You can find an example in `codes.txt`. Instructions on how to generate codes for our site can be found on the Neon. 
## Edit the codes
If you want special codes for some people, change them now in your `codes.txt` (e.g. if you want to give the person with number 7 the code SEVEN, you should change your seventh code to SEVEN)
## Install dependencies and run code
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
## Make the labels
You now have a csv containing the numbers and codes. 
Install gLabels on Ubuntu:
```
sudo apt-get install glabels
```
Open it, create a new file and choose your label format (or create your own one if it doesn't exist yet for your brand).
Choose "Edit merge properties" at the second row of the top bar in gLabels and select the generated `codes.csv` file (as a CSV file with keys on line 1). Now, you can create a text box. When editting the text field (on the right), you can "Insert merge field", being the `lidnr` and `code`. Design your label and hit print. (Note: First print one sheet on normal paper, to be sure everything is aligned right for the stickers)
## The old way
This method has a few problems, so it's recommended to use gLabels.
In `main.py`, set `GENERATE_ODT` to `TRUE` and run the script. 
Upload the generated `Stickers.odt` to Google Drive and open it with Google Docs (opening with other programs can give a different formatting).
You'll probably have to add here and there a few extra tabs (because some codes are shorter than others). After this, print one sheet on normal paper to see everything is aligned well for printing on etiquetes. Then print on pre-cut sticker paper (A4 size, 3x8 stickers per page).
## The very old way
Don't use this script and just copy paste all codes one by one in a word document. 


Feel free to open a pull requests if you've got any bug fixes/new features. 
