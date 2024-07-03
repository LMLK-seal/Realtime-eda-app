<h1>Real-time Exploratory Data Analysis App</h1>

<p>This repository contains a Streamlit app that enables real-time Exploratory Data Analysis (EDA) of uploaded datasets.</p>
<img src="https://raw.githubusercontent.com/LMLK-seal/Realtime-eda-app/main/EDApp.jpg" alt="Real-time Exploratory Data Analysis App Screenshot" style="max-width: 100%; height: auto; margin: 20px 0;">
<h2>Features</h2>

<ul>
    <li><strong>Data Upload:</strong> Users can upload CSV or Excel files.</li>
    <li><strong>Data Exploration:</strong>
        <ul>
            <li><strong>Filtering:</strong> Select columns and apply filters to narrow down the data.</li>
            <li><strong>Sorting:</strong> Sort data by any column in ascending or descending order.</li>
            <li><strong>Data Subset Selection:</strong> Create specific subsets of data based on filters.</li>
        </ul>
    </li>
    <li><strong>Real-time Visualization:</strong>
        <ul>
            <li>Choose from scatter, bar, and line charts.</li>
            <li>Select X and Y axes for visualization.</li>
            <li>Charts update in real-time as you interact with the data (filters, sorting, etc.).</li>
        </ul>
    </li>
    <li><strong>Statistical Computations:</strong>
        <ul>
            <li>Calculate statistics (mean, median, standard deviation) on selected data subsets.</li>
            <li>Results update in real-time alongside visualization changes.</li>
        </ul>
    </li>
</ul>

<h2>Getting Started</h2>

<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone &lt;repository_url&gt;</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>cd realtime-eda-app
pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Run the App:</strong>
        <pre><code>streamlit run app.py</code></pre>
    </li>
</ol>

<h2>Deployment</h2>

<ul>
    <li><strong>Streamlit Cloud:</strong> The easiest way to deploy your app is on Streamlit Cloud. Follow these steps:
        <ul>
            <li>Go to <a href="https://streamlit.io/">https://streamlit.io/</a> and sign in.</li>
            <li>Click "Deploy" and choose "GitHub."</li>
            <li>Select your repository and branch.</li>
            <li>Streamlit Cloud will automatically detect your app.py and deploy your app. You'll receive a link to access your app.</li>
        </ul>
    </li>
</ul>

<h2>Contributing</h2>

<p>Contributions are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <strong>LICENSE</strong> file for details.</p>

<h2>Acknowledgements</h2>

<ul>
    <li>Streamlit: <a href="https://streamlit.io/">https://streamlit.io/</a></li>
    <li>Altair: <a href="https://altair-viz.github.io/">https://altair-viz.github.io/</a></li>
    <li>WebSockets: <a href="https://websockets.readthedocs.io/">https://websockets.readthedocs.io/</a></li>
</ul>
