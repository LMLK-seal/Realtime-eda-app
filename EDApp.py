import streamlit as st
import pandas as pd
import altair as alt
import websockets
import asyncio
import json
import multiprocessing  # Added for multithreading

# --- Data Upload ---

st.title("Real-time Exploratory Data Analysis")

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error uploading file: {e}")
else:
    st.info("Please upload a file to begin.")

# --- Data Exploration ---

if "df" in locals():
    st.subheader("Data Exploration")

    # Filters
    filter_columns = st.multiselect("Select columns to filter:", df.columns)
    filters = {}
    for col in filter_columns:
        if df[col].dtype == "object":
            filters[col] = st.multiselect(f"Filter {col}:", df[col].unique())
        else:
            filters[col] = st.slider(f"Filter {col}:", min_value=df[col].min(), max_value=df[col].max(), value=(df[col].min(), df[col].max()))

    # Sorting
    sort_column = st.selectbox("Sort by column:", df.columns)
    ascending = st.checkbox("Ascending", True)

    # Data Subset
    subset = df.copy()
    for col, filter_values in filters.items():
        if len(filter_values) > 0:
            subset = subset[subset[col].isin(filter_values)]
    subset = subset.sort_values(by=sort_column, ascending=ascending)

# --- Real-time Visualization ---

    st.subheader("Real-time Visualization")

    # Chart Type
    chart_type = st.selectbox("Select chart type:", ["Scatter", "Bar", "Line"])

    # Chart Options
    x_axis = st.selectbox("X-axis:", subset.columns)
    y_axis = st.selectbox("Y-axis:", subset.columns)

    # Chart Generation
    if chart_type == "Scatter":
        chart = alt.Chart(subset).mark_point().encode(
            alt.X(x_axis),
            alt.Y(y_axis)
        )
    elif chart_type == "Bar":
        chart = alt.Chart(subset).mark_bar().encode(
            alt.X(x_axis),
            alt.Y(y_axis)
        )
    else:
        chart = alt.Chart(subset).mark_line().encode(
            alt.X(x_axis),
            alt.Y(y_axis)
        )
    
    # Display Chart
    st.altair_chart(chart, use_container_width=True)

# --- Real-time Updates with WebSockets (using multithreading) ---
def start_websocket_server():
    async def handle_websocket(websocket):
        async for message in websocket:
            data = json.loads(message)
            # Update chart or perform statistical computation based on data received
            if data.get("chart_type") == "Scatter":
                # Update scatter chart based on new data
                pass
            elif data.get("chart_type") == "Bar":
                # Update bar chart based on new data
                pass
            else:
                # Update line chart based on new data
                pass

    async def main():
        async with websockets.serve(handle_websocket, "localhost", 8765):
            await asyncio.Future()

    asyncio.run(main())

    # Start WebSocket server in a separate process
    process = multiprocessing.Process(target=start_websocket_server)
    process.start()

# --- Statistical Computations ---

    st.subheader("Statistical Computations")

    # Compute statistics on selected data subset
    # Display results in real-time as user interacts with the data
    # Example:
    # st.write(f"Mean of {x_axis}: {subset[x_axis].mean()}")
    # st.write(f"Median of {y_axis}: {subset[y_axis].median()}")
