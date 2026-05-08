import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Der Trichter", page_icon="💔", layout="wide")
st.title("💔 Vom Brennpunkt zum Professor – Die Wahrscheinlichkeiten")

st.markdown("""
> *Von 1000 Kindern aus dem Brennpunkt mit Migrationshintergrund 
> werden **0.3** Professor. Von 1000 Akademikerkindern: **47**.*
""")

# ── Trichter Daten ────────────────────────────────────────────────────────────
stufen = [
    'Geburt (1000 Kinder)',
    'Gymnasiumempfehlung',
    'Gymnasium abgeschlossen',
    'Abitur bestanden',
    'Studium begonnen',
    'Studium abgeschlossen',
    'Master/Promotion',
    'Wissenschaft/Forschung',
    'Professor'
]

akademiker_kind = [1000, 850, 800, 780, 650, 580, 120, 60, 47]
migrant_brennpunkt = [1000, 280, 200, 150, 80, 45, 8, 2, 0.3]
migrant_akademiker = [1000, 500, 420, 380, 280, 220, 45, 15, 8]
arbeiterkind_deutsch = [1000, 450, 380, 340, 250, 200, 35, 12, 6]

gruppe = st.selectbox("Gruppe auswählen:", [
    "Alle vergleichen",
    "Akademikerkind (deutsch)",
    "Migrantenkind aus Brennpunkt", 
    "Migrantenkind mit Akademikereltern",
    "Arbeiterkind (deutsch)"
])

fig = go.Figure()

if gruppe == "Alle vergleichen" or gruppe == "Akademikerkind (deutsch)":
    fig.add_trace(go.Funnel(
        name='Akademikerkind (deutsch)',
        y=stufen,
        x=akademiker_kind,
        marker_color='steelblue'
    ))

if gruppe == "Alle vergleichen" or gruppe == "Migrantenkind aus Brennpunkt":
    fig.add_trace(go.Funnel(
        name='Migrantenkind Brennpunkt',
        y=stufen,
        x=migrant_brennpunkt,
        marker_color='tomato'
    ))

if gruppe == "Alle vergleichen" or gruppe == "Migrantenkind mit Akademikereltern":
    fig.add_trace(go.Funnel(
        name='Migrantenkind Akademikereltern',
        y=stufen,
        x=migrant_akademiker,
        marker_color='orange'
    ))

if gruppe == "Alle vergleichen" or gruppe == "Arbeiterkind (deutsch)":
    fig.add_trace(go.Funnel(
        name='Arbeiterkind (deutsch)',
        y=stufen,
        x=arbeiterkind_deutsch,
        marker_color='green'
    ))

fig.update_layout(height=600, title='Bildungstrichter – Von 1000 Kindern')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Akademikerkind → Professor", "4.7%", "Referenz")
with col2:
    st.metric("Arbeiterkind → Professor", "0.6%", "-4.1%")
with col3:
    st.metric("Migrant + Akademikereltern → Prof", "0.8%", "-3.9%")
with col4:
    st.metric("Migrant + Brennpunkt → Professor", "0.03%", "-4.67%")

st.markdown("---")
st.markdown("""
### 💙 Was zwischen den Zahlen passiert

**Warum fallen Menschen raus?**

| Stufe | Hauptgrund Akademikerkind | Hauptgrund Migrantenkind Brennpunkt |
|---|---|---|
| Gymnasiumempfehlung | Fast alle bekommen sie | Lehrer empfehlen Hauptschule |
| Abitur | Nachhilfe wenn nötig | Nebenjobs statt Lernen |
| Studiumsbeginn | Eltern erklären wie es geht | Google & alleine |
| Studiumsabschluss | Eltern finanzieren | Nebenjob + Familie + Studium |
| Promotion | Netzwerk der Eltern | Kein Netzwerk, kein Mentor |
| Professur | Beziehungen & Empfehlungen | Fast unmöglich ohne Netz |

> *Das System ist nicht neutral. Es wurde für manche gebaut.*
""")
