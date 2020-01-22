# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:24:49 2020

@author: krish.naik
"""
#inside the business layer we are importing data layer library as well
from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    
    keyword=""
    fileLoc=""
    image_name=""
    header=""
    
    #header=
     
    def downloadImages( keyWord, header):
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyWord)
        rawHtml = imgScrapper.scrap_html_data(url, header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        
        return masterListOfImages    
   
    
    