 YouTube Video Engagement Analysis

This repository contains two Python projects analyzing YouTube video performance using static and interactive visualizations.

---

## Version 1 – Matplotlib (Static Dashboard)
**Folder:** day17-matplotlib-version

This project extracts key YouTube video metrics such as total views, likes, comments, and average watch time. It generates a **static bar chart** visualizing video performance to help understand engagement at a glance.

### Key Features
- Extracts and calculates KPIs including average watch time and total engagement.
- Creates static visualizations using Matplotlib.
- Provides a simple, clear overview of video performance.

### Usage
Run the script `matplotlib_dashboard.py` to generate the bar chart image.

### Bar Chart Preview
<img src="./day17-matplotlib-version/engagement_scores.png" alt="Engagement Scores Bar Chart" width="75%" />


---

## Version 2 – Streamlit (Interactive Dashboard)
**Folder:** day17-streamlit-version

An interactive Streamlit dashboard allows dynamic exploration of video KPIs using sliders and filters. It showcases an interactive mini ETL pipeline with real-time metrics and charts.

**Live Demo:** [Click to View the App](https://your-username.streamlit.app/)

### Key Features
- Real-time KPI display using `st.metric()`
- Identifies most popular and highest engagement video
- Interactive horizontal bar chart of engagement scores
- Clean, minimalist UI with Streamlit

---

# Project Structure
DAY17-METRICS.CODE-WORKSHOP
├── day17-matplotlib-version/
│ ├── engagement_scores.png
│ ├──kpi_report_vs.txt
│ ├──README.md
│ ├──reports.pdf
│ ├── video_kpi_static.py
│ 
├── day17-streamlit-version/
│ ├── app.py
└ ├── requirements.txt

---

## Tech Stack
- Python
- Matplotlib (static visualization)
- Streamlit (interactive visualization)
- VSCode Workspace
- Git & GitHub

---

## How to Run (Matplotlib Version)

1. Make sure you have Python and Matplotlib installed:
   ```bash
   pip install matplotlib


## Run the dashboard script to generate the bar chart:

    python day17-matplotlib-version/matplotlib_dashboard.py

    The bar chart image bar_chart.png will be saved inside the day17-matplotlib-version folder.


## Sample KPIs Calculated

    Total Views

    Total Likes

    Total Comments

    Average Watch Time

    Engagement Scores (derived metrics)


## Streamlit Version

    Clone the repo and install dependencies:

git clone https://github.com/Amarachi-flora/YOUTUBE-VIDEO-ENGAGEMENT-ANALYSIS.git
cd day17-streamlit-version
pip install -r requirements.txt

## Run the Streamlit app locally:

    streamlit run app.py

    Open the dashboard in your browser at http://localhost:8501.



## Notes

### For interactive exploration, check out the Streamlit dashboard in the day17-streamlit-version folder, which provides dynamic KPIs, filters, and real-time visualization. Feel free to explore both versions for complementary insights into YouTube video engagement.
