# How to Scrap Real Estate Listing Data from Zillow

![Screenshot](https://github.com/yehaimi/real_estate_zillow/blob/903429acba7b3b74a58dd96ede89046d292a6a7b/assets/Screen%20Shot%202022-08-05%20at%2012.56.04%20AM.png)

Above is an interactive dashboard I put together in Tableau. 

I love real estate but I hate those listing websites. Visually it is not attractive or clear to me finding hidden gems. Yes we can use filters to narrow down our search, but honestly there are not too many insights.

I decide to do my own research with my data analytics skills. First thing to do, is getting the data. There are many handy packages in Python to scrape data from websites. I used BeautifulSoup, requests, json, and pandas to extract the data from Zillow (please scrape responsibly), by looping zip code and page number in the URL link (the reason I use zip code is because, the max page is 20 per search query and 40 listings per page. If I use city, then the returned results will be much more than 800). After trial and error, I locate the right elements I need in HTML, i.e. price, size, bedroom, bathroom, geo location, etc. There are much more useful data but for now let us start with these. After structuring the dataset, I output it to an excel and load that excel into Tableau.

That's how I did it. The real question is, what is the business insight and how to capitalize it? We can actually create daily job to automate the scrapping process and load those data into our database. Then we can send us alert in terms of price drop, market trend, and even evalution model.

Feel free to try out the python code to scrap those listing data from Zillow.com!
Here:(https://github.com/yehaimi/real_estate_zillow/blob/18c2262412a770fe4872cdb63d3992cf79c07a72/real_estate_zillow.py)


(Please Scrape Responsibly)
