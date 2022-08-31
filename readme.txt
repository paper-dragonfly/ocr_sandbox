## Goal
Extract data from the workout_memory screen of a concept2 Ergometer

## TODOs
* crop image to standard screen view - screen box only (this is hard. for now do manualy)
* resize image so all images will be the same dimensions
* crop image into a number of smaller images that seperate out info (date, summary, interval data)
* ocr each image 
* return results and send to db 

### Repo Explanation
This project contains two files. 
1. process_image.ipynb
    - Takes a raw photograph and prepares it for OCR through the following steps:
        a. convert to grayscale 
        b. convert to binary b/w 
            - I used thresh_mode: ADAPTIVE_THRESH_GAUSSIAN_C. I'm not exactly sure how this works but the documentation indicated to use this if lighting/shadows vary across the image which they did in my example photo (erg_01.jpeg)
        c. noise removal
            - acheived through a combination of dilation and erosion. I've played around with different kernal sizes. Kernal size definitely affects the quality of the end result. However, there are clear tradeoffs (eg. less noise also means less clear numbers) so there doesn't seem to be a perfect choice
2. 

