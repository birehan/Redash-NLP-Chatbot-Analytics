import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random as random 

class DataSummarizer:
    """
    a class with list of data sumarizing methods.
    """
    def __init__(self) -> None:
        pass

    def percent_missing(self, df):
        """
        this function calculates the total percentage of missin values in a dataset.
        """
        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        print("The dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "(", totalMissing,")missing values.")

    def columns_missing_most_values(self, df, descript, percentage):
        '''
        Function returning names of columns missing atleast n% values from a dataframe
        '''
        colum_wise = df.isnull().sum() * 100 /df.shape[0]
        missing_col_names = colum_wise[colum_wise > percentage].index.tolist()
        good_col_names = [cn for cn in df.columns if cn not in missing_col_names]
        if percentage:
            print(" {} columns are missing moethan {}% of their values\nThey are:\n".format(len(missing_col_names), percentage))
        else:
            print(" {} columns are missing atleast 1 value, they are:\n".format(len(missing_col_names)))
        with pd.option_context('expand_frame_repr', False):
            droped = descript.loc[descript['Fields'].isin(missing_col_names)]
            droped['% Missing'] = [colum_wise.get(col_nm) for col_nm in missing_col_names]
            print (droped.sort_values(by=['% Missing']))
            good = descript.loc[descript['Fields'].isin(good_col_names)]
            if percentage:
                print("\n The columns with atmost {}% values missing are:\n".format(percentage))
                good['% Missing'] = [colum_wise.get(col_nm) for col_nm in good_col_names]
                print(good.sort_values(by=['% Missing']))
            else:
                print("\n The columns with no values missing are:\n",good)

        return missing_col_names, good_col_names

    def show_N_per_col(self, df, main, cols, N, target="top"):
        """
        sorts a column and shows top 10 values.
        """
        asc = False
        if(target == "bottom"):
            asc = True
        for col in cols:
            print("\nTop 10 customers based on "+col+"\n")
            print(df.sort_values(by=col, ascending=asc).loc[:,[main, col]].head(N))
    
    def bivariateAnalysis(self, df, cols, colors): 
        """
        it plots a scatter chart and runs correlation test
        """
        for i in range(len(cols)):
            plt.style.use('fivethirtyeight')
            plt.figure(figsize=(8, 4)) 
            sns.scatterplot(data = df, x=cols[i][0], y=cols[i][1], s=20, color=colors[i])
            print(self.corrMatrix(df, cols[i]))
    
    def plot_count(self, df, no_of_cat, col, hue_col=None):
        #plt.style.use('fivethirtyeight')
        plt.figure(figsize=(8, 4))
        if hue_col:
            sns.countplot(x=col, hue=hue_col, data=df, order=df[col].value_counts(ascending=True).iloc[(-1*no_of_cat):].index)
            plt.title("Multi-level count plot of Top {} {} by {} ".format(no_of_cat,hue_col,col), size=20, fontweight='bold')
        else:
            sns.countplot(x=col, data=df, order=df[col].value_counts(ascending=True).iloc[(-1*no_of_cat):].index)
            plt.title("Count plot of Top {} {} ".format(no_of_cat,col), size=20, fontweight='bold')
        plt.yscale("log")
        plt.tick_params(axis='x', rotation=90)
        plt.show()

    def plot_boxes(self, df, cols=None):
        """
        Box-plot plotting function.
        """
        if not cols:
            cols = df.columns
        for col in cols:
            self.plot_box(df,col,"Outliers of {} coulmn".format(col))

    def plot_distributions(self, df, cols=None):
        """
        Distribution plotting function.
        """
        if not cols:
            cols = df.columns
        for col in cols:
            self.plot_hist(df,col,(random.random(),random.random(),random.random()))
    
    def plot_corr_heatmap(self, df:pd.DataFrame, cols):
        """
        Correlation heatmap b/n selected columns plotting function.
        """
        mask = np.zeros_like(df[cols].corr(), dtype=bool)
        mask[np.triu_indices_from(mask)] = True

        f, ax = plt.subplots(figsize=(12, 9))
        plt.title("Correlation heatmap b/n columns",fontsize=25)

        sns.heatmap(df[cols].corr(),linewidths=0.25,vmax=0.7,square=True,cmap="BuGn", #"BuGn_r" to reverse
                    linecolor='w',annot=True,annot_kws={"size":8},mask=mask,cbar_kws={"shrink": .9})
        plt.show()
    
    def plot_hist(self, df:pd.DataFrame, column:str, color:str)->None:
        plt.figure(figsize=(12, 7))
        sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

    def plot_bar(self, df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
        plt.figure(figsize=(12, 7))
        sns.barplot(data = df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks( fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show()

    def plot_box(self, df:pd.DataFrame, x_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.xscale("log")
        plt.show()

    def plot_box_multi(self, df:pd.DataFrame, x_col:str, y_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks( fontsize=14)
        plt.xscale("log")
        plt.show()

    def plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data = df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks( fontsize=14)
        plt.show()

        
    def summarise_columns(self, df, unique=True):
        """
        shows columns and their missing values along with data types.
        """
        df2 = df.isna().sum().to_frame().reset_index()
        df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df2['missing_percent_(%)'] = round(df2['missing_count']*100/df.shape[0])
        data_type_lis = df.dtypes.to_frame().reset_index()
        df2['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df2.shape[0]):
                unique_val.append(len(pd.unique(df[df2.iloc[i,0]])))
            df2['unique_values'] = pd.Series(unique_val)
        return df2.sort_values(by=['missing_percent_(%)'])
    '''
    def plot_box(self, df:pd.DataFrame, col:str)->None:
        """
        Boxplot plotting function.
        """
        plt.boxplot(df[col])
        plt.title(f'Plot of {col}', size=20, fontweight='bold')
        ax = plt.gca()
        #ax.set_ylim(top = df[col].quantile(0.9999))
        #ax.set_ylim(bottom = 0)
        # show plot
        plt.show()

    def plot_box2(self, df:pd.DataFrame, columns, color:str)->None:
        """
        Boxplot plotting function.
        """
        fig = plt.figure(figsize =(10, 7))
        
        for col in columns:
            # Creating plot
            plt.boxplot(df[col])
            plt.title(f'Plot of {col}', size=20, fontweight='bold')
            ax = plt.gca()
            ax.set_ylim(top = df[col].quantile(0.9999))
            ax.set_ylim(bottom = 0)
            # show plot
            plt.show()


    def summarise_columns(self, df, unique=True):
        """
        shows columns and their missing values along with data types.
        """
        df2 = df.isna().sum().to_frame().reset_index()
        df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df2['missing_percent_(%)'] = round(df2['missing_count']*100/df.shape[0])
        data_type_lis = df.dtypes.to_frame().reset_index()
        df2['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df2.shape[0]):
                unique_val.append(len(pd.unique(df[df2.iloc[i,0]])))
            df2['unique_values'] = pd.Series(unique_val)
        return df2.sort_values(by=['missing_percent_(%)'])


    def top_n_grouped(self, df, col_name, num):
        """
        a function that groups a column and return the top n groups based on member count
        """
        return (df.groupby(col_name).size().reset_index(name='counts')).sort_values(by=['counts']).tail(num)


    def manByHandset(self, df, dfname, globalDict):
        """
        a function that returns top three handsets from top three manufacturers
        """
        


    def find_agg(self, df, group_columns, agg_columns, agg_metrics, new_columns):
        """
        a function that returns a new dataframe with aggregate values of specified columns.
        """
        new_column_dict ={}
        agg_dict = {}
        for i in range(len(agg_columns)):
            new_column_dict[agg_columns[i]] = new_columns[i]
            agg_dict[agg_columns[i]] = agg_metrics[i]

        new_df = df.groupby(group_columns).agg(agg_dict).reset_index().rename(columns=new_column_dict)
        return new_df


    def combineColumns(self, df, col1, col2, new_name, rem=False):
        """
        combines two numerical variables and create new variable.
        """
        df[new_name] = df[col1]+df[col2]
        if(rem):
            df.drop([col1, col2], axis = 1, inplace = True)


    def generateFreqTable(self, df, cols, range):
        """
        generate a freqeuncy table
        """
        for col in cols:
            print(df[col].value_counts().iloc[:range,])


    def summary_one(self, df, cols):
        """
        calculate range, max, count, and min.
        """
        df2 = df[cols]
        data_types_dict = {'max': float, 'min':float}
  
        df_sum = df2.max().to_frame().reset_index().rename(columns={"index":"variables",0:"max"})
        df_sum["min"] = df2.min().to_frame().reset_index().iloc[:,1]
        df_sum= df_sum.astype(data_types_dict)
        df_sum['range'] = df_sum['max'] - df_sum['min']
        df_sum["count"] = df2.count().to_frame().reset_index().iloc[:,1]
        return df_sum


    def summary_two(self, df, cols):
        """
        calculate central tendency measures.
        """
        df2 = df[cols]
        df_sum = df2.mean().to_frame().reset_index().rename(columns={"index":"variables",0:"mean"})
        df_sum["median"] = df2.median().to_frame().reset_index().iloc[:,1]
        df_sum["mode"] = df2.mode().iloc[:,1]
        return df_sum


    def summary_three(self, df, cols):
        """
        calculate dispersion measures
        """
        df2 = df[cols]
        df_sum = df2.std().to_frame().reset_index().rename(columns={"index":"variables",0:"std"})
        df_sum["var"] = df2.var().to_frame().reset_index().iloc[:,1]
        return df_sum


    def bar_graph(self, df, cols, x_ax):
        """
        graphical univariate analysis function. bar chart.
        """
        plot_df = df[cols]
        plt.figure(figsize=(25, 12))
        sns.countplot(x= x_ax, data=plot_df)



    def topDecile(self, df, group,deci, cols, metric, name, range):
        """
        function that aggregates based on top n deciles.
        """
        df['Decile'] = pd.qcut(df['session_dur'], 10, labels=False)
        aggr_n = self.find_agg(df, group, cols, metric, name)
        aggr_n = aggr_n.loc[aggr_n['Decile'] < range[1]+1]
        aggr_n = aggr_n.loc[aggr_n['Decile'] > range[0]-1]
        return aggr_n


    def corrMatrix(self, df, cols):
        """
        a function that generates correlation matrix as a table.
        """
        relation = df[cols].corr()
        return relation
        '''