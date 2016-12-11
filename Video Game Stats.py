
# coding: utf-8

# In[37]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import csv

def import_data():
    result = []

    file_dir = 'VideoGames.csv'
    with open(file_dir, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()
        for line in reader:
            # store line data into a python data structure
            result.append(line)

        return headers, result

headers, rows = import_data()

def graph_salesdata(x=1, y=2):
    # which column the data is stored in in the csv file
    x_axis_index = x
    y_axis_index = y

    plt.xlabel(headers[x_axis_index])
    plt.ylabel(headers[y_axis_index])
    game_dict = dict()
    
    for row in rows:
        game_dict[row[1]] = row[2]
    
    x_axis_values = []
    y_axis_values = []

    #for row in rows:
    #    x_axis_values.append(row[x_axis_index])
    #    y_axis_values.append(row[y_axis_index])
    
    # sorts games
    f = sorted(game_dict.items(), key=lambda x: x[1], reverse=True)
    sales = []
    for item in f:
        sales.append(item[1])
    plt.plot(range(len(f)), sales)
    plt.show()
    # finds top 10
    print 'Top 10 Games Sold in the US:'
    print ' '
    for i in range(10):
        print '  ' + f[i][0]
    
def get_average_images(self):
    return

graph_salesdata()


# In[ ]:



