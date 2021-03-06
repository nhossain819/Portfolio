"""
DESCRIPTION:
The following are samples of my Pandas skillset. These samples are organized by increasing complexity.

These are the result of self-teaching as well as practice exercises found through W3resource.
"""

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
PROJECT 1 DATA CLEANING
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
(Currently being edited and updated)
-The datasets used in this project are made up of 10 csv files, named 'states0.csv' to 'states9.csv' respectively.
-Each csv file contains 5 rows of data with the columns:
    'State', 'TotalPop', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'Income', 'GenderPop'
-All files used require cleaning for missing values and inappropriate data types.

"""
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
Import all necessary modules
    -pandas for analysis
    -numpy for analysis
    -matplotlib.pyplot to generate scatterplots
    -glob for combining multiple datasets
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import glob





"""
CONSILIDATE ALL CSV FILES TO CREATE ONE DATAFRAME
'files' uses glob to create a list of all csv files that have the names similar to states
The wildcard * is used because all the csv files are states0.csv, states1.csv, ...
"""
files = glob.glob("states*.csv")

#   df_list is a list of all csv files from files (created using the for loop thorugh files)
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

#   us_census is the final dataframe which is df_list concatenated.
us_census = pd.concat(df_list)






"""
DATA CLEANING
"""
#   Replace all '$' from the values in the 'Income' column with nothing. Regex refers to regular expression(\$)
us_census.Income = us_census['Income'].replace('[\$]', '', regex=True)


#   splitlist is made up of the strings of the GenderPop column 'split' at the character '_' .
#   sample of an observation in GenderPop: 2964003M_3081445F
#   The observations of GenderPop are the datatype string.
splitlist = us_census.GenderPop.str.split('_')


#   MalePop is created as a new column in us_census. The observations of MalePop are the first
#       observations of splitlist.
us_census['MalePop']= splitlist.str.get(0)

#   The following line replaces the 'M's in the observations of the column MalePop with nothing.
us_census.MalePop = us_census['MalePop'].replace('[M]', '', regex=True)


#   The column FemalePop is created and edited in the same format as the column MalePop.
us_census['FemalePop'] = splitlist.str.get(1)
us_census.FemalePop = us_census['FemalePop'].replace('[F]', '', regex=True)


#   The columns FemalePop, TotalPop, and MalePop are converted into numeric datatypes
us_census.FemalePop = pd.to_numeric(us_census.FemalePop)
us_census.TotalPop = pd.to_numeric(us_census.TotalPop)
us_census.MalePop = pd.to_numeric(us_census.MalePop)


#   The FemalePop column contains missing observations. The values in this column can be
#       calculated from the values of the TotalPop and MalePop columns.
us_census = us_census.fillna(value={"FemalePop":us_census.TotalPop - us_census.MalePop})


#   The columns 'Hispanic' and 'White' go through similar cleaning as the FemalePop and MalePop columns.
us_census.Hispanic = us_census['Hispanic'].replace('[%]', '', regex=True)
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)
us_census.White = us_census['White'].replace('[%]', '', regex=True)
us_census.White = pd.to_numeric(us_census.White)




#   The following line removes duplicate observations from the us_census dataframe.
us_census = us_census.drop_duplicates()


#   Creates and displays a scatterplot of FemalePop vs. Income
pyplot.scatter(us_census.FemalePop, us_census.Income)
pyplot.show()



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
PROJECT 2 DATA ANALYSIS
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines analyze a sample dataset.

SAMPLE DATASET CREDIT: The dataset used here is a sample dataset found on W3resource and
originating from https://github.com/mwaskom/seaborn-data . The sample dataset involves the
characteristics of diamonds.

SAMPLE ROWS FROM DATASET
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
#   Import pandas
import pandas as pd

#   Create a dataframe
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

#   Print the first 5 rows.
print(df.head(5))

#   Print information about the data frame.
print(df.info())



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Selects rows by index
-Selects specific rows and columns
-Finds the numbers of rows and columns
"""
#   Select rows 50 to 75.
rows_50_to_75 = df.iloc[50:76]

#   Select specific rows and columns.
carat_cut = df[['carat' , 'cut']]
carat_cut_rows_5_10_15 = carat_cut.iloc[[5, 10, 15]]

#   Find the number of columns and rows.
number_of_columns = len(df.axes[1])
number_of_rows = len(df.axes[0])



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Creates a subsets of data based on row value.
"""
#   Create a subset of data with the best cut of diamond.
best_cut = df[df.cut == 'Ideal']

#   Produce a subset of data with null clarity values.
missing_clarity = df[df['clarity'].isnull()]

#   A subset of data with carat values between 0.25 and 0.30.
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
#   Create a dataframe based on color and size.
color_size = df[['color' , 'size']]

#   Calculate the average size by color.
mean_size_by_color = color_size.groupby(['color']).mean()

#   Create a dataframe based on color and price.
color_price = df[['color' , 'price']]

#   Calculate the total revenue of each color.
sum_price_by_color = color_price.groupby(['color']).sum()

#   Calculate the total revenue of each color.
sum_price_by_color.sort_values(by=['price'], inplace=True, ascending=False)

#   Remove rows of index 7 and 10 from the dataframe.
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


#   Average carat of each cut style using a groupby.
carat_cut = df[['carat' , 'cut']]
mean_carat_by_cut_type = carat_cut.groupby(['cut']).mean()



#   Average carat of each cut style using a for loop.
list_of_all_cuts = list(pd.unique(df.cut))

for cut_type in list_of_all_cuts:
    cut_subset = df[df.cut == cut_type]
    cut_subset_meancarat = cut_subset.carat.mean()
    print('Mean Carat of ' + str(cut_type) + ' Cut ' + str(round(cut_subset_meancarat , 5)))



#   Average carat of each cut style using data subsets.
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

#   Create a calculated 'size' column.
df['size'] = round((df.x * df.y * df.z) , 2)

#   Create a calculated 'Expensive' column.
df['Expensive'] = df.price.apply(lambda x: 'Yes' if x > 2000 else 'No')

#   Create a dataframe based on the 'Expensive' column.
big_expensive = df[(df.size > 25) & (df.Expensive == 'Yes')]

#   Sort the dataframe by price.
df.sort_values(by=['price'], inplace=True, ascending=False)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
The following lines:
-Create a dataframe from the first 5 rows.
-Export the dataframe as a CSV.
-Import the exported CSV.
"""
#   Create a dataframe from the first 5 rows.
rows5 = df.iloc[:5]

#   Export the dataframe as a CSV.
rows5.to_csv('/Users/Nayeem/Desktop/WORKING/rows5.csv', sep=',', index=False)

#   Import the exported CSV.
df2 = pd.read_csv('/Users/Nayeem/Desktop/WORKING/rows5.csv')
