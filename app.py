import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import time

# Page configuration
st.set_page_config(page_title="Real-Time Dashboard", page_icon="📊", layout="wide")

# Load the dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"
)

st.title("Real-Time Dashboard")

job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

placeholder = st.empty()

df = df[df["job"] == job_filter]

if df.empty:
    st.warning("No data available for the selected job.")
else:
    while True:
        df["age_new"] = df["age"] * np.random.choice((1, 3))
        df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

        # Creating KPIs
        avg_age = np.mean(df["age_new"])
        count_married = int(
            df[(df["marital"] == "married")]["marital"].count()
            + np.random.choice(range(1, 30))
        )
        balance = np.mean(df["balance_new"])

        with placeholder.container():
            # Create three columns
            kpi1, kpi2, kpi3 = st.columns(3)

            # Fill columns with respective KPIs
            kpi1.metric(label="Age ⌛", value=round(avg_age), delta=round(avg_age) - 10)
            kpi2.metric(
                label="Married Count 💍",
                value=int(count_married),
                delta=-10 + count_married,
            )
            kpi3.metric(
                label="A/C Balance 💸",
                value=f"$ {round(balance, 2)}",
                delta=(
                    -round(balance / count_married * 100) if count_married != 0 else 0
                ),
            )

            # Creating two columns for charts
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.markdown("## First Chart")
                fig1 = px.density_heatmap(data_frame=df, y='age_new', x="marital")
                st.write(key=fig1)

            with fig_col2:
                st.markdown("### Second Chart")
                fig2 = px.histogram(data_frame=df, x='age_new')
                st.write(key=fig2)
            # Creating two columns for charts
           

            st.markdown("### Detailed View")
            st.dataframe(df)
        time.sleep(0.5)
