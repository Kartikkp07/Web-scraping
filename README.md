# hello-world
extensive web scraping of an ecommerce website involving the use of python to extract information of a number of books by category, from the following site:
https://books.toscrape.com/

There are some 50 categories of books on this site.Extracting the following information for the first 30 (or less if so is the case) for any 10 categories has been done:
1. Book Name
2. Rating
3. Price
4. Availability
5. Image


The extracted information (apart from the images) for each of the books is made available in the following form:

1. A .csv file for each category of books with columns for name, rating, price
and availability

2. A combined .csv file to store all books in the single file( one
extra column now for each book - that’s the category).

For the images,  each book’s image is downloaded and stored in a folder having the name of the
category of the book. All these folders have been stored inside one combined folder named as
“book_images”.

**ALL OF THIS TASK HAS BEEN AUTOMATED USING PYTHON SCRIPT**
