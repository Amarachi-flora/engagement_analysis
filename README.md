# YouTube Video Engagement Analysis – Mini Data Pipeline & KPI Dashboard

**Author:** Amarachi F. Onyedinma-N  
**Challenge:** Day 17 – Python Challenge @ ZION TECH HUB  
**Tools Used:** Python, Matplotlib

---

##  Introduction

With the increasing popularity of online video content, especially in education, it's critical to track performance metrics that reflect not just popularity (views) but also engagement and retention. This mini project explores the performance of five educational YouTube videos using a simplified analytics pipeline.

The goal is to design a lightweight but effective ETL process that extracts raw video data, transforms it to compute key performance indicators (KPIs), and visualizes these metrics in a simple dashboard. This exercise simulates real-world analytics tasks for content strategy and marketing insights.

---

##  Statement of the Problem

Content creators and analysts often struggle to go beyond surface-level video metrics. Views alone don't indicate how much value a video provides or how well it retains audience attention. There's a need to quantify deeper insights like retention, engagement, and conversion to guide better content decisions.

---

##  Objectives

- Simulate a lightweight ETL pipeline using Python  
- Compute critical KPIs such as retention rate, like rate, and conversion rate  
- Design a custom engagement score that reflects both watch time and user interactions  
- Visualize video performance for strategic analysis  
- Generate a summary report accessible to technical and non-technical stakeholders  

---

##  Data Description

The mock dataset consists of 5 educational videos, each with metadata including:
- `video_id`: Unique identifier  
- `title`: Name of the video  
- `views`: Number of total views  
- `likes`: Total likes received  
- `watch_time`: Total minutes watched  

---

##  Methodology

The process follows the ETL (Extract, Transform, Load) framework:

### 🔹 Extract
A static list of video data (views, likes, watch time) is loaded.

### 🔹 Transform
KPIs and engagement scores are computed using simple formulas:
- **Total & average watch time**
- **Like rate** = likes / views  
- **Conversion rate** = likes / watch time  
- **Retention rate** = total watch time / (views × avg video length)  
- **Engagement score** = (likes × 2) + (watch_time × 0.3)

### 🔹 Load
- KPIs printed and saved to a file: `kpi_report_v2.txt`  
- Visualization saved as: `engagement_scores.png`  

---

##  Key Performance Indicators (KPIs)

| Metric               | Value                         |
|----------------------|-------------------------------|
| Average Watch Time   | 2680.00 minutes               |
| Like Rate            | 0.22                          |
| Conversion Rate      | 0.05 (likes per min watched)  |
| Retention Rate       | 0.60                          |
| Most Popular Video   | "Data Science 101" (1800 views) |
| Highest Engagement   | "Data Science 101" (Score: 1756.0) |

These metrics help identify which videos keep users engaged and which are most effective at converting viewers to active participants.

---

##  Visualization Output

A horizontal bar chart was generated using **matplotlib** to showcase **Engagement Scores by Video**.  

**Filename:** `bar_chart.png`

This helps stakeholders quickly identify high-performing videos that combine views with meaningful engagement.

![Engagement Score Chart](day17-matplotlib-version/bar_chart.png)

---

##  Insights

-  **Top Performer:** *Data Science 101* excelled across all KPIs.  
-  **Improvement Areas:** *AI Explained* and *Intro to Python* showed lower engagement.  
-  **Retention Patterns:** Some videos had uneven watch time, suggesting need for improved pacing or delivery.

---

## Conclusion

This mini data-pipeline project shows how a simple ETL process can turn raw YouTube statistics into useful insights for better content strategy. Instead of just focusing on views, the dashboard highlights engagement as the real measure of success.

- “Data Science 101” stood out across all key metrics—engagement score, like rate, and viewer retention, likely because the topic is in high demand and the video delivered it in a clear, structured, and relatable way.  
- In contrast, videos like “AI Explained” and “Intro to Python” had lower engagement, possibly due to complex concepts being presented too broadly or lacking interactivity and pacing that keeps viewers engaged.  
- Retention overall is solid but uneven, highlighting where some videos could improve in storytelling, clarity, or delivery style.  
- The workflow is lightweight but scalable, making it easy to apply to more content or even full channel reviews.  

Even with a small dataset, this project shows how tracking the right metrics, not just view counts, can lead to smarter, data-driven content decisions.

---

##  Recommendations

1. **Build on what’s working:** Create more content around top-performing topics like *Data Science* and *Web Development*. Consider repurposing these videos into blog posts, short clips, or carousel content.  
2. **Improve weaker videos:** For *AI Explained*, break down complex topics more clearly. For *Intro to Python*, add interactivity and real-world examples.  
3. **Segment the audience:** Tailor content to beginners vs. advanced learners using audience pattern analysis.  
4. **Focus on retention strategies:** Strengthen the intro hooks, pacing, and call-to-actions to boost watch time and completion rates.  
5. **Promote high-performing content:** Feature successful topics in thumbnails and titles. Share snippets on social platforms to extend reach.  
6. **Encourage feedback:** Ask viewers what they'd like to see next. Use comments to guide future content strategy.

---

 *Thank you for reviewing this project. Connect with me to explore more data-driven insights.*
