import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt




# building app

# app title
# st.title('Colorbrace EDA APP')
st.markdown("<h1 style='text-align: center; color: teal; font-size: 40px; margin-bottom: 20px;'>Colorbrace EDA APP</h1>", unsafe_allow_html=True)

# file uploader
uploaded_file = st.file_uploader('Upload your data', type=['csv','xlsx'])


# file uploaded details
if uploaded_file is not None:
    st.write("")
else:
    st.write("No file uploaded")


# show info
if uploaded_file is not None:
    
    # from file to dataframe
    if 'csv' in uploaded_file.type.lower():
        data = pd.read_csv(uploaded_file)

    else:
        data = pd.read_excel(uploaded_file, engine='xlrd')

    if data.empty:
        st.write("Data is Empty")

    else:
        st.write("Data Info")
        # show first Head
        if st.checkbox('Show Data Head (first 5 rows)'):
            st.text("First 5 rows of the dataset")
            st.write(data.head())
            st.write("")

        if st.checkbox("Show columns of the dataset"):
            st.text("Columns of the dataset")
            st.write(data.columns)

        
        if st.checkbox("Show Sample (random)"):
            st.text("Random sample of dataset")
            st.write(data.sample(n=12))
            st.write("")

            

        # show size of data
        if st.checkbox("Show shape of the dataset"):
            st.text("Rows , Columns")
            st.write(data.shape)
            st.write("")

        if st.checkbox("Show description of dataset"):
            st.text("Description of the dataset")
            st.write(data.describe())
            st.write("")

        if st.checkbox("Check for null value"):
            st.text("Null values in each column")
            st.write(data.isnull().sum())

        
        if st.checkbox("Count values"):
            valCount = st.selectbox("Choose column:", data.columns)
            if valCount is not None:
                st.write(data[valCount].value_counts())
                st.write("")

        if st.checkbox("Show unique values"):
            st.text("Unique values in each column")
            st.write(data.nunique())


        
        # OPERATIONS

        st.write("")
        st.write("")
        st.write("Operations")
        st.write("")

        if st.checkbox("Group By"):
            groub_by = st.multiselect("Select columns", data.columns)
            operations =["Mean", 'Sum']
            opera = st.selectbox("Select operation", operations)
            if len(groub_by) > 0 and opera is not None:

                if opera == 'Mean':
                    st.write(data.groupby(groub_by).mean())
                else:
                    st.write(data.groupby(groub_by).sum())

        
        if st.checkbox("Display part of data (row)"):
            from_ = st.number_input("From [index]", min_value=0, max_value=data.shape[0]-1)
            to_ = st.number_input("To [index]", min_value=1, max_value=data.shape[0])
            cols = st.multiselect("Select columns", data.columns)
            st.write(data.loc[from_:to_, cols])

        if st.checkbox("Merge data"):
            merge_file = st.file_uploader('Upload file to merge', type=['csv','xlsx'])
            if merge_file is not None:
                if 'csv' in merge_file.type.lower():
                    data2 = pd.read_csv(merge_file)

                else:
                    data2 = pd.read_excel(merge_file)

                if data2.empty:
                    st.write("Data is Empty")
                
                else:
                    how_merge = st.selectbox("Select how to merge", ['Inner','Left','Right','Outer', 'Cross'])

                    if how_merge is not None:
                        merged_ = data.merge(data2.sample(), how=how_merge.lower())
                        st.write(merged_)
                        st.download_button("Download csv", merged_.to_csv(index=False), 'text/csv')
                        

        # GRAPHS
        st.write("")
        st.write("")
        st.write("Visualization")
        st.write("")

        if st.checkbox("Bar Chart"):
            aaa = st.selectbox("Select columns to compare (Must be numerical data)", data.columns)

            if len(aaa) > 0:
                # fig = ff.create_distplot(data[aaa], aaa)
                st.bar_chart(data[aaa], use_container_width=True)

        if st.checkbox("Scatter Plot"):
            x = st.selectbox("Select your X", data.columns) 
            y = st.selectbox("Select your Y", data.columns)
            fig, ax = plt.subplots()

            ax.scatter(data[x],data[y])
            plt.xlabel = x
            plt.ylabel = y
            st.pyplot(fig)

        if st.checkbox("Pie Chart"):
            abc = st.selectbox("Select column", data.columns)

            if len(abc) > 0:
                fig, ax = plt.subplots()

                
                try:
                    ax.pie(data[abc],labels=data[abc].values)
                    st.pyplot(fig)
                except Exception:
                    pass