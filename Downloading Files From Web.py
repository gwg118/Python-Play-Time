from urllib import request
# Download csv file

test_csv = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

#function to download csv
def download_stock_data(test_csv):

    #connection to the internet
    response = request.urlopen(test_csv)
    csv = response.read()
    csv_str = str(csv)

    # convert to readable data
    lines = csv_str.split("\\n")
    
    #tell computer where to save data
    desk_url = r'goog.csv'
    fx = open(desk_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(test_csv)
