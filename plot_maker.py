import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from os import listdir
from os.path import isfile, join


def main():
    st.set_page_config(layout='centered')

    st.title('Data Cleaning App')
    try:
        file = st.file_uploader('Data to clean', type=['csv', 'txt'], key='file_uploader')
    
        text = file.read().decode('utf-8')

        text = text.replace('--', '')
        text = text.replace('\n\n', '\n')
        text.strip('\n')
        text.strip()
        elements = text.split('\n\n ')
    

        for element in elements:
            index = element.split('\n')[0]
            if index == '':
                index = element.split('\n')[1]
            st.download_button(
                    label=f'Download {index}',
                    data=element,
                    file_name=f'{index}.csv',
                    mime='text/csv'
                )
    except:
        pass

    









    st.title('Data Plotting App')

    files = st.file_uploader('Data to plot', type='csv', key='uploader',
                             accept_multiple_files=True)

    x_label = st.text_input('X Label', '')
    y_label = st.text_input('Y Label', '')

    try:
        for i, file in enumerate(files):
            label = st.text_input(f'Label {i}', '')
            data = pd.read_csv(file, header=1)

            sns.set_style('darkgrid')
            plt.plot(data[data.columns[0]], data[data.columns[1]], label=label)

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
        plt.legend()
        st.pyplot(plt)
    except:
        pass









if __name__=='__main__':
    main()
