import numpy as np
from data_summary import DataSummarizer;


class DataCleaner:
    """
    class that handles data cleaning.
    """
    def __init__(self) -> None:
        self.summar = DataSummarizer()

    def fill_missing(self, df, column_types):
        '''
        Function to fill missing values appropriately
        The Columns can be grouped in to five different types:
            **Categorical**:  categorical properties(string or digit) fill with some constant
            **Time Series**:  system time stamps of events >> fill with FORWARD/BACKWARD
            **Numerica percentage distributions**: Performanc edistribution over speed ranges in %
            **Numerical **: the rest of numerical columns >> fill with MEAN
                ***avarages
                ***time-gaps
                ***data-volumes
        '''
        #Fill categorical strings with 'undefined' 
        df1 = df.fillna(value={ k:v for (k,v) in zip(column_types['cat_str'], ['undefined']*len(column_types['cat_str']))})

        #Fill categorical digits with 0 
        df2 = df1.fillna(value={ k:v for (k,v) in zip(column_types['cat_dig'], [0]*len(column_types['cat_dig']))})

        #Fill Timeseries forward/backward
        df2.loc[:,column_types['time_series']] = df2.loc[:,column_types['time_series']].ffill().bfill()

        #Fill numerical percentage distributions with 0.0 as they represent missing as columns need to addup to 100% for each row
        df3 = df2.fillna(value={ k:v for (k,v) in zip(column_types['num_dist'], [0]*len(column_types['num_dist']))})

        #Fill numerical averages, time-gaps , and data volumes with mean
        all_num = column_types['num']['time']+column_types['num']['data']+column_types['num']['avg']
        df4 = df3.fillna(value={ k:v for (k,v) in zip(all_num, [df3[col].mean() for col in all_num])})

        return df4
    
    def remove_cols(self, df, cols, keep=False):
        """
        a functions that removes specified columns from dataframe
        """
        if(keep):
            r_df = df.loc[:,cols]
        else:
            r_df = df.drop(cols, axis=1)

        return r_df

    def reduce_dim_missing(self, df,limit):
        """
        removes columns with number of missing values greater than the provided limit
        """
        temp = self.summar.summ_columns(df)
        rem_lis = []
        for i in range(temp.shape[0]):
            if(temp.iloc[i,2] > limit):
                rem_lis.append(temp.iloc[i,0])
        r_df = df.drop(rem_lis, axis=1) 
        
        return r_df

    def combine_datatime_with_offset(self, df, datetime_col, offset_col):
        df['Start(Secs)'] = df[datetime_col[0]].total_seconds() + offset_col[0]
        df['End(Secs)'] = df[datetime_col[1]].total_seconds() + offset_col[1]
        return df

    def fix_outliers(self, df, columns=None):
        if not columns:
            columns = df.columns
        for column in columns:
            df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
        return df

    def convert_bytes_to_megabytes(self, df, bytes_colmns):
        megabyte = 1048576
        for column in bytes_colmns:
            df[column] = df[column] / megabyte
        return df

    def ms_to_s(self, df, ms_cols):
        """
        converting ms to s.
        """
        for col in ms_cols:
            df[col] = df[col]/1000
        return df