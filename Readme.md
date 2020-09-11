# lidkaart-stickers
A script to automatically generates a `.odt` file to print on sticker paper from a list of registration codes.

# Instructions
## Get the codes
Generate the codes from the site and paste the output in `codes.txt`. Be sure every code is somewhere in the file between brackets. You can find an example in `codes.txt`. Instructions on how to generate codes for our site can be found on the Neon. 
## Install dependencies and run code
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
## Finishing touch
Upload the generated `Stickers.odt` to Google Drive and open it with Google Docs (opening with other programs can give a different formatting).
You'll probably have to add here and there a few extra tabs (because some codes are shorter than others). After this, print one sheet on normal paper to see everything is aligned well for printing on etiquetes. Then print on pre-cut sticker paper (A4 size, 3x8 stickers per page).

Feel free to open a pull request if you've got a fix for the extra tabs. 
