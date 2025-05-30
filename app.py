import streamlit as st
import pandas as pd
import altair as alt

# ----------------------
# Sample Data
# ----------------------
data = [
    {"video_id": "vid1", "title": "Intro to Python", "views": 1500, "likes": 300, "watch_time": 3500},
    {"video_id": "vid2", "title": "Data Science 101", "views": 1200, "likes": 400, "watch_time": 4200},
    {"video_id": "vid3", "title": "AI Explained", "views": 900, "likes": 150, "watch_time": 1800},
    {"video_id": "vid4", "title": "Machine Learning Crash Course", "views": 1700, "likes": 320, "watch_time": 2900},
    {"video_id": "vid5", "title": "Build a Website", "views": 2100, "likes": 500, "watch_time": 4000}
]

df = pd.DataFrame(data)

# ----------------------
# Calculations
# ----------------------
total_views = df["views"].sum()
total_likes = df["likes"].sum()
total_watch_time = df["watch_time"].sum()

avg_watch_time = round(total_watch_time / len(df), 2)
like_rate = round(total_likes / total_views, 4)
conversion_rate = round(total_likes / total_watch_time, 4)
avg_video_length = 2  # minutes
retention_rate = round(total_watch_time / (total_views * avg_video_length), 4)

df["engagement_score"] = round((df["likes"] * 2) + (df["watch_time"] * 0.3), 2)
most_engaging_video = df.loc[df["engagement_score"].idxmax()]
most_popular_video = df.loc[df["views"].idxmax()]

# ----------------------
# App Layout
# ----------------------
st.set_page_config(page_title="YouTube Engagement Dashboard", layout="wide")
st.title("YouTube Engagement Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Like Rate (likes/views)", f"{like_rate}")
col2.metric("Conversion Rate (likes/min)", f"{conversion_rate}")
col3.metric("Avg. Watch Time (mins)", f"{avg_watch_time}")
col4.metric("Retention Rate", f"{retention_rate}")

st.markdown("---")

col5, col6 = st.columns(2)
col5.markdown(f"**Most Engaging Video:** {most_engaging_video['title']} — Score: {most_engaging_video['engagement_score']}")
col6.markdown(f"**Most Viewed Video:** {most_popular_video['title']} — Views: {most_popular_video['views']}")

# ----------------------
# Enhanced Chart with Colors and Data Labels
# ----------------------
st.subheader("Engagement Score by Video")

color_scale = alt.Scale(scheme='category20b')  
bar_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('title:N', sort='-y', title="Video Title"),
    y=alt.Y('engagement_score:Q', title="Engagement Score"),
    color=alt.Color('title:N', scale=color_scale),
    tooltip=["title", "views", "likes", "watch_time", "engagement_score"]
).properties(width=800, height=400)

text = alt.Chart(df).mark_text(
    align='center',
    baseline='bottom',
    dy=-5,
    fontSize=12
).encode(
    x=alt.X('title:N', sort='-y'),
    y='engagement_score:Q',
    text='engagement_score:Q'
)

st.altair_chart(bar_chart + text, use_container_width=True)

# ----------------------
# Data Table
# ----------------------
st.subheader("Raw Data Table")
st.dataframe(df)

# ----------------------
# Insights + Conclusion + Recommendations
# ----------------------
st.subheader("Insights and Analysis")

st.markdown("""
### Performance Insights:
- **Data Science 101** outperforms all videos in engagement score despite having fewer views than some. This indicates **higher viewer quality**, likely due to a **targeted topic** and **strong relevance** to the audience.
- **Build a Website** is the most viewed video, suggesting **broad appeal**, but its lower engagement score per view indicates **less depth of interaction** — possibly due to casual viewers who drop off early or don't like the video.
- **AI Explained** received the **lowest engagement**, which could be due to **complexity**, lack of clarity, or insufficient SEO targeting. It may need improvement in **presentation, thumbnails, or audience match**.
- **Intro to Python** and **Machine Learning Crash Course** maintained balanced engagement and performance — a good signal of consistent content value and clarity.
 
 

### Conclusion:
The dashboard reveals that **engagement is not only driven by views**, but by how relevant and valuable the content is to its audience. Videos with moderate views but high like-to-watch ratios are more effective in building a loyal audience.



### Recommendations:
1. **Double Down on What Works**: Create follow-up content related to *Data Science 101* and *Intro to Python*. These formats clearly resonate well.
2. **Improve Underperformers**: Review *AI Explained* for pacing, design, and clarity. Test new titles or restructure the content for accessibility.
3. **Optimize for Engagement, Not Just Views**: Add **calls to action**, **interactive visuals**, or **clear takeaways** at key video timestamps.
4. **Audience Segmentation**: Group viewers by topic interest and personalize video suggestions based on prior engagement scores.
5. **A/B Test Thumbnails and Titles**: First impressions matter. Use analytics to test versions and track improvement in CTR and retention.
""")
