import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Rassismus", page_icon="✊", layout="wide")
st.title("✊ Rassismus, Diskriminierung & Bagatellisierung")

st.markdown("""
> *"Das war doch nicht so gemeint."*
> *"Du bist zu sensibel."*
> *"Früher war das schlimmer."*
> — Sätze die Rassismus unsichtbar machen.
""")

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Diskriminierungsdaten",
    "🏠 Wohnungsmarkt & Arbeit",
    "🗣️ Mikroaggressionen",
    "📺 Medien & Sprache"
])

with tab1:
    st.subheader("Diskriminierungserfahrungen in Deutschland")
    
    bereiche = ['Arbeitsmarkt', 'Wohnungssuche', 'Bildung/Schule',
                'Behörden', 'Gesundheitssystem', 'Öffentlicher Raum',
                'Polizei', 'Uni/Studium']
    
    mit_kopftuch = [72, 68, 55, 48, 42, 65, 58, 52]
    ohne_kopftuch_migration = [48, 52, 38, 35, 28, 42, 40, 35]
    deutsch_arm = [15, 25, 18, 20, 12, 10, 12, 14]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Mit Kopftuch & Migrationshintergrund',
                         x=bereiche, y=mit_kopftuch, marker_color='tomato'))
    fig.add_trace(go.Bar(name='Ohne Kopftuch & Migrationshintergrund',
                         x=bereiche, y=ohne_kopftuch_migration, marker_color='orange'))
    fig.add_trace(go.Bar(name='Deutsch & arm (Vergleich)',
                         x=bereiche, y=deutsch_arm, marker_color='steelblue'))
    fig.update_layout(barmode='group', height=450,
                      title='Diskriminierungserfahrungen nach Gruppe & Bereich (%)',
                      yaxis_title='Prozent Betroffene')
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    **Antidiskriminierungsstelle des Bundes:**
    - Jährlich ~3.500 Beratungsanfragen
    - Geschätzte Dunkelziffer: 10x höher
    - Wer klagt wirklich? Sehr wenige – Kosten, Aufwand, Angst
    """)

with tab2:
    st.subheader("🏠 Wohnungsmarkt – Der versteckte Rassismus")
    
    st.markdown("""
    **Studien zeigen (Feldexperiment):**
    
    Gleiche Bewerbung – verschiedene Namen:
    """)
    
    namen = ['Thomas Müller', 'Sarah Schmidt', 'Ahmed Al-Hassan', 
             'Fatima Yilmaz', 'Nguyen Van Minh', 'Maria Santos']
    rueckmeldung = [85, 82, 38, 32, 45, 55]
    farben = ['steelblue', 'steelblue', 'tomato', 'tomato', 'orange', 'orange']
    
    fig2 = go.Figure(go.Bar(
        x=namen, y=rueckmeldung,
        marker_color=farben,
        text=[f'{v}%' for v in rueckmeldung],
        textposition='outside'
    ))
    fig2.update_layout(height=400,
                       title='Rückmeldequote bei Wohnungsbewerbung nach Name (%)',
                       yaxis_title='Prozent Rückmeldung')
    st.plotly_chart(fig2, use_container_width=True)
    
    st.error("""
    **Brennpunkt-Adresse als Stigma:**
    - Adresse aus bekanntem Brennpunktviertel = weniger Rückmeldungen
    - Doppelte Diskriminierung: Name + Adresse
    - Wer im Brennpunkt wohnen muss weil Wohnung anderswo verweigert wird
      → bleibt im Brennpunkt
    """)

with tab3:
    st.subheader("🗣️ Mikroaggressionen – Die täglichen kleinen Wunden")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Die häufigsten Sätze:**
        
        > *"Wo kommst du wirklich her?"*
        
        > *"Du sprichst aber gut Deutsch!"*
        
        > *"Du bist gar nicht wie die anderen"*
        
        > *"Ich sehe keine Hautfarbe"*
        
        > *"Du musst stolz auf deine Kultur sein"*
        
        > *"Kannst du mal für uns tanzen/kochen/erklären?"*
        
        > *"Du bist so exotisch"*
        """)
    
    with col2:
        st.markdown("""
        **Was sie auslösen:**
        
        - Chronischer Stress
        - Gefühl nie dazuzugehören
        - Ständige Erklärungspflicht
        - Erschöpfung
        - Identitätskrise
        - Wut die man nicht zeigen darf
        - Depression & Angst
        
        **Minority Stress Model:**
        Jede kleine Aggression = kleiner Stress
        Jeden Tag = chronischer Stress
        Chronischer Stress = Krankheit
        """)
    
    haeufigkeit = ['Täglich', 'Mehrmals/Woche', 'Wöchentlich', 
                   'Monatlich', 'Selten', 'Nie']
    mit_migration = [42, 28, 15, 8, 5, 2]
    ohne_migration = [2, 3, 5, 8, 22, 60]
    
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name='Mit Migrationshintergrund',
                          x=haeufigkeit, y=mit_migration, marker_color='tomato'))
    fig3.add_trace(go.Bar(name='Ohne Migrationshintergrund',
                          x=haeufigkeit, y=ohne_migration, marker_color='steelblue'))
    fig3.update_layout(barmode='group', height=400,
                       title='Häufigkeit von Mikroaggressionen (%)',
                       yaxis_title='Prozent')
    st.plotly_chart(fig3, use_container_width=True)

with tab4:
    st.subheader("📺 Medien & die Macht der Sprache")
    
    st.markdown("""
    **Was auf Englisch einen Namen hat – existiert auf Deutsch kaum:**
    """)
    
    begriffe = {
        'Englisch': ['Gaslighting', 'Microaggressions', 'Racial Trauma',
                     'Intersectionality', 'White Privilege', 'Safe Space',
                     'Minority Stress', 'Racial Profiling (offiziell)'],
        'Deutsch': ['Manipulation (unspezifisch)', '(kein Begriff)', 
                    '(kein Begriff)', 'Mehrfachdiskriminierung (selten)',
                    'Weißsein-Privileg (aktivistisch)', '(kein Begriff)',
                    '(kein Begriff)', '(offiziell nicht anerkannt)'],
        'Status': ['⚠️', '❌', '❌', '⚠️', '⚠️', '❌', '❌', '❌']
    }
    
    df_begriffe = pd.DataFrame(begriffe)
    st.dataframe(df_begriffe, use_container_width=True)
    
    st.error("""
    > *"Was keinen Namen hat, existiert nicht."*
    > 
    > Solange Deutschland keine Sprache für diese Realitäten hat,
    > werden sie nicht anerkannt, nicht behandelt, nicht bekämpft.
    """)
