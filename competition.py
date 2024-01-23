import pandas as pd
import streamlit as st
import os

st.set_page_config(page_title='Competition', layout='wide')

# Read data from Sheet 
df = pd.read_csv('Africa 2024-.csv')

# Define the folder path for photos
photos_folder = 'photos'

# Display images and results in the Streamlit app
st.header('Competition Results')

st.markdown("""
<style>
.rainbow-divider {
    background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
    height: 2px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="rainbow-divider"></div>', unsafe_allow_html=True)

# Display contestant photos and results in the same row
for index, row in df.iterrows():
    col1, col2, col3, col4 = st.columns(4, gap='large')  # Divide the row into 3 parts
    
    # Convert the 'Photo_URL' value to string and construct the full path to the image
    image_path = os.path.join(photos_folder, str(row['Photo_URL']))

    try:
        col1.image(image_path, width=200)
    except Exception as e:
        col1.error(f"Error loading image for {row['Contestant']}: {str(e)}")
    with col2:
        st.info(f"{index + 1}. {row['Contestant']} ")
        st.metric(label=f":red[_Score:_] :blue[_{row['Score']}_]", value='')
