# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.sidebar.checkbox("Show raw data"):	
    st.subheader("Census Data Set")
    st.dataframe(census_df)
    st.write('Numbers of rows and columns of the dataset',census_df.shape)
st.title('Census APP')
st.sidebar.title('Census APP')
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
plot_list=st.sidebar.multiselect('Select the Chart/Plots',['Count Plot','Pie Chart','Box Plot'])
if 'Pie Chart' in plot_list:
    st.subheader("Pie Chart")
    pie_data = census_df['income'].value_counts()
    plt.figure(figsize = (5, 5))
    plt.pie(pie_data, labels = pie_data.index, autopct = '%1.2f%%')
    st.pyplot()
# Display box plot using matplotlib module and 'st.pyplot()'
if 'Box Plot' in plot_list:
    st.subheader('Box Plot')
    column=st.sidebar.selectbox('Select the column for Box Plot',['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country'])
    sns.boxplot(census_df[column])
    st.pyplot()
# Display count plot using seaborn module and 'st.pyplot()' 
if 'Count Plot' in plot_list:
    st.subheader('COUNT PLOT')
    sns.countplot(x='income',data=census_df)
    st.pyplot()
