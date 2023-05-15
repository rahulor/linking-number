import streamlit as st
# configure page
#--------------------------------------------------------------------------------------------
st.set_page_config(
     page_title="Linking number",
     page_icon=":knot:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
        #'Get Help': 'https://www.extremelycoolapp.com/help',
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "The loop-maker app creates random loops."
     })
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1.2rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.subheader(":blue[Linking number]")
#--------------------------------------------------------------------------------------------
# imorts 
import numpy as np
import plotly.graph_objects as go
import helper
#--------------------------------------------------------------------------------------------
def create_the_sidebar():
     with st.sidebar:
          pass
     
@st.cache_data
def draw_the_loops(loops):
     R1x, R1y, R1z, R2x, R2y, R2z = loops.T
     cubesize = 0.6
     axis = dict(range=[-cubesize,cubesize], nticks=4,)
     fig = go.Figure(layout=go.Layout(
          height=400, width=300, uirevision=True, 
          scene=dict(
               aspectmode='cube', 
               aspectratio=dict(x=1, y=1, z=1),
               xaxis = axis, yaxis = axis, zaxis = axis)
          ))
     fig.add_trace(go.Scatter3d(x=R1x, y=R1y, z=R1z, mode='lines', showlegend=False, 
                    line=dict(color='red', width=4.0), opacity=0.5,
                    ))
     fig.add_trace(go.Scatter3d(x=R2x, y=R2y, z=R2z, mode='lines', showlegend=False, 
                    line=dict(color='blue', width=4.0), opacity=0.5,
                    ))
     st.plotly_chart(fig)
     return


def main(rows=3, columns=5):
     loops_list, label_list = helper.unpickle_from('data/train_loops_labels')
     cols = st.columns([1]*columns, gap="small")
     random_index = np.random.randint(low=0, high=len(label_list), size=rows*columns)
     for j in range(rows):
          for i, col in enumerate(cols, start = j*5):
               with col:
                    idx = random_index[i]
                    draw_the_loops(loops_list[idx])
                    Lktext  = f'<div align="center">  Lk = {str(label_list[idx])}  </div>'
                    st.write("", Lktext , unsafe_allow_html=True)

#     streamlit run curve.py --server.headless true &  
if __name__ == "__main__":
     main(rows=3, columns=5)
