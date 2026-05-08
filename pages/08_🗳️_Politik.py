import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Politik", page_icon="🗳️", layout="wide")
st.title("🗳️ Politik, AfD & Repräsentation")

tab1, tab2, tab3 = st.tabs([
    "🗳️ AfD & Wahlergebnisse",
    "🏛️ Repräsentation",
    "⚖️ Gesetze & Schutz"
])

with tab1:
    st.subheader("AfD Wahlergebnisse & Migrantenanteil nach Bundesland")
    
    bundeslaender = ['Sachsen', 'Thüringen', 'Brandenburg', 'Sachsen-Anhalt',
                     'Mecklenburg-VP', 'Berlin', 'Bayern', 'NRW', 
                     'Hamburg', 'Bremen']
    afd_prozent = [32, 33, 29, 28, 25, 18, 15, 12, 11, 10]
    migrant_anteil = [8, 7, 10, 8, 9, 32, 28, 30, 35, 38]
    
    df_pol = pd.DataFrame({
        'Bundesland': bundeslaender,
        'AfD (%)': afd_prozent,
        'Migrantenanteil (%)': migrant_anteil
    })
    
    fig = px.scatter(df_pol, x='Migrantenanteil (%)', y='AfD (%)',
                     text='Bundesland', size='AfD (%)',
                     color='AfD (%)', color_continuous_scale='Reds',
                     title='AfD Stärke vs. Migrantenanteil – Wo wenige Migranten leben, ist AfD stärker')
    fig.update_traces(textposition='top center')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    **Was die Daten zeigen:**
    - Wo wenige Migranten leben → AfD am stärksten
    - Wo viele Migranten leben → AfD schwächer
    - Angst vor dem Unbekannten ist größer als Realität
    - Persönlicher Kontakt reduziert Vorurteile
    """)

with tab2:
    st.subheader("🏛️ Repräsentation – Wer spricht für wen?")
    
    institutionen = ['Bundestag', 'Professoren', 'Therapeuten',
                     'Richter', 'Chefredakteure', 'Ärzte (leitend)',
                     'Schulleiter']
    
    bevoelkerung = [27, 27, 27, 27, 27, 27, 27]
    repraesentation = [12, 5, 8, 4, 3, 15, 10]
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name='Bevölkerungsanteil mit Migrationshintergrund (%)',
                          x=institutionen, y=bevoelkerung, marker_color='steelblue'))
    fig2.add_trace(go.Bar(name='Tatsächliche Repräsentation (%)',
                          x=institutionen, y=repraesentation, marker_color='tomato'))
    fig2.update_layout(barmode='group', height=450,
                       title='Repräsentation vs. Bevölkerungsanteil (%)',
                       yaxis_title='Prozent')
    st.plotly_chart(fig2, use_container_width=True)
    
    st.error("""
    > *Das System wurde nicht für alle gebaut –
    > und das sieht man daran wer es leitet.*
    """)

with tab3:
    st.subheader("⚖️ AGG – Allgemeines Gleichbehandlungsgesetz")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Was das AGG schützt:**
        - Ethnische Herkunft
        - Religion
        - Geschlecht
        - Behinderung
        - Alter
        - Sexuelle Identität
        
        **Klagefrist:** Nur 2 Monate!
        """)
    
    with col2:
        st.markdown("""
        **Realität:**
        - ~3.500 AGG-Beschwerden/Jahr
        - Geschätzte Fälle: 350.000+
        - Wer klagt wirklich? <1%
        - Kosten eines Prozesses: 5.000-20.000€
        - Beweislast beim Opfer
        - Psychische Belastung
        """)
    
    kategorien = ['Diskriminierung\nerlebt', 'Kennen ihre\nRechte',
                  'Beschwerde\neingereicht', 'Klage\neingereicht',
                  'Klage\ngewonnen']
    werte = [100, 35, 8, 2, 0.8]
    
    fig3 = go.Figure(go.Funnel(
        y=kategorien, x=werte,
        marker_color='tomato'
    ))
    fig3.update_layout(height=400,
                       title='Von Diskriminierung zur Klage – Wie viele kämpfen wirklich?')
    st.plotly_chart(fig3, use_container_width=True)
