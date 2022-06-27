import pandas

# TASK - create a CSV file called squirrel_count.csv how many grey cinnamon and black ones are there?

data = pandas.read_csv('Squirrel_Data.csv')

grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')

color_data = pandas.read_csv('squirrel_count.csv')
print(color_data)
