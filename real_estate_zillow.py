from bs4 import BeautifulSoup
import requests
import time
import random
import pandas as pd
import json
import math

start_time = time.time()

## Greater Vancouver zip codes
zipcode = ['V3S','V3W', 'V4N', 'V3R', 'V3B', 'V3V', 'V2X', 'V6Y', 'V5R', 'V4C', 'V3M', 'V3A', 'V3J', 'V3E', 'V3N', 'V7C', 'V5H', 'V3C', 'V3T', 'V7E', 'V3H', 'V4A', 'V2Y', 'V5N', 'V6X', 'V5P', 'V1M', 'V6P', 'V3K', 'V5C', 'V6B', 'V3Z', 'V5X', 'V5S', 'V3X', 'V3L', 'V6G', 'V6E', 'V7A', 'V7L', 'V6K', 'V5E', 'V5V', 'V4K', 'V5A', 'V5T', 'V5M', 'V5K', 'V5Z', 'V5B', 'V6J', 'V5J', 'V7M', 'V4B', 'V5G', 'V5L', 'V5W', 'V4W', 'V6R', 'V2W', 'V3Y', 'V6A', 'V6H', 'V6Z', 'V5Y', 'V7J', 'V6M', 'V2Z', 'V4R', 'V7V', 'V7N', 'V7R', 'V4M', 'V6N', 'V7H', 'V7P', 'V6T', 'V7K', 'V4P', 'V6S', 'V4E', 'V0M', 'V7G', 'V6V', 'V7S', 'V6L', 'V7T', 'V7W', 'V4L', 'V6C', 'V6W', 'V7B', 'V4G', 'V7X', 'V7Y']

## Greater Victoria zip codes
# zipcode = ['V9B','V9A','V8Z','V8V','V8N','V8X','V8R','V8L','V9C','V8T','V8P','V9Z','V8S','V8M','V8K','V8Y','V8W','V9E','V0S']

## Greater Toronto zip codes
# zipcode = ['M2N','M1B','M2J','M9V','M1V','M5V','M1W','M1K','M1E','M4C','M1P','M6H','M6M','M3N','M6N','M5A','M6K','M2R','M9W','M6P','M3C','M9C','M6E','M8V','M1S','M3H','M1J','M4J','M1C','M9A','M1L','M3A','M1T','M6S','M9R','M6J','M4L','M9B','M2M','M6G','M4K','M4Y','M1R','M1G','M6B','M4S','M5R','M5M','M3J','M9N','M4E','M4M','M6C','M2H','M1H','M3M','M2K','M1M','M9M','M1N','M8Y','M6A','M9P','M4X','M8W','M6L','M4P','M6R','M4H','M5P','M4G','M4B','M4V','M5T','M3L','M8Z','M5N','M5S','M4N','M1X','M4W','M5J','M4A','M3B','M5B','L5E','M9L','M2L','M4R','M8X','M4T','M5E','M5G','M2P','M3K','M5C','M5H','M5K','M5L','M5X','M7A','L5M','L6R','L6Y','L5N','L6P','L7A','L6X','L5B','L6S','L5V','L5A','L5L','L6V','L6T','L4T','L4Z','L5R','L7E','L6Z','L5C','L5J','L5W','L7C','L4Y','L6W','L4W','L5G','L4X','L5H','L5K','L5E','L7K','L4V','L5T','L5S','L6A','L4J','L4C','L4H','L3R','L3S','L4G','L4L','L4E','L6C','L3T','L3Y','L3X','L4A','L0G','L3P','L6E','L4B','L4S','L6B','L4P','L0E','L4K','L7B','L9N','L6G','L0J','L3L','L1V','L1T','L1N','L1C','L4A','L1J','L1G','L1S','L1R','L1K','L1H','L1Z','L1E','L1M','L0E','L1X','L1P','L1W','L9P','L0B','L9L','L0A','L1B','L0C','L1L','L0H','L1Y','L9T','L6M','L6H','L7M','L7L','L7G','L6L','L7P','L6J','L7T','L7R','L7J','L6K','L7N','L7S','L0P','L9E']

### set data structure
column_names = ['zpid', 'id', 'detailUrl',
       'price','unformattedPrice', 'address', 'addressStreet', 'addressCity',
       'addressState', 'addressZipcode',  'beds',
       'baths', 'area',  'brokerName',
       'latLong.latitude', 'latLong.longitude',
       'hdpData.homeInfo.homeType']
listdata = pd.DataFrame(columns = column_names).set_index('zpid')

### Construct headers
headers = {'accept':
'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'en-US,en;q=0.8',
           'upgrade-insecure-requests': '1',
           'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}

### create function to extract data based on url

def listing(link):
    #### get text from web through bs4
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    #### trim the text
    properties = soup.find_all('script')[-30].text.strip()[4:-3]
    data0 = json.loads(properties)
    data = data0['cat1']['searchResults']['listResults']

    #### inject data to dataframe
    df = pd.json_normalize(data)
    listdata0 = df[column_names].set_index('zpid')
    global listdata
    listdata = pd.concat([listdata0,listdata], ignore_index=True)

### create loop to extract data from multiple pages from website based on zip code
for i in zipcode:
    try:
        url0 = 'https://www.zillow.com/homes/' + i + '/'
        response = requests.get(url0, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        for listingnum in soup.find('div',{'class':'total-text'}):
            pagenumber = math.ceil(float(listingnum) / 40)
            print(i + ' ' + str(listingnum) + ' ' + str(pagenumber))
        if listingnum != 0:
            for j in range(1, pagenumber+1):
                try:
                    url = 'https://www.zillow.com/homes/' + i + '/' + str(j) + '_p'
                    listing(url)
                    time.sleep(1)
                except:
                    pass
    except:
        pass

num_rows = listdata['address'].nunique()
print('Raw number of rows:' + str(num_rows))

listdata.drop_duplicates(keep='first')
listdata.to_excel('listdata.xlsx')

num_rows = listdata['address'].nunique()
print('Final number of rows:' + str(num_rows))

# listdata.to_csv('listdata.csv')

print("--- %s seconds ---" % (time.time() - start_time))
