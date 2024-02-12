import streamlit as st
from PIL import Image

title = 'Beyond the Waves: Charting Land-Based Material Spills in New York State'

introduction = """
Spills of materials onto Land in New York State might not always make the headlines, but they are critical to our environmental health. This report takes a closer look at these spills, examining how often they happen, what substances are involved, and where they're most prevalent. Our aim is to bring this issue to the forefront, promoting awareness and action to prevent and respond to these incidents.
"""
text_boxplot = """
Our journey through the data starts in the 1990s, where we see a consistent occurrence of small petroleum spills. There's a noticeable downtrend in these incidents since the 2000s, suggesting effective regulatory measures. This boxplot focuses on number of incidents, more imporantly though, is the magnitude of each spill.
"""

text_bubble1 = """After spliting spills into volume groups: Minor (below 30 Liters), Large (30-1000 Liters), and Major (above 1000 Liters),
we can tell that a few big spills have had a huge impact."""

text_bubble = """
Notably, the massive spill in 2018 was an outlier, being one of the largest in history. While it's important to recognize these rare events, they can distort our understanding of the data. Therefore, in our analysis, we'll focus on the more frequent, yet still significant spills, ensuring a clear picture of the typical spill volumes.
"""
#TODO: add box for 93% statistic

text_map = """
Mapping out spills shows us that not all areas are affected equally. 
Each county is represented by a circle on the map, with size and color indicating spill volume and material type.\n
The regions with the highest volumes of spills surround New York City, likely due to higher population density. Meanwhile, the counties with the most hazardous spills are grouped together in industrial areas. Guiding us to where prevention and response efforts are most crucial.
"""

text_sunburst = """
The reasons for spills vary by zone, and our sunburst charts lay this out. In industrial areas, a mix of causes such as equipment failures and human error lead to spills, while urban areas have a variety of reasons. This information helps us understand spill patterns and can inform specific strategies for spill prevention and cleanup operations.
"""

conclusion = """
This isn't just a collection of stats and graphs; it's a real-life story about land spills in New York. 
It's a call to action for us to make better policies, raise awareness, and protect our communities. 
Let's use these insights to tackle these spills head-on and keep our environment safe.
"""

# Set page config
st.set_page_config(layout="wide", page_title='Land-Spills New York State', page_icon="🌊", initial_sidebar_state="collapsed")

# Load images - replace with the actual paths to your images
viz1 = Image.open("viz1.png")
viz2 = Image.open("viz2.png")
viz4 = Image.open("viz4.png")

# Function to read HTML file
def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Title and Introduction
st.title(title)
st.write(introduction)

# Visualization 1: Boxplot
st.header("Spill Trends Over Three Decades")
col1, col2 = st.columns([3, 1])
with col1:
    st.image(viz1, caption="Annual Spill Incident Count by Material Family")
with col2:
    st.write(text_boxplot)

# Visualization 2: Bubble Chart
st.header("The Scale of Major Spills")
st.write(text_bubble1)
col1, col2 = st.columns([1, 3])
with col1:
    st.write(text_bubble)
with col2:
    st.image(viz2, caption="Visualizing the Volume of Major Spills")

# Visualization 3: Interactive Map
st.header("Mapping Spills Across New York")
st.write(text_map)
# Load and display the HTML file for the map
map3 = load_html("viz3.html")
st.components.v1.html(map3, height=600)

# Visualization 4: Sunburst Chart
st.header("Analyzing the Causes of Spills")
col1, col2 = st.columns([3, 1])
with col1:
    st.image(viz4, caption="Breakdown of Spill Causes by Zone")
with col2:
    st.write(text_sunburst)

# Conclusion
st.header("Moving Forward")
st.write(conclusion)