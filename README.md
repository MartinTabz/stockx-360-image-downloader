# StocX 360 Photo Downloader

This simple python script that allowes you to download all 36 images of a sneaker from StockX.

Unfortunately StockX does not allow direct access to their website with code so you have to extract the first image URL manually.


## First Image Extraction

- Find your sneaker/item you want to download
- Right click on the page and click on Inspect
- Developer console will popup
- Select the "Select an element in the page to inspect it" tool on the top left of the developer console
- Point it to the image and press
- The HTML element should appear in the developer console - hover over the image url and open it
- Now copy the part of the URL "https://images.stockx.com/360/Air-Jordan-1-Retro-Low-OG-SP-Travis-Scott-Reverse-Mocha/Images/xxx...xxx/Lv2/img01.jpg", run the script and paste the url to it.
- Select the name of a folder where images will be saved to and press enter
- Now wait for the download and hooray...done.