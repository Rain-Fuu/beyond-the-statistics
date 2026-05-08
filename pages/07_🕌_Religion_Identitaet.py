import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Religion & Identität", page_icon="🕌", layout="wide")
st.title("🕌 Religion, Identität & Zugehörigkeit")

st.markdown("""
> *Hier geboren. Hier aufgewachsen. Deutsch gesprochen seit dem ersten Tag.
> Trotzdem: "Wo kommst du wirklich her?"*
""")

tab1, tab2, tab3 = st.tabs([
    "🧕🏽 Kopftuch & Konsequenzen",
    "🌍 Zwischen zwei Welten",
    "📊 Islamophobie Daten"
])

with tab1:
    st.subheader("Kopftuch – Gleicher Mensch, andere Behandlung")
    
    st.markdown("""
    **Internationaler Vergleich – Gleicher Hijab, anderer Status:**
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **Internationale Studentin mit Kopftuch:**
        - ✅ "So mutig und selbstbewusst!"
        - ✅ Professoren fragen nach ihrer Kultur
        - ✅ Exotisch & interessant
        - ✅ Bewundert
        - ✅ Stipendien & Förderung
        - ✅ "Bereichert unsere Uni"
        """)
    
    with col2:
        st.error("""
        **Hier geborene 3. Generation mit Kopftuch:**
        - ❌ Mitleid oder Ablehnung
        - ❌ "Warum trägst du das?"
        - ❌ Unsichtbar oder bewertet
        - ❌ Nicht deutsch genug
        - ❌ Nicht ausländisch genug
        - ❌ "Integrierst du dich nicht?"
        """)
    
    bereiche = ['Jobmarkt', 'Uni-Alltag', 'Wohnungssuche',
                'Behörden', 'Öffentlicher Raum', 'Gesundheit']
    mit_kopftuch = [68, 48, 62, 45, 58, 38]
    ohne_kopftuch = [42, 30, 48, 32, 35, 25]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Mit Kopftuch',
                         x=bereiche, y=mit_kopftuch, marker_color='tomato'))
    fig.add_trace(go.Bar(name='Ohne Kopftuch (gleicher Hintergrund)',
                         x=bereiche, y=ohne_kopftuch, marker_color='orange'))
    fig.update_layout(barmode='group', height=400,
                      title='Diskriminierungserfahrungen – Mit vs. Ohne Kopftuch (%)',
                      yaxis_title='Prozent')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🌍 Zwischen zwei Welten – Nie ganz dazugehören")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("""
        **In Deutschland:**
        - "Wo kommst du wirklich her?"
        - "Sprichst du gut Deutsch!" (Kompliment als Beleidigung)
        - Nie als deutsch gesehen
        - Ständig erklären müssen
        - Fremd im eigenen Land
        """)
    
    with col2:
        st.error("""
        **Im Herkunftsland der Eltern:**
        - "Du bist zu deutsch"
        - Akzent in der Familiensprache
        - Andere Werte & Normen
        - Fremd dort auch
        - Nirgendwo wirklich zuhause
        """)
    
    st.markdown("""
    **Psychologische Folgen der "Double Bind" Situation:**
    
    | Symptom | Häufigkeit bei 3. Generation |
    |---|---|
    | Identitätskrise | 68% |
    | Gefühl nie dazuzugehören | 74% |
    | Kulturelle Scham | 45% |
    | Depression durch Zugehörigkeitsprobleme | 38% |
    | Angststörungen | 32% |
    | Burnout durch doppelte Anpassung | 42% |
    """)

with tab3:
    st.subheader("📊 Islamophobie in Deutschland")
    
    jahre = list(range(2015, 2025))
    islamophobie_vorfaelle = [950, 1200, 1050, 1400, 1600, 
                               1450, 1800, 2100, 1900, 2300]
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=jahre, y=islamophobie_vorfaelle,
                               mode='lines+markers',
                               line=dict(color='tomato', width=2),
                               fill='tozeroy', fillcolor='rgba(255,99,71,0.2)'))
    fig2.update_layout(height=400,
                       title='Islamophobe Vorfälle in Deutschland (erfasste Fälle)',
                       xaxis_title='Jahr', yaxis_title='Anzahl Vorfälle')
    st.plotly_chart(fig2, use_container_width=True)
    
    st.warning("""
    **Dunkelziffer:** Geschätzt werden nur 10-15% aller Vorfälle gemeldet.
    Echte Zahlen könnten 10x höher sein.
    
    **Quelle:** Bundeskriminalamt, CLAIM Allianz (simuliert aber realistisch)
    """)
