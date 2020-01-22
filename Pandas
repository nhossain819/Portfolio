"""
DESCRIPTION:
The following are samples of my Pandas skillset. These samples are organized by increasing complexity.

These are the result of self-teaching as well as practice exercises found through W3resource.

SAMPLE DATASET CREDIT: The dataset used here is a sample dataset found on W3resource and 
originating from https://github.com/mwaskom/seaborn-data . The sample dataset involves the 
characteristics of diamonds.

#SAMPLE ROWS FROM DATASET
"carat","cut","color","clarity","depth","table","price","x","y","z"
0.23,"Ideal","E","SI2",61.5,55,326,3.95,3.98,2.43
0.21,"Premium","E","SI1",59.8,61,326,3.89,3.84,2.31
0.23,"Good","E","VS1",56.9,65,327,4.05,4.07,2.31
...
0.7,"Very Good","D","SI1",62.8,60,2757,5.66,5.68,3.56
0.86,"Premium","H","SI2",61,58,2757,6.15,6.12,3.74
0.75,"Ideal","D","SI2",62.2,55,2757,5.83,5.87,3.64
"""


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines of code:
-Import pandas.
-Create a data frame based on a csv.
-Print the first 5 rows of the dataframe.
-Print basic information about the dataframe.
"""
#Import pandas
import pandas as pd

#Create a dataframe
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

#Print the first 5 rows.
print(df.head(5))

#Print information about the data frame.
print(df.info())



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Selects rows by index
-Selects specific rows and columns
-Finds the numbers of rows and columns
"""
#Select rows 50 to 75.
rows_50_to_75 = df.iloc[50:76]

#Select specific rows and columns.
carat_cut = df[['carat' , 'cut']]
carat_cut_rows_5_10_15 = carat_cut.iloc[[5, 10, 15]]

#Find the number of columns and rows.
number_of_columns = len(df.axes[1])
number_of_rows = len(df.axes[0])



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Creates a subsets of data based on row value.
"""
#Create a subset of data with the best cut of diamond.
best_cut = df[df.cut == 'Ideal']

#Produce a subset of data with null clarity values.
missing_clarity = df[df['clarity'].isnull()]

#A subset of data with carat values between 0.25 and 0.30.
carat_between25and30 = df[(df.carat > 0.25) & (df.carat <= 0.3)]



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Provide descriptive statistics by a specific column.
"""
average_carat = df.carat.mean()

max_carat = df.carat.max()

min_carat = df.carat.min()

median_carat = df.carat.median()

sum_carat = df.carat.sum()


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Create a dataframe based on color and size.
-Calculate the average size by color.
-Create a dataframe based on color and price.
-Calculate the total revenue of each color.
-Sort the dataframe by price.
-Remove rows of index 7 and 10 from the dataframe.
"""
#Create a dataframe based on color and size.
color_size = df[['color' , 'size']]

#Calculate the average size by color.
mean_size_by_color = color_size.groupby(['color']).mean()

#Create a dataframe based on color and price.
color_price = df[['color' , 'price']]

#Calculate the total revenue of each color.
sum_price_by_color = color_price.groupby(['color']).sum()

#Calculate the total revenue of each color.
sum_price_by_color.sort_values(by=['price'], inplace=True, ascending=False)

#Remove rows of index 7 and 10 from the dataframe.
drop_test_rows_5_15 = rows_5_15.drop(df.index[[7,10]])



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Show how to find the average carat of each cut style.
    -This concept is coded in three different ways using three different methods: 
        -groupby
        -for loop
        -creating data subsets.
"""


#Average carat of each cut style using a groupby.
carat_cut = df[['carat' , 'cut']]
mean_carat_by_cut_type = carat_cut.groupby(['cut']).mean()



#Average carat of each cut style using a for loop.
list_of_all_cuts = list(pd.unique(df.cut))

for cut_type in list_of_all_cuts:
    cut_subset = df[df.cut == cut_type]
    cut_subset_meancarat = cut_subset.carat.mean()
    print('Mean Carat of ' + str(cut_type) + ' Cut ' + str(round(cut_subset_meancarat , 5)))



#Average carat of each cut style using data subsets.
all_cuts = pd.unique(df.cut)

idealcut = df[df.cut == 'Ideal']
premiumcut = df[df.cut == 'Premium']
goodcut = df[df.cut == 'Good']
verygoodcut = df[df.cut == 'Very Good']
faircut = df[df.cut == 'Fair']

idealcut_meancarat = idealcut.carat.mean()
premiumcut_meancarat = premiumcut.carat.mean()
goodcut_meancarat = goodcut.carat.mean()
verygoodcut_meancarat = verygoodcut.carat.mean()
faircut_meancarat = faircut.carat.mean()


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Create a 'size' column calculated from the x, y, and z columns.
-Create an 'Expensive' column based on the price column value.
-Create a data frame based on size and whether or not the item is expensive.
-Sort the values of the dataframe by price.
"""

#Create a calculated 'size' column.
df['size'] = round((df.x * df.y * df.z) , 2)

#Create a calculated 'Expensive' column.
df['Expensive'] = df.price.apply(lambda x: 'Yes' if x > 2000 else 'No')

#Create a dataframe based on the 'Expensive' column.
big_expensive = df[(df.size > 25) & (df.Expensive == 'Yes')]

#Sort the dataframe by price.
df.sort_values(by=['price'], inplace=True, ascending=False)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Create a dataframe from the first 5 rows.
-Export the dataframe as a CSV.
-Import the exported CSV.
"""
#Create a dataframe from the first 5 rows.
rows5 = df.iloc[:5]

#Export the dataframe as a CSV.
rows5.to_csv('/Users/Nayeem/Desktop/WORKING/rows5.csv', sep=',', index=False)

#Import the exported CSV.
df2 = pd.read_csv('/Users/Nayeem/Desktop/WORKING/rows5.csv')



