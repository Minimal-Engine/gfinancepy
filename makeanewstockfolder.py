from pytickersymbols import PyTickerSymbols
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets

# Authenticate using the credentials
gc = pygsheets.authorize(service_file='credentials.json')
# Open Spreadsheet 'Aktienwatchlist'
sh = gc.open_by_key('1kfki9dBE78At0V0bFFh1Lcp3gk6my-31GVEYmJ8TQ30') 

stock_data = PyTickerSymbols()
german_stocks = stock_data.get_stocks_by_index('DAX')
uk_stocks = stock_data.get_stocks_by_index('FTSE 100')

# for i in german_stocks:
#    print(i['name'])
#    print(i['symbols'][0]['google'])
#    print(i['symbols'][0]['yahoo'])
print(sh.worksheets)
#sh.add_worksheet('DAX', rows=250, cols=20, src_worksheet='VORLAGE')
print(sh)
