1) Download Tesseract OCR from here and install it: https://github.com/UB-Mannheim/tesseract/wiki
NOTE: You must restart your computer after installing Tesseract OCR
and replace in main.py the path file with the path of tesseract on your computer
2) Make sure you have Python 3 installed
3) Install the required packages: `pip3 install -r requirements.txt`
4) Run the script: `python3 main.py`

If you get an error while you trying to install PIL (Pillow), you can try this
pip3 uninstall pillow
pip3 uninstall PIL
pip3 install image