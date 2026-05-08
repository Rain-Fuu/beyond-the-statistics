import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Zukunft", page_icon="🔭", layout="wide")
st.title("🔭 Perspektive & Zukunft")

st.markdown("""
> *Das System wurde nicht für alle gebaut.*
> *Aber wir bauen es um. Jeden Tag. Mit jeder Geschichte.*
> *Mit jeder Person die trotzdem aufsteht.* 💙
""")

tab1, tab2, tab3 = st.tabs([
    "🌱 Was sich ändern muss",
    "💪 Positive Beispiele",
    "💙 Warum diese App"
])

with tab1:
    st.subheader("Was strukturell geändert werden muss")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Bildung:**
        - Abschaffung der frühen Schulempfehlung
        - Kostenlose Nachhilfe für alle
        - Lehrer-Fortbildung zu Stereotype Threat
        - Diversität im Lehrpersonal
        - Hochbegabungsförderung unabhängig von Herkunft
        """)
    
    with col2:
        st.markdown("""
        **Gesundheit:**
        - Mehr kultursensible Therapeuten ausbilden
        - Mehrsprachige Therapie auf Kassenbasis
        - Rassismustrauma als Diagnose anerkennen
        - Echte JVA-Behandlung statt Alibi
        - Niedrigschwellige Angebote
        """)
    
    with col3:
        st.markdown("""
        **Politik & Gesellschaft:**
        - Daten systematisch erheben
        - AGG reformieren (längere Fristen!)
        - Racial Profiling anerkennen & abschaffen
        - Mehr Repräsentation in allen Bereichen
        - Sprache für die Realität entwickeln
        """)

with tab2:
    st.subheader("💪 Menschen die es trotzdem geschafft haben")
    
    st.markdown("""
    > *Diese Menschen haben es nicht geschafft weil das System fair war.*
    > *Sie haben es trotz des Systems geschafft.*
    """)
    
    beispiele = [
        ("🎓", "Erste Professorin mit Kopftuch", "Kämpfte 10 Jahre für ihre Stelle"),
        ("🧠", "Psychologin 3. Generation", "Hatte keine Vorbilder – wurde selbst eins"),
        ("⚖️", "Richterin mit Migrationshintergrund", "Alle sagten: nicht möglich"),
        ("🎵", "Rapper der über Trauma spricht", "Macht unsichtbares sichtbar"),
        ("📚", "Schriftstellerin aus Brennpunkt", "Schreibt was niemand schreiben wollte"),
    ]
    
    for emoji, titel, beschreibung in beispiele:
        st.markdown(f"**{emoji} {titel}**")
        st.caption(beschreibung)
        st.markdown("---")

with tab3:
    st.subheader("💙 Warum diese App existiert")
    
    st.markdown("""
    Diese App wurde gebaut weil:
    
    - 📊 Die Daten existieren nicht – also machen wir sie sichtbar
    - 🗣️ Die Sprache fehlt – also schaffen wir sie
    - 👁️ Die Geschichten werden nicht erzählt – also erzählen wir sie
    - 💙 Menschen sich alleine fühlen – also zeigen wir: du bist nicht alleine
    
    ---
    
    > *"Realschulempfehlung. Gymnasium erkämpft. Zurück. Wieder hoch.*
    > *Abi 2,1 trotz allem. 4 Jahre Pause. Psychologie. Alleine.*
    > *Ohne Netz. Ohne dass es jemand für möglich gehalten hat."*
    >
    > *Diese App ist für alle die diese Geschichte kennen.*
    > *Und für alle die sie verstehen wollen.* 💙
    
    ---
    """)
    
    st.info("""
    **Beyond the Statistics** bedeutet:
    Hinter jeder Zahl steckt ein Mensch.
    Hinter jedem Prozent steckt ein Leben.
    Hinter jeder Statistik steckt eine Geschichte
    die erzählt werden muss. 💙
    """)
    
    st.caption("Made with 💙 | Daten simuliert aber realistisch | "
               "Echte Daten werden in Deutschland kaum erhoben – das ist Teil des Problems")
