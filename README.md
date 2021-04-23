# Web-scraping-challenge

### Overview:
We built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.<br>

### Pre-requisites:
> - Beautifulsoup 
> - Requests/Splinter

### Step:1 (Scraping the websites)
> The following websites are scraped using Python script in Jupyter notebook:<br>
> - `NASA Mars News`: https://redplanetscience.com/ is scraped to get he latest news on Mars mission.<br>
> - `Mars Space Images - Featured Image`: https://spaceimages-mars.com is scraped to get the image of the Mars.<br>
> - `Mars Facts`: https://galaxyfacts-mars.com is scraped using pandas to get the facts about Earth & Mars. <br>
> - `Mars Hemispheres`: https://marshemispheres.com/ is scraped to get the image of Mars' hemisphere. <br>
> - All the details & facts scraped are appended to a dictionary for later use/storage in database.<br>

### Step:2 (MongoDB and Flask Application)
> - The Python script created in Jupyter notebook is converted into `scrape_mars.py` and it is called from flask route (/scrape).<br>
> - The output of scrape_mars.py is the dictionary with all the facts, images & tables. It is then returned to flask app and updated into MongoDB.<br>
> - The root route ('/') is created with query to mongoDB to retreive the Mars fact and passing it as dictionary to  `index.html`.<br>
> - All the parameters are placed in the appropriate placeholder to create a web application with bootstrap.<br>
> - The new data can be scraped on clicking the button `get new data`.<br.
> - The screenshot of the web application is taken.<br>

