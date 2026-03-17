import pandas as pd 

def explain_data(dataframe):
  ''' 
  Returns a dataframe with columns such as shape, data types,
  missing values and descriptive stats for all columns of input dataframe. 
  
  '''
  
  print(f"The data has {dataframe.shape[0]} rows and {dataframe.shape[1]} columns")
  
  print('Below are the column wise data-types,missing values, unique level and descriptive stats of the data')
  
  dtypes = dataframe.dtypes
  missing_values = dataframe.isnull().sum()
  unique_values = dataframe.nunique()
  describe = dataframe.describe(include='all').transpose()
  details = pd.concat([dtypes,missing_values,unique_values],axis =1,\
                      keys=['dtypes','missing_values','unique_values'])
  details = pd.concat([details,describe],axis=1)
  return details
