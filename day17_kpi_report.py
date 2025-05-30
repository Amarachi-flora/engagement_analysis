"""
Day 17 Python Challenge. Mini Data Pipeline + KPI Dashboard with Charts
Author: Amarachi F. Onyedinma-N
------------------------------------------------------------
This script includes:
    1. ETL process (Extract, Transform, Load)
    2. KPI calculation
    3. Matplotlib visualization
"""

import matplotlib.pyplot as plt

# ------------------------ 1) EXTRACT ------------------------

avg_video_length = 3  # in minutes

videos = [
    {"video_id": "v001", "title": "Intro to Python", "views": 1500, "likes": 300, "watch_time": 2500},
    {"video_id": "v002", "title": "Data Science 101", "views": 1800, "likes": 420, "watch_time": 3100},
    {"video_id": "v003", "title": "AI Explained", "views": 1200, "likes": 280, "watch_time": 2200},
    {"video_id": "v004", "title": "Build a Website", "views": 2100, "likes": 390, "watch_time": 2900},
    {"video_id": "v005", "title": "Machine Learning Intro", "views": 1700, "likes": 360, "watch_time": 2700},
]

# --------------------- 2) TRANSFORM / KPIs ------------------

total_watch_time = sum(v["watch_time"] for v in videos)
total_views = sum(v["views"] for v in videos)
total_likes = sum(v["likes"] for v in videos)

average_watch_time = total_watch_time / len(videos)
like_rate = total_likes / total_views
conversion_rate = total_likes / total_watch_time
retention_rate = total_watch_time / (total_views * avg_video_length)

for v in videos:
    v["engagement_score"] = v["likes"] * 2 + 0.3 * v["watch_time"]

most_popular = max(videos, key=lambda v: v["views"])
highest_engagement = max(videos, key=lambda v: v["engagement_score"])

# ------------------------- 3) LOAD --------------------------

report_lines = [
    "KPI Report – Enhanced Version",
    "----------------------------------",
    f"Average Watch Time       : {average_watch_time:.2f} minutes",
    f"Like Rate                : {like_rate:.2f}",
    f"Conversion Rate          : {conversion_rate:.2f} (likes per min watched)",
    f"Retention Rate           : {retention_rate:.2f}",
    f"Most Popular Video       : \"{most_popular['title']}\" ({most_popular['views']} views)",
    f"Highest Engagement Video : \"{highest_engagement['title']}\" (Score: {highest_engagement['engagement_score']:.2f})",
]

print("\n".join(report_lines))

with open("kpi_report_v2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print("\nEnhanced report saved to kpi_report_v2.txt")

# ---------------------- 4) VISUALIZE -----------------------

# Bar chart: Engagement Scores
titles = [v["title"] for v in videos]
engagement_scores = [v["engagement_score"] for v in videos]

plt.figure(figsize=(10, 6))
plt.barh(titles, engagement_scores, color="skyblue")
plt.xlabel("Engagement Score")
plt.title("Engagement Score by Video")
plt.tight_layout()
plt.savefig("engagement_scores.png")
plt.show()
