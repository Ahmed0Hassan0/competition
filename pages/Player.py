import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Player statistics', page_icon='📈' ,layout='wide')
st.balloons()
df_player = pd.read_excel('Datasets/Africa 2024-.xlsx', sheet_name='التوقعات')
df_player = df_player.dropna()
player_list = df_player['name'].unique()
players = pd.DataFrame(player_list)

st.sidebar.image('photos/logo2.jpg')
st.sidebar.header('Select a player')
add_selectbox = st.sidebar.selectbox(
    '',
    ['',*players[0]]
)



if add_selectbox == '':
    st.subheader('Please select a player ! ');
else:
    select_player = df_player[df_player['name'] == add_selectbox]
    player_name = 'Player name: ' + add_selectbox
    st.header(player_name)

    def main():
        col1, col2, col3 = st.columns(3, gap='large')
        

        
        exact_true_prediction = select_player[select_player['Total'] == 5]
        exact_true_prediction_result = exact_true_prediction[['Match', 'Prediction', 'Result']]
        exact_true_prediction_result.reset_index(inplace=True, drop=True)
        exact_true_prediction_result.index.name = 'No.'
        exact_true_prediction_result.index = np.arange(1, len(exact_true_prediction_result) + 1)
        
        true_prediction = select_player[select_player['Total'] == 3]
        true_prediction_result = true_prediction[['Match', 'Prediction', 'Result']]
        true_prediction_result.reset_index(inplace=True, drop=True)
        true_prediction_result.index.name = 'No.'
        true_prediction_result.index = np.arange(1, len(true_prediction_result) + 1)
    
        false_prediction = select_player[select_player['Total'] == 0]
        false_prediction_result = false_prediction[['Match', 'Prediction', 'Result']]
        false_prediction_result.reset_index(inplace=True, drop=True)
        false_prediction_result.index.name = 'No.'
        false_prediction_result.index = np.arange(1, len(false_prediction_result) + 1)    
        
        with col1:
            st.info('توقع الفائز')
            st.dataframe(true_prediction_result)
        with col2:
            st.info('توقعات صحيحة')
            st.dataframe(exact_true_prediction_result)
        with col3:
            st.info('توقعات غير صحيحة')
            st.dataframe(false_prediction_result)



    main()
