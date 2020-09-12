# Handwriting-OCR (with a Flask - Integrated Dashboard)

I worked on this project during college, and ended up making a dashboard for presentation.
The image is used from the forked branch, and well as we all, the algorithm is only as 
accurate as the data you feed it. Feel free to plug any knn_data.npz and it can technically
give you a canvas for any use case where you are trying to match something that someone drew 
on a canvas.

## Steps to get started

1. Make a virtual environment. (You can use `python -m venv name_of_environment`)  
2. Activate it. (By running `source name_of_environment/bin/activate`)  
3. Run `pip install -r requirements.txt `  
4. Run `python dashboard.py`  

That's it!  A development server will start running and you can see all the requests listed here.

## Training Data

![Training Image]("/digits.png")

![Dashboard Screenshot]("/screenshot.png")




## Notes

Original knn_OCR.py is also present, feel free to tweak the configuration.  
The flask dashboard uses MDBootstrap (For UI) and Ajax to pull data from Flask.  



run `python kNN_OCR.py` to test its accuracy against digits.png. For testing with different images change img source path and adjust size and number of cells in image.

