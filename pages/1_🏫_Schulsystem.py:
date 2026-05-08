import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Schulsystem", page_icon="🏫", layout="wide")
st.title("🏫 Schulsystem & Bildungsungleichheit")

st.markdown("""
> *"Du passt nicht aufs Gymnasium"* – Satz der Leben verändert.
> Nicht weil er wahr ist. Sondern weil Lehrer ihn sagen.
""")

# ── Daten ─────────────────────────────────────────────────────────────────────
bundeslaender = ['Bayern', 'NRW', 'Berlin', 'Hamburg', 'Sachsen', 
                 'BaWü', 'Hessen', 'Brandenburg', 'Bremen', 'Thüringen']

gym_ohne = [52, 48, 45, 44, 55, 53, 49, 42, 40, 43]
gym_mit  = [28, 25, 30, 32, 22, 27, 29, 20, 35, 21]

df_gym = pd.DataFrame({
    'Bundesland': bundeslaender,
    'Ohne Migrationshintergrund': gym_ohne,
    'Mit Migrationshintergrund': gym_mit
})

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Gymnasiumempfehlungen",
    "🧠 Stereotype Threat", 
    "🏫 Schulwechsel",
    "📈 PISA Vergleich"
])

with tab1:
    st.subheader("Gymnasiumempfehlungen nach Migrationshintergrund (%)")
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Ohne Migrationshintergrund',
        x=df_gym['Bundesland'],
        y=df_gym['Ohne Migrationshintergrund'],
        marker_color='steelblue'
    ))
    fig.add_trace(go.Bar(
        name='Mit Migrationshintergrund',
        x=df_gym['Bundesland'],
        y=df_gym['Mit Migrationshintergrund'],
        marker_color='tomato'
    ))
    fig.update_layout(
        barmode='group',
        title='Gymnasiumempfehlungen nach Bundesland & Migrationshintergrund',
        yaxis_title='% der Schüler mit Gymnasiumempfehlung',
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    **Was die Daten zeigen:**
    - Kinder mit Migrationshintergrund bekommen deutlich seltener Gymnasiumempfehlungen
    - Bei gleichen Noten: Effekt bleibt bestehen
    - Quelle: PISA, Destatis (simuliert aber realistisch)
    """)

with tab2:
    st.subheader("🧠 Stereotype Threat – Wenn Erwartungen Leistung beeinflussen")
    
    st.markdown("""
    **Was ist Stereotype Threat?** (Claude Steele, Stanford 1995)
    
    > Wenn du weißt dass jemand niedrige Erwartungen an dich hat –
    > verschlechtert sich deine Leistung. Selbst wenn du hochbegabt bist.
    
    **In Deutschland bedeutet das:**
    - Lehrer erwartet weniger → Kind leistet weniger
    - Nicht weil Kind weniger kann
    - Sondern weil Erwartung internalisiert wird
    """)
    
    gruppen = ['Akademikerkind\n(deutsch)', 'Arbeiterkind\n(deutsch)', 
               'Migrantenkind\n(2. Gen)', 'Migrantenkind\n(3. Gen)', 
               'Migrantenkind\n(Kopftuch)']
    erwartung_lehrer = [85, 65, 45, 40, 30]
    tatsaechliche_begabung = [85, 80, 80, 82, 85]
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        name='Lehrererwartung (%)',
        x=gruppen, y=erwartung_lehrer,
        marker_color='tomato'
    ))
    fig2.add_trace(go.Bar(
        name='Tatsächliche Begabung (geschätzt %)',
        x=gruppen, y=tatsaechliche_begabung,
        marker_color='steelblue'
    ))
    fig2.update_layout(
        barmode='group',
        title='Lehrererwartung vs. tatsächliche Begabung',
        yaxis_title='Prozent',
        height=400
    )
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("🏫 Schulwechsel als Lebensweg")
    
    st.markdown("""
    **Ein echter Lebensweg:**
    """)
    
    steps = [
        ("Grundschule", "Realschulempfehlung – obwohl Noten gut", "❌"),
        ("Realschule", "Erkämpft: Wechsel zum Gymnasium Klasse 6", "💪"),
        ("Gymnasium", "Zurück zur Realschule – Druck, Familie, System", "😔"),
        ("Realschule", "Abschluss mit 1,0 – Beste der Klasse", "⭐"),
        ("Gymnasium", "Wieder erkämpft – Klasse 10 EF bis Abitur", "💪"),
        ("Abitur", "2,1 – trotz massiver Familienprobleme", "🎓"),
        ("Pause", "4 Jahre – Familie, Überleben, Neuorientierung", "⏸️"),
        ("Uni", "Psychologiestudium – alleine, ohne Netz", "💙"),
    ]
    
    for schule, beschreibung, emoji in steps:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.markdown(f"**{schule}**")
        with col2:
            st.markdown(beschreibung)
        with col3:
            st.markdown(emoji)
        st.markdown("↓")
    
    st.markdown("""
    > *Wie viele Menschen mit dieser Geschichte gibt es?
    > Wie viele haben beim ersten "Nein" aufgehört?*
    """)

with tab4:
    st.subheader("📈 PISA Ergebnisse Deutschland nach Migrationshintergrund")
    
    kategorien = ['Lesen', 'Mathematik', 'Naturwissenschaften']
    ohne_migration = [500, 508, 505]
    erste_gen = [448, 455, 450]
    zweite_gen = [462, 468, 463]
    
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name='Ohne Migrationshintergrund', 
                          x=kategorien, y=ohne_migration, marker_color='steelblue'))
    fig3.add_trace(go.Bar(name='1. Generation', 
                          x=kategorien, y=erste_gen, marker_color='tomato'))
    fig3.add_trace(go.Bar(name='2. Generation', 
                          x=kategorien, y=zweite_gen, marker_color='orange'))
    fig3.update_layout(
        barmode='group',
        title='PISA Punkte nach Migrationshintergrund (Deutschland)',
        yaxis_title='PISA Punkte',
        height=400
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.warning("""
    **Wichtig:** Diese Lücke ist kein Intelligenzproblem.
    Sie ist ein **Systemproblem**:
    - Armut
    - Sprachbarrieren  
    - Stereotype Threat
    - Schlechtere Schulen in Brennpunkten
    - Weniger Förderung
    """)
