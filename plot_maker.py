import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


def main():
    st.set_page_config(layout='centered')

    st.title('Data Plotting App')

    file = st.file_uploader('Upload a CSV file', type='csv', key='file_uploader')

    x_label = st.text_input('X Label', '')
    y_label = st.text_input('Y Label', '')

    try:
        data = pd.read_csv(file, header=1)

        sns.set_style('darkgrid')
        plt.plot(data[data.columns[0]], data[data.columns[1]])

        try:
            if x_label == '':
                plt.xlabel(data.columns[0])
            else:
                plt.xlabel(x_label)
            if y_label == '':
                plt.ylabel(data.columns[1])
            else:
                plt.ylabel(y_label)
        except:
            plt.xlabel(x_label)
            plt.ylabel(y_label)

        st.pyplot(plt)
    except:
        pass







if __name__=='__main__':
    main()