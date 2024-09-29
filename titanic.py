# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# show the title
st.title('Titanic App by Linxi Xia')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Box plot for each class
for i in range(1, 4):
    ax[i-1].boxplot(df[df['Pclass'] == i]['Fare'])  
    ax[i-1].set_xlabel(f'PClass = {i}')
    ax[i-1].set_xticklabels(['Fare'])
    ax[i-1].set_ylabel('Fare')

plt.tight_layout()
st.pyplot(fig)

