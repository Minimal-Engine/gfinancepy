from pytickersymbols import PyTickerSymbols
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets

# Authenticate using the credentials
gc = pygsheets.authorize(service_file='credentials.json')

# Open Spreadsheet 'Aktienwatchlist'
sh = gc.open_by_key('1kfki9dBE78At0V0bFFh1Lcp3gk6my-31GVEYmJ8TQ30')

# Get the names of the indices of pytickersymbols into a list
stock_data = PyTickerSymbols()
index_list = stock_data.get_all_indices()

# write a loop to get the name out and copy it into the 'Aktien_Watchlisten'
for index_name in index_list:
    stocklist = stock_data.get_stocks_by_index(index_name)
    print('Now printing Stocks from: ' + index_name)
    for stock in stocklist:
        print(stock['name'])
        print(stock['symbols'])

# print(list(stocklist))


# for i in german_stocks:
#    print(i['name'])
#    print(i['symbols'][0]['google'])
#    print(i['symbols'][0]['yahoo'])
# print(sh.worksheets())
# sh.add_worksheet(index_name, rows=250, cols=20, 
#               src_worksheet=sh.worksheets()[-1])
# print(index_list)
