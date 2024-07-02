# Real-time Exploratory Data Analysis App

This repository contains a Streamlit app that enables real-time Exploratory Data Analysis (EDA) of uploaded datasets.

## Features

- **Data Upload:** Users can upload CSV or Excel files.
- **Data Exploration:** 
    - **Filtering:** Select columns and apply filters to narrow down the data.
    - **Sorting:** Sort data by any column in ascending or descending order.
    - **Data Subset Selection:**  Create specific subsets of data based on filters.
- **Real-time Visualization:**
    - Choose from scatter, bar, and line charts.
    - Select X and Y axes for visualization.
    - Charts update in real-time as you interact with the data (filters, sorting, etc.).
- **Statistical Computations:** 
    - Calculate statistics (mean, median, standard deviation) on selected data subsets.
    - Results update in real-time alongside visualization changes.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
Use code with caution.
Markdown
Install Dependencies:
cd realtime-eda-app
pip install -r requirements.txt
Use code with caution.
Bash
Run the App:
streamlit run app.py
Use code with caution.
Bash
Deployment
Streamlit Cloud: The easiest way to deploy your app is on Streamlit Cloud. Follow these steps:
Go to https://streamlit.io/ and sign in.
Click "Deploy" and choose "GitHub."
Select your repository and branch.
Streamlit Cloud will automatically detect your app.py and deploy your app. You'll receive a link to access your app.
Contributing
Contributions are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements
Streamlit: https://streamlit.io/
Altair: https://altair-viz.github.io/
WebSockets: https://websockets.readthedocs.io/
