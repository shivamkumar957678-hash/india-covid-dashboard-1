# ================= INSTALL FIRST =================
# pip install streamlit pandas plotly folium streamlit-folium

# ================= IMPORT =================
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

# ================= PAGE =================
st.set_page_config(
    page_title="India COVID Dashboard",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

html, body, [class*="css"]{
    background-color:#02133b;
    color:white;
    font-family:Arial;
}

.main{
    background:#02133b;
}

section[data-testid="stSidebar"]{
    background:#031446;
    border-right:2px solid #00e5ff;
}

.sidebar-title{
    text-align:center;
    font-size:26px;
    font-weight:bold;
    color:#00e5ff;
    line-height:1.8;
    margin-top:20px;
}

.menu{
    color:white;
    font-size:20px;
    line-height:2.2;
    margin-top:20px;
}

.card{
    background:#17357f;
    padding:15px;
    border-radius:20px;
    text-align:center;
    height:180px;
}

.card1{
    border:3px solid #00e5ff;
    box-shadow:0 0 20px #00e5ff;
}

.card2{
    border:3px solid #00ff66;
    box-shadow:0 0 20px #00ff66;
}

.card3{
    border:3px solid #ff00c8;
    box-shadow:0 0 20px #ff00c8;
}

.card4{
    border:3px solid #ffd000;
    box-shadow:0 0 20px #ffd000;
}

.card-title{
    color:white;
    font-size:24px;
    font-weight:bold;
}

.card-value{
    color:white;
    font-size:36px;
    margin-top:20px;
    font-weight:bold;
}

.heading{
    color:#00e5ff;
    font-size:26px;
    font-weight:bold;
    margin-top:10px;
}

.box{
    background:#1a3c8b;
    border-radius:20px;
    padding:20px;
    border:2px solid #00e5ff;
}

.footer-box{
    background:#04204f;
    border-radius:20px;
    border:2px solid #00e5ff;
    padding:25px;
    text-align:center;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.markdown("""
<div class='sidebar-title'>
🦠 COVID-19 <br>
INDIA <br>
DASHBOARD
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class='menu'>
📍 Dashboard <br>
📈 Prediction <br>
🗺️ Map <br>
🤖 AI Chatbot <br>
ℹ️ About
</div>
""", unsafe_allow_html=True)

st.sidebar.success("Stay Safe ❤️")

# ================= MADE BY =================
st.sidebar.markdown("""
<div style='
background:#04204f;
border:2px solid #00e5ff;
border-radius:20px;
padding:20px;
text-align:center;
margin-top:30px;'>

<h3 style='color:white;'>Made with ❤️ by</h3>

<h2 style='color:#00e5ff;'>
Shivam Kumar
</h2>

</div>
""", unsafe_allow_html=True)

# ================= 28 STATES DATA =================

states = [
"Maharashtra","Tamil Nadu","Karnataka","Kerala","Uttar Pradesh",
"Delhi","West Bengal","Odisha","Rajasthan","Andhra Pradesh",
"Bihar","Madhya Pradesh","Punjab","Haryana","Gujarat",
"Assam","Jharkhand","Chhattisgarh","Goa","Tripura",
"Manipur","Nagaland","Mizoram","Sikkim","Uttarakhand",
"Himachal Pradesh","Jammu Kashmir","Arunachal Pradesh"
]

cases = [
6460317,4359355,3874910,3671375,3228213,
2901795,2109875,1800000,1500000,1400000,
1200000,1100000,1000000,980000,960000,
850000,830000,800000,700000,650000,
620000,600000,550000,500000,450000,
420000,400000,350000
]

recovered = [
5878888,3959260,3532169,3342551,2939001,
2700000,1900000,1700000,1400000,1300000,
1100000,1000000,950000,900000,920000,
800000,780000,760000,680000,600000,
590000,570000,520000,470000,420000,
400000,380000,330000
]

deaths = [
71001,47289,42624,40385,25511,
24000,20000,12000,9000,8500,
7000,6500,6000,5800,5400,
5000,4500,4200,3000,2500,
2200,2100,1800,1500,1400,
1300,1200,1000
]

active = [
510428,352806,300117,288439,263701,
210000,180000,90000,60000,50000,
45000,42000,39000,36000,34000,
32000,30000,28000,25000,22000,
21000,19000,17000,15000,13000,
12000,11000,9000
]

df = pd.DataFrame({
    "State":states,
    "Cases":cases,
    "Recovered":recovered,
    "Deaths":deaths,
    "Active":active
})

# ================= STATE SELECT =================

selected_state = st.selectbox("Select State", states)

row = df[df["State"] == selected_state].iloc[0]

# ================= TITLE =================

st.markdown("""
<h1 style='text-align:center;
color:#00e5ff;
text-shadow:0 0 15px #00e5ff;'>
📊 INDIA COVID-19 ANALYTICS DASHBOARD 🦠
</h1>
""", unsafe_allow_html=True)

# ================= CARDS =================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='card card1'>
    <div class='card-title'>👨‍👩‍👧 TOTAL CASES</div>
    <div class='card-value'>{row['Cases']:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='card card2'>
    <div class='card-title'>✅ RECOVERED</div>
    <div class='card-value'>{row['Recovered']:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='card card3'>
    <div class='card-title'>💔 DEATHS</div>
    <div class='card-value'>{row['Deaths']:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='card card4'>
    <div class='card-title'>☀️ ACTIVE CASES</div>
    <div class='card-value'>{row['Active']:,}</div>
    </div>
    """, unsafe_allow_html=True)

# ================= FILTERS =================

f1,f2 = st.columns(2)

with f1:
    st.markdown("<div class='heading'>🔎 SEARCH STATE</div>", unsafe_allow_html=True)
    state = st.selectbox("STATE", states)

with f2:
    st.markdown("<div class='heading'>💉 VACCINATION ANALYTICS</div>", unsafe_allow_html=True)
    year = st.selectbox("SELECT YEAR",[2020,2021,2022,2023])

# ================= VACCINATION + PIE =================

v1,v2 = st.columns(2)

with v1:

    st.markdown("""
    <div class='box'>
    <h1 style='text-align:center;color:white;'>
    YEAR 2021 VACCINATION
    </h1>

    <h2 style='color:#00e5ff;'>👶 Child Vaccinated : 62%</h2>
    <h2 style='color:#00ff66;'>🧑 Adult Vaccinated : 71%</h2>
    <h2 style='color:#ff66cc;'>👴 Old Vaccinated : 48%</h2>

    </div>
    """, unsafe_allow_html=True)

with v2:

    pie = go.Figure(data=[go.Pie(
        labels=["Child","Adult","Old"],
        values=[62,71,48],
        hole=0.5
    )])

    pie.update_layout(
        title="VACCINATION DISTRIBUTION 2021",
        title_font=dict(size=28,color="white"),
        paper_bgcolor="#1a3c8b",
        plot_bgcolor="#1a3c8b",
        font=dict(color="white")
    )

    st.plotly_chart(pie,use_container_width=True)

# ================= LINE + BAR =================

g1,g2 = st.columns(2)

with g1:

    line = px.line(
        x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
        y=[120000,220000,340000,450000,560000,700000,800000,720000,550000,470000,320000,180000]
    )

    line.update_layout(
        title="📈 MONTHLY CASES TREND",
        title_font=dict(size=28,color="white"),
        paper_bgcolor="#1a3c8b",
        plot_bgcolor="#1a3c8b",
        font=dict(color="white")
    )

    st.plotly_chart(line,use_container_width=True)

with g2:

    bar = px.bar(df,x="State",y="Cases",color="Cases")

    bar.update_layout(
        title="📊 ALL STATES CASES",
        title_font=dict(size=28,color="white"),
        paper_bgcolor="#1a3c8b",
        plot_bgcolor="#1a3c8b",
        font=dict(color="white")
    )

    st.plotly_chart(bar,use_container_width=True)

# ================= PIE + TABLE =================

p1,p2 = st.columns(2)

with p1:

    pie2 = px.pie(df,names="State",values="Cases",hole=0.5)

    pie2.update_layout(
        title="🧬 COVID DISTRIBUTION",
        title_font=dict(size=28,color="white"),
        paper_bgcolor="#1a3c8b",
        plot_bgcolor="#1a3c8b",
        font=dict(color="white")
    )

    st.plotly_chart(pie2,use_container_width=True)

with p2:

    st.markdown("""
    <h1 style='color:#00e5ff;'>
    📋 ALL STATES DATA
    </h1>
    """, unsafe_allow_html=True)

    st.dataframe(df,use_container_width=True)

# ================= FULL SCREEN MAP =================

st.markdown("""
<h1 style='color:#00e5ff;'>
🗺️ INDIA COVID MAP
</h1>
""", unsafe_allow_html=True)

india_map = folium.Map(
    location=[22.5,78.9],
    zoom_start=5,
    tiles="cartodbpositron"
)

locations = [
[19.07,72.87],[13.08,80.27],[12.97,77.59],[8.52,76.93],
[26.84,80.94],[28.61,77.20],[22.57,88.36],[20.29,85.82],
[26.91,75.78],[16.50,80.64],[25.59,85.13],[23.25,77.41],
[30.90,75.85],[28.45,77.01],[23.02,72.57],[26.14,91.73],
[23.34,85.30],[21.25,81.63],[15.49,73.82],[23.84,91.28],
[24.81,93.95],[25.67,94.11],[23.72,92.71],[27.33,88.61],
[30.31,78.03],[31.10,77.17],[34.08,74.79],[27.10,93.62]
]

for i in range(len(states)):

    folium.CircleMarker(
        location=locations[i],
        radius=8,
        popup=f"""
        <b>{states[i]}</b><br>
        Cases: {cases[i]}<br>
        Recovered: {recovered[i]}<br>
        Deaths: {deaths[i]}<br>
        Active: {active[i]}
        """,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=1
    ).add_to(india_map)

st_folium(
    india_map,
    width=1400,
    height=700
)

# ================= CHATBOT =================
# ================= CHATBOT =================

st.markdown("""
<div class='box'>

<h1 style='color:#00e5ff;'>
🤖 AI COVID CHATBOT
</h1>

<h2 style='color:#00ff66;'>
Hello! I am your AI COVID Assistant.
</h2>

<h3 style='color:#ffd700;'>
All 28 States COVID Data Available ✅
</h3>

<p style='font-size:20px;color:white;'>
Ask anything about COVID-19 in India.
</p>

</div>
""", unsafe_allow_html=True)

# ================= TYPES OF QUESTIONS =================

st.markdown("""
<div style='
background:#17357f;
padding:25px;
border-radius:25px;
border:3px solid #00e5ff;
margin-top:20px;
box-shadow:0 0 20px #00e5ff;'>

<h2 style='
color:#00e5ff;
font-size:38px;
text-align:center;
font-weight:bold;'>

📌 TYPES OF QUESTIONS

</h2>

<hr style='border:2px solid cyan;'>

<div style='
font-size:24px;
color:white;
line-height:2.2;
font-weight:bold;'>

✅ Bihar cases 2022 <br><br>

✅ Maharashtra active cases <br><br>

✅ Delhi vaccination data <br><br>

✅ Karnataka death cases <br><br>

✅ Tamil Nadu recovered cases <br><br>

✅ Uttar Pradesh COVID data <br><br>

✅ India total cases <br><br>

✅ Top state by cases <br><br>

✅ Lowest active cases <br><br>

✅ What is COVID-19? <br><br>

✅ What is vaccination? <br><br>

✅ What is active case? <br><br>

</div>

</div>
""", unsafe_allow_html=True)

# ================= QUESTION BOX =================

question = st.text_input(
    "💬 TYPE YOUR QUESTION..."
).lower().strip()

response = ""

# ================= STATE QUESTIONS =================

for i, s in enumerate(states):

    state_name = s.lower()

    if state_name in question and "case" in question:

        response = f"""
📍 {s} COVID REPORT

🦠 Total Cases : {cases[i]:,}

💚 Recovered : {recovered[i]:,}

❤️ Active Cases : {active[i]:,}

💀 Deaths : {deaths[i]:,}

💉 Vaccination : 82%
"""

    elif state_name in question and "active" in question:

        response = f"""
📍 {s}

❤️ Active Cases : {active[i]:,}
"""

    elif state_name in question and "recover" in question:

        response = f"""
📍 {s}

💚 Recovered Cases : {recovered[i]:,}
"""

    elif state_name in question and "death" in question:

        response = f"""
📍 {s}

💀 Death Cases : {deaths[i]:,}
"""

    elif state_name in question and (
        "vaccination" in question or
        "vaccine" in question
    ):

        response = f"""
📍 {s}

💉 Vaccination Completed : 82%

👶 Child Vaccinated : 62%

🧑 Adult Vaccinated : 71%

👴 Old Vaccinated : 48%
"""

# ================= INDIA QUESTIONS =================

if "india total" in question:

    response = f"""
🇮🇳 INDIA TOTAL COVID DATA

🦠 Total Cases : {sum(cases):,}

💚 Total Recovered : {sum(recovered):,}

❤️ Active Cases : {sum(active):,}

💀 Deaths : {sum(deaths):,}
"""

if "top state" in question:

    max_case = max(cases)
    idx = cases.index(max_case)

    response = f"""
🏆 TOP STATE BY CASES

📍 State : {states[idx]}

🦠 Cases : {cases[idx]:,}
"""

if "lowest active" in question:

    min_active = min(active)
    idx = active.index(min_active)

    response = f"""
✅ LOWEST ACTIVE CASES

📍 State : {states[idx]}

❤️ Active Cases : {active[idx]:,}
"""

# ================= AI QUESTIONS =================

if "what is covid" in question:

    response = """
🦠 COVID-19

COVID-19 ek infectious disease hai
jo coronavirus ki wajah se hoti hai.
"""

if "what is vaccination" in question:

    response = """
💉 Vaccination

Vaccination body ko virus se
bachane me help karta hai.
"""

if "what is active case" in question:

    response = """
❤️ Active Case

Active case matlab jo patient
abhi infected hai.
"""

# ================= SHOW ANSWER =================

if question != "":

   st.markdown(f"""
<div style='
background:#dff5e8;
padding:25px;
border-radius:20px;
margin-top:20px;
border:2px solid #00aa55;'>

<h2 style='color:#008844;'>
🤖 AI ANSWER
</h2>

<p style='
font-size:24px;
color:#006633;
line-height:2;'>

{response}

</p>

</div>
""", unsafe_allow_html=True)

# ================= REPORT =================

report = f"""
==============================
      INDIA COVID REPORT
==============================

QUESTION:
{question}

------------------------------

ANSWER:
{response}

------------------------------

Generated By:
Shivam Kumar

COVID-19 Analytics Dashboard
"""

# ================= DOWNLOAD BUTTON =================

st.download_button(
    label="📄 Download COVID Report",
    data=report,
    file_name="covid_report.txt",
    mime="text/plain"
)

