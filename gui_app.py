import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Dark mode theme
st.set_page_config(page_title='CloudCost VizPro', layout='wide', initial_sidebar_state='expanded')
st.markdown("""<style>.main {background-color: #1e1e2f; color: #ffffff;}</style>""", unsafe_allow_html=True)

# Title
st.title('CloudCost VizPro - Real-Time Cloud Spending Analyzer')

# Sidebar for filters
st.sidebar.header('Filters')
cloud_provider = st.sidebar.selectbox('Select Cloud Provider', ['AWS', 'Azure', 'Google Cloud'])
date_range = st.sidebar.date_input('Select Date Range', [])

# Live status indicator
st.sidebar.markdown('### Live Status')
status = st.sidebar.progress(0)
for i in range(100):
    status.progress(i + 1)

# Generate sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Cost': np.random.randint(100, 1000, size=30)
})

# Interactive charts
st.markdown('### Cloud Spending Over Time')
fig = px.line(data, x='Date', y='Cost', title='Cloud Cost Over Time', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)

st.markdown('### Cost Breakdown by Service')
service_data = pd.DataFrame({
    'Service': ['Compute', 'Storage', 'Networking', 'Database'],
    'Cost': np.random.randint(100, 500, size=4)
})
fig2 = px.pie(service_data, values='Cost', names='Service', title='Cost Breakdown by Service', template='plotly_dark')
st.plotly_chart(fig2, use_container_width=True)

# Input fields for budget
st.markdown('### Budget Management')
budget = st.number_input('Set Monthly Budget ($)', min_value=0, value=1000)
current_spending = data['Cost'].sum()
st.markdown(f'**Current Spending:** ${current_spending}')
st.markdown(f'**Remaining Budget:** ${budget - current_spending}')

# Progress bar for budget
st.markdown('### Budget Utilization')
budget_utilization = (current_spending / budget) * 100
st.progress(int(budget_utilization))
