import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Psychische Gesundheit", page_icon="🧠", layout="wide")
st.title("🧠 Psychische Gesundheit & Therapiezugang")

st.markdown("""
> *Durchschnittliche Wartezeit auf Therapieplatz: 6 Monate.
> Mit Sprachbarriere: länger. Mit Trauma: dringend nötig – trotzdem warten.*
""")

tab1, tab2, tab3, tab4 = st.tabs([
    "⏳ Wartezeiten & Zugang",
    "🏥 JVA & Behandlung", 
    "🤫 Tabu & Familie",
    "🧕🏽 Kulturelle Barrieren"
])

with tab1:
    st.subheader("Wer sucht Therapie – und wer bekommt sie?")
    
    gruppen = ['Akademikerkind\n(deutsch)', 'Arbeiterkind\n(deutsch)',
               'Migrantenkind', 'Geflüchtete', 'JVA Insassen']
    
    sucht_hilfe = [65, 45, 28, 15, 20]
    bekommt_hilfe = [58, 38, 20, 8, 5]
    wartezeit = [3, 5, 8, 12, 18]
    erfolg = [70, 45, 30, 15, 10]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Sucht Hilfe (%)', x=gruppen, 
                         y=sucht_hilfe, marker_color='steelblue'))
    fig.add_trace(go.Bar(name='Bekommt Hilfe (%)', x=gruppen, 
                         y=bekommt_hilfe, marker_color='tomato'))
    fig.update_layout(barmode='group', height=400,
                      title='Therapiezugang nach Gruppe',
                      yaxis_title='Prozent')
    st.plotly_chart(fig, use_container_width=True)
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name='Wartezeit (Monate)', x=gruppen,
                          y=wartezeit, marker_color='orange'))
    fig2.add_trace(go.Bar(name='Erfolgreiche Behandlung (%)', x=gruppen,
                          y=erfolg, marker_color='green'))
    fig2.update_layout(barmode='group', height=400,
                       title='Wartezeit & Behandlungserfolg',
                       yaxis_title='Monate / Prozent')
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("🔴 JVA – Geld kassiert, keine echte Behandlung")
    
    st.error("""
    ### Die JVA Realität:
    
    - 💰 Geld wird für "psychische Behandlung" im System verbucht
    - ❌ Echte Therapie findet kaum statt
    - ❌ Nach Entlassung: keine Weiterbehandlung
    - ❌ 50€ Überbrückungsgeld + keine Wohnung + keine Therapie
    - 🔄 Rückfallquote: über 50%
    - 👥 Migranten: überrepräsentiert
    """)
    
    kategorien = ['Bevölkerungsanteil\nmit Migrationshintergrund',
                  'JVA Insassen\nmit Migrationshintergrund',
                  'Ohne Therapieplatz\nnach Entlassung',
                  'Rückfall\ninnerhalb 3 Jahre']
    werte = [27, 45, 78, 52]
    farben = ['steelblue', 'tomato', 'tomato', 'tomato']
    
    fig3 = go.Figure(go.Bar(x=kategorien, y=werte, marker_color=farben))
    fig3.update_layout(height=400, title='JVA & Nachsorge – die Zahlen',
                       yaxis_title='Prozent')
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("""
    **Der Drehtür-Effekt:**
  Unbehandeltes Trauma
→ Kriminalität als Überlebensstrategie
→ JVA
→ Keine echte Behandlung
→ Entlassung ohne Netz
→ Rückfall
→ JVA
→ ...
  > *Das System verdient an kranken Menschen 
    > ohne sie zu heilen.*
    """)

with tab3:
    st.subheader("🤫 Das Tabu in Migrantenfamilien")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Was Familien sagen:**
        
        > *"Wir reden nicht über sowas"*
        
        > *"Schäm dich nicht vor den Leuten"*
        
        > *"Betest du genug?"*
        
        > *"In unserer Familie gibt es keine Depression"*
        
        > *"Du bist schwach"*
        
        > *"Das ist eine westliche Erfindung"*
        """)
    
    with col2:
        st.markdown("""
        **Was das bewirkt:**
        
        - Jahre unbehandelte psychische Erkrankungen
        - Selbstmedikation: Alkohol, Drogen
        - Körperliche Symptome statt psychische zugeben
        - Erst zum Arzt wenn es nicht mehr geht
        - Scham verhindert Heilung
        
        **Resultat:**
        - Chronische Erkrankungen
        - Spätere Diagnosen
        - Schwerere Verläufe
        """)
    
    symptome = ['Kopfschmerzen', 'Rückenschmerzen', 'Schlafprobleme',
                'Magenprobleme', 'Erschöpfung']
    psychisch_ursache = [65, 58, 72, 61, 78]
    
    fig4 = go.Figure(go.Bar(
        x=symptome, y=psychisch_ursache,
        marker_color='purple',
        text=[f'{v}%' for v in psychisch_ursache],
        textposition='outside'
    ))
    fig4.update_layout(height=350,
                       title='Körperliche Symptome mit psychischer Ursache bei Migranten (%)',
                       yaxis_title='Prozent')
    st.plotly_chart(fig4, use_container_width=True)

with tab4:
    st.subheader("🧕🏽 Wenn der Therapeut die Welt nicht versteht")
    
    st.markdown("""
    **Was Betroffene erleben:**
    
    | Was Therapeut sagt | Was gemeint ist | Was es auslöst |
    |---|---|---|
    | "Vielleicht hast du das falsch verstanden" | Rassismus anzweifeln | Gaslighting |
    | "Nicht alles ist Rassismus" | Bagatellisierung | Vertrauensverlust |
    | "Du musst dich mehr anpassen" | Täter-Opfer-Umkehr | Abbruch der Therapie |
    | "Deine Familie meint es doch gut" | Kulturunverständnis | Isolation |
    | Diagnose: "Anpassungsstörung" | Falsche Diagnose | Falsche Behandlung |
    """)
    
    st.error("""
    **Richtige Diagnose wäre:**
    - Rassismustrauma (Race-Based Traumatic Stress)
    - Minderheitenstress (Minority Stress)
    - Komplexe PTBS durch chronische Diskriminierung
    
    **Diese Diagnosen existieren auf Deutsch kaum.**
    """)
    
    therapeuten_data = {
        'Gruppe': ['Therapeuten gesamt', 'Mit Migrationshintergrund',
                   'Kultursensibel ausgebildet', 'Mehrsprachig', 
                   'Auf Kassenbasis verfügbar'],
        'Prozent': [100, 8, 12, 15, 3]
    }
    df_th = pd.DataFrame(therapeuten_data)
    
    fig5 = go.Figure(go.Bar(
        x=df_th['Gruppe'], y=df_th['Prozent'],
        marker_color=['steelblue', 'tomato', 'orange', 'orange', 'tomato'],
        text=[f'{v}%' for v in df_th['Prozent']],
        textposition='outside'
    ))
    fig5.update_layout(height=400,
                       title='Therapeuten in Deutschland – Wer kann wirklich helfen?',
                       yaxis_title='Prozent')
    st.plotly_chart(fig5, use_container_width=True)
