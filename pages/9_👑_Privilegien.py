import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Privilegien", page_icon="👑", layout="wide")
st.title("👑 Privilegien, Vergleiche & die die auch kämpfen")

st.markdown("""
> *Privileg bedeutet nicht dass dein Leben leicht ist.
> Es bedeutet dass deine Hautfarbe, dein Name, dein Pass
> es nicht schwerer macht.*
""")

tab1, tab2, tab3 = st.tabs([
    "⚖️ Großer Vergleich",
    "🇩🇪 Deutsche die auch kämpfen",
    "🌍 Internationale vs. Hier-Geborene"
])

with tab1:
    st.subheader("Der große Vergleich – Wer hat welche Karten?")
    
    faktoren = ['Eltern helfen\nfinanziell', 'Netzwerk\nvorhanden',
                'Studiumswissen\nvon Eltern', 'Sprache\nkein Problem',
                'Name klingt\n"deutsch"', 'Wohnung\nleicht finden',
                'Therapie\nzugänglich', 'Vorbilder\nvorhanden',
                'BAföG\nWissen', 'Arbeit nach\nStudium']
    
    akademiker = [90, 88, 92, 95, 95, 85, 75, 90, 80, 85]
    arbeiterkind = [30, 35, 25, 90, 90, 65, 50, 55, 45, 60]
    migrant_brennpunkt = [10, 8, 5, 70, 20, 38, 25, 15, 20, 35]
    migrant_akademiker_aberkannt = [15, 10, 60, 65, 20, 35, 30, 20, 25, 30]
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=akademiker, theta=faktoren,
                                   fill='toself', name='Akademikerkind',
                                   line_color='steelblue'))
    fig.add_trace(go.Scatterpolar(r=arbeiterkind, theta=faktoren,
                                   fill='toself', name='Arbeiterkind (deutsch)',
                                   line_color='green'))
    fig.add_trace(go.Scatterpolar(r=migrant_brennpunkt, theta=faktoren,
                                   fill='toself', name='Migrantenkind Brennpunkt',
                                   line_color='tomato'))
    fig.add_trace(go.Scatterpolar(r=migrant_akademiker_aberkannt, theta=faktoren,
                                   fill='toself', name='Migrant-Akademiker (nicht anerkannt)',
                                   line_color='orange'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                      height=500, title='Privilege-Radar – Wer hat welche Ressourcen?')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🇩🇪 Deutsche die auch kämpfen – Wichtig & wahr")
    
    st.info("""
    **Diese App zeigt keine Opfer-Konkurrenz.**
    Armut, Trauma und Benachteiligung kennen keine Hautfarbe.
    Aber manche tragen zusätzliche Last.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Deutsche die auch kämpfen:**
        - 🏭 Ostdeutschland nach der Wende
        - 📉 Hartz IV Familien
        - 🧠 Eltern mit psychischen Erkrankungen
        - 🏘️ Ländliche Gebiete ohne Chancen
        - 👨‍👩‍👧 Alleinerziehende
        - 🔄 Generationsarmut
        """)
    
    with col2:
        st.markdown("""
        **Was sie NICHT zusätzlich haben:**
        - ✅ Name klingt deutsch
        - ✅ Keine Sprachbarriere
        - ✅ Aussehen kein Thema
        - ✅ Kein Racial Profiling
        - ✅ Abschlüsse anerkannt
        - ✅ Kein Kopftuch-Problem
        
        *Das ist kein Angriff – das sind Fakten.*
        """)
    
    gemeinsam = ['Finanzielle\nArmut', 'Kein\nNetzwerk',
                 'Schlechte\nSchulen', 'Psychische\nBelastung',
                 'Wenig\nVorbilder', 'Studiensystem\nunbekannt']
    deutsche_arm = [65, 55, 48, 52, 45, 50]
    migrant_arm = [72, 60, 55, 68, 72, 65]
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name='Deutsche aus armem Haushalt',
                          x=gemeinsam, y=deutsche_arm, marker_color='steelblue'))
    fig2.add_trace(go.Bar(name='Migrantenkind aus armem Haushalt',
                          x=gemeinsam, y=migrant_arm, marker_color='tomato'))
    fig2.update_layout(barmode='group', height=400,
                       title='Gemeinsame Probleme – aber nicht identische Last (%)',
                       yaxis_title='Prozent Betroffene')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("🌍 Internationale Studierende vs. Hier-Geborene")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **Internationale Studierende:**
        - ✅ Stipendien (DAAD, Erasmus)
        - ✅ Uni hilft bei Wohnung
        - ✅ Respekt weil "aus dem Ausland"
        - ✅ Exotisch & interessant
        - ✅ Professoren neugierig
        - ✅ Bereichert die Uni
        - ✅ Klarer Status
        """)
    
    with col2:
        st.error("""
        **3. Generation hier geboren:**
        - ❌ Kein Stipendium oft
        - ❌ Wohnungsdiskriminierung
        - ❌ Nicht deutsch genug
        - ❌ Nicht ausländisch genug
        - ❌ Unsichtbar oder bewertet
        - ❌ "Warum bist du noch nicht integriert?"
        - ❌ Kein klarer Status
        """)
    
    st.markdown("""
    > *Gleiche Religion. Gleicher Hijab. Anderer Pass.*
    > *Internationale wird bewundert.*
    > *Hier-Geborene wird bewertet.*
    > 
    > **Das sagt alles über das System.**
    """)
