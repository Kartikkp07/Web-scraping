from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urlparse

###########################################################################################################################################################################################
#
#code to store data from website :


url="https://books.toscrape.com/"

caturls=[]
catname=[]

#to store category wise names,prices,ratings and availaibility
booknames={}
bookratings={}
bookprices={}
bookavailability={}

#to store category_name:category_link
dict={"Travel":"","Classics":"","Philosophy":"","Religion":"","Music":"","Science Fiction":"","Sports and Games":"","New Adult":"","Science":"","Poetry":"",}

#home page requested to add category names and links to dict
r=requests.get("https://books.toscrape.com/")
s1=BeautifulSoup(r.content,"lxml")

clst=s1.find("ul",class_="nav nav-list")

for a in clst("li"):
    for b in a("ul"):
        for c in b("li"):
            for catlink in c("a"):
                    catname.append(catlink.text.strip())
                    caturls.append(catlink["href"])

for i in range(len(caturls)):
    caturls[i]="https://books.toscrape.com/"+caturls[i]

for i in range(len(caturls)):
    for j in dict:
        if j==catname[i]:
            dict[j]=caturls[i]

#to store image details wrt each book's name
bookimages={}

#loop to go through different caturls
for i in dict:
    #requests page whos link is mentioned in caturls
    p=requests.get(dict[i])
    s2=BeautifulSoup(p.content,"lxml")
    
    
    
    names=[]
    ratings=[]
    prices=[]
    availability=[]
    
    productlist=s2.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for books in productlist:
        for bookdata in books("article",class_="product_pod"):
            
                        
                        #for storing booknames
                        
            for heading in bookdata("h3"):
                for x in heading("a"):
                    names=names+[x["title"]]
            
            
                        #for storing rating

            for r in bookdata("p",class_="star-rating"):
                star_rating=r["class"][-1]
                ratings=ratings+[star_rating]
                
                       
                        #for storing prices
                        
            for p in bookdata("p",class_="price_color"):
                prices=prices+[p.text]
                    
                        
                        #for storing availability
                        
            for avlb in bookdata("p",class_="instock availability"):
                availability=availability+[avlb.text.strip()]
            
            
                        #for storing book images
                        
            for imgdata in bookdata("div",class_="image_container"):
                for imgdesc in imgdata("a"):
                    for imgsrc in imgdesc("img"):
                        imgname=imgsrc["alt"]
                        imglink="https://books.toscrape.com/"+imgsrc["src"][12::]
                        bookimages.update({imgname:imglink})
                        
    #updating required dictionaries
    
    bookprices.update({i:prices})
    bookavailability.update({i:availability})
    bookratings.update({i:ratings})
    booknames.update({i:names})

#print statements to test updates in dictionaries
#print(bookprices)
#print(bookavailability)
#print(bookratings)
#print(bookimages)
#print(booknames)

###########################################################################################################################################################################################
#
#code to put data in required files and folders:
#
#
#
import json
import csv
import regex
import os

#category wise .xlsx files:'
for i in dict:
    path="/Users/kkp/Desktop/category-wise csv files"
    name =i+'.csv'
    csvFileName = os.path.join(path,name)
    with open(csvFileName, 'w') as csv_file:
        csvWriter = csv.writer(csv_file, delimiter = ',')
        csvWriter.writerow(["Name","Rating","Price","Availability"])
        for j in range(len(booknames[i])):
            csvWriter.writerow([booknames[i][j],bookratings[i][j],bookprices[i][j],bookavailability[i][j]])

#file with additional category column
with open("Total_book_data.csv", 'w') as csv_file1:
    csvWriter = csv.writer(csv_file1, delimiter = ',')
    csvWriter.writerow(["Category","Name","Rating","Price","Availability"])
    for i in dict:
        for j in range(len(booknames[i])):
            csvWriter.writerow([i,booknames[i][j],bookratings[i][j],bookprices[i][j],bookavailability[i][j]])

#for storing downloaded images in folders named according to category
for i in dict:
    os.chdir("/Users/kkp/Desktop/book_images")
    try:
        os.mkdir(os.path.join(os.getcwd(),i))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),i))
    for j in booknames[i]:
        
        imgfolder_name=j+".jpg"
        with open(imgfolder_name,"wb") as imgfile:
        
            imglink=bookimages[j]
            img=requests.get(imglink)
            imgfile.write(img.content)
                
    
