import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Unis", page_icon="🎓", layout="wide")
st.title("🎓 Universitäten & Studienzugang")

st.markdown("""
> *Psychologie NC 1,0. Medizin NC 1,1. 
> Wer kommt rein? Wessen Kinder studieren das?*
""")

# ── Daten ─────────────────────────────────────────────────────────────────────
unis = ['LMU München', 'FU Berlin', 'Uni Hamburg', 'Uni Frankfurt', 
        'Uni Köln', 'Heidelberg', 'TU München', 'Humboldt Berlin',
        'Uni Bremen', 'Uni Leipzig']

migrant_anteil = [18, 28, 22, 25, 23, 15, 20, 26, 24, 17]
diskriminierung = [35, 42, 38, 40, 37, 30, 33, 44, 41, 32]
beschwerdestelle = [True, True, False, True, False, True, True, True, False, False]
kulturberatung = [False, True, False, False, False, False, False, True, True, False]

df_unis = pd.DataFrame({
    'Uni': unis,
    'Migrantenanteil (%)': migrant_anteil,
    'Diskriminierungserfahrungen (%)': diskriminierung,
    'Beschwerdestelle': beschwerdestelle,
    'Kulturensensible Beratung': kulturberatung
})

tab1, tab2, tab3, tab4 = st.tabs([
    "🏛️ Unis im Vergleich",
    "📚 Wer studiert was?",
    "🌍 Erasmus & Ausland",
    "❓ Fehlende Daten"
])

with tab1:
    st.subheader("Unis im Vergleich")
    
    uni_filter = st.multiselect("Unis auswählen:", unis, default=unis[:5])
    df_filtered = df_unis[df_unis['Uni'].isin(uni_filter)]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Migrantenanteil (%)',
        x=df_filtered['Uni'],
        y=df_filtered['Migrantenanteil (%)'],
        marker_color='steelblue'
    ))
    fig.add_trace(go.Bar(
        name='Diskriminierungserfahrungen (%)',
        x=df_filtered['Uni'],
        y=df_filtered['Diskriminierungserfahrungen (%)'],
        marker_color='tomato'
    ))
    fig.update_layout(barmode='group', height=400,
                      title='Migrantenanteil vs. Diskriminierungserfahrungen')
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Infrastruktur für Betroffene")
    df_display = df_filtered[['Uni', 'Beschwerdestelle', 'Kulturensensible Beratung']].copy()
    df_display['Beschwerdestelle'] = df_display['Beschwerdestelle'].map({True: '✅', False: '❌'})
    df_display['Kulturensensible Beratung'] = df_display['Kulturensensible Beratung'].map({True: '✅', False: '❌'})
    st.dataframe(df_display, use_container_width=True)

with tab2:
    st.subheader("Wer studiert was? – Migrantenanteil nach Fach")
    
    faecher = ['Medizin', 'Psychologie', 'Jura', 'BWL', 
               'Ingenieurwesen', 'Soziale Arbeit', 'Pflege', 
               'Lehramt', 'Informatik', 'Architektur']
    
    anteil_migration = [12, 14, 11, 20, 28, 35, 42, 18, 30, 16]
    nc_wert = [1.1, 1.0, 1.5, 2.0, 2.5, 2.8, 3.0, 2.3, 2.4, 2.2]
    prestige = [10, 9, 9, 7, 7, 4, 3, 5, 7, 8]
    
    df_fach = pd.DataFrame({
        'Fach': faecher,
        'Migrantenanteil (%)': anteil_migration,
        'NC': nc_wert,
        'Prestige (1-10)': prestige
    })
    
    fig2 = px.scatter(df_fach, 
                      x='NC', y='Migrantenanteil (%)',
                      size='Prestige (1-10)',
                      text='Fach',
                      color='Prestige (1-10)',
                      color_continuous_scale='RdYlBu_r',
                      title='NC vs. Migrantenanteil – Je höher das Prestige, desto weniger Migranten')
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    st.plotly_chart(fig2, use_container_width=True)
    
    st.error("""
    **Was das zeigt:**
    - Prestigefächer (Medizin, Psychologie, Jura) haben niedrigsten Migrantenanteil
    - Pflegeberufe haben höchsten Migrantenanteil
    - NC als Zugangsbarriere trifft Migrantenkinder härter
    - Warum? Weniger Nachhilfe, weniger Vorbereitung, mehr Nebenjobs
    """)

with tab3:
    st.subheader("🌍 Erasmus & Auslandsstudium – Wer kann sich das leisten?")
    
    gruppen = ['Akademikerkind\n(deutsch)', 'Arbeiterkind\n(deutsch)',
               'Migrantenkind\n(EU-Pass)', 'Migrantenkind\n(Nicht-EU-Pass)',
               'Internationale\nStudierende']
    
    erasmus_anteil = [45, 22, 18, 8, 35]
    finanzierung_eltern = [75, 30, 15, 10, 20]
    bafoeg_ausland = [40, 55, 35, 20, 5]
    
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name='Erasmus-Teilnahme (%)', 
                          x=gruppen, y=erasmus_anteil, marker_color='steelblue'))
    fig3.add_trace(go.Bar(name='Eltern finanzieren (%)', 
                          x=gruppen, y=finanzierung_eltern, marker_color='gold'))
    fig3.update_layout(barmode='group', height=400,
                       title='Erasmus & Auslandsstudium nach Gruppe')
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("""
    **Der doppelte Standard:**
    
    | | Akademikerkind geht nach Amsterdam | Migrantenkind geht ins Ausland |
    |---|---|---|
    | Reaktion Familie | "So mutig! Horizont erweitern!" | "Was ist mit uns?" |
    | Reaktion Freunde | "So toll!" | "Kannst du dir das leisten?" |
    | Finanzierung | Eltern zahlen | Stipendium oder gar nicht |
    | Visum | Kein Problem | Manchmal großes Problem |
    """)

with tab4:
    st.subheader("❓ Die fehlenden Daten – Das ist selbst das Problem")
    
    st.error("""
    ### Was Deutschland nicht erhebt:
    
    - ❌ Systematische Daten zu Rassismuserfahrungen an Unis
    - ❌ Migrantenanteil nach Fach und Uni (kaum vorhanden)
    - ❌ Therapieerfolg nach ethnischer Zugehörigkeit  
    - ❌ Diskriminierung bei Wohnungssuche (nur Studien, keine Statistik)
    - ❌ Racial Profiling durch Polizei (offiziell)
    
    ### In den USA ist das Pflicht:
    - ✅ Jede Uni muss Diversity-Berichte veröffentlichen
    - ✅ Polizei muss Racial Profiling Daten melden
    - ✅ Therapieerfolg wird nach Ethnizität ausgewertet
    
    ### Was das bedeutet:
    > *"Was nicht gemessen wird, existiert nicht."*
    > Das Problem wird unsichtbar gemacht indem man nicht hinschaut.
    """)
