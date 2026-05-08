import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wissenschaft", page_icon="📚", layout="wide")
st.title("📚 Wissenschaft – Was existiert & was fehlt")

st.markdown("""
> *In den USA gibt es seit 50 Jahren Forschung zu Rassismustrauma.*
> *In Deutschland fehlt diese Sprache.*
> *Das Problem existiert trotzdem.*
""")

tab1, tab2, tab3 = st.tabs([
    "🇺🇸 Amerikanische Studien",
    "🇩🇪 Deutschland – Was fehlt",
    "📖 Ressourcen & Bücher"
])

with tab1:
    st.subheader("Wichtige Studien & Konzepte")
    
    studien = {
        'Konzept': ['Minority Stress Model', 'Race-Based Traumatic Stress',
                    'Stereotype Threat', 'Weathering Hypothesis',
                    'Intersectionality', 'Post-Traumatic Growth',
                    'Cultural Humility', 'Implicit Bias'],
        'Forscher:in': ['Meyer (2003)', 'Carter (2007)', 'Steele (1995)',
                        'Geronimus (1992)', 'Crenshaw (1989)',
                        'Tedeschi & Calhoun (1996)', 'Tervalon & Murray-García (1998)',
                        'Greenwald & Banaji (1995)'],
        'Bedeutung': [
            'Chronischer Stress durch Minderheitenstatus → Krankheit',
            'Rassismus verursacht echtes Trauma, keine Überempfindlichkeit',
            'Niedrige Erwartungen verschlechtern Leistung selbst bei Hochbegabten',
            'Chronischer Rassismus führt zu biologisch schnellerer Alterung',
            'Mehrere Diskriminierungsformen wirken zusammen',
            'Trauma kann stärken – aber nur mit Unterstützung',
            'Nicht "ich kenne deine Kultur" sondern "ich lerne von dir"',
            'Unbewusste Vorurteile existieren auch bei "nicht-rassistischen" Menschen'
        ],
        'Auf Deutsch anerkannt': ['⚠️ Kaum', '❌ Nein', '⚠️ Teilweise',
                                   '❌ Nein', '⚠️ Selten', '✅ Ja',
                                   '❌ Nein', '⚠️ Teilweise']
    }
    
    df_studien = pd.DataFrame(studien)
    st.dataframe(df_studien, use_container_width=True)

with tab2:
    st.subheader("🇩🇪 Was in Deutschland nicht erforscht wird")
    
    st.error("""
    ### Fehlende Forschung in Deutschland:
    
    - ❌ Systematische Daten zu Rassismuserfahrungen an Unis
    - ❌ Therapieerfolg nach ethnischer Zugehörigkeit
    - ❌ Racial Profiling Statistiken (offiziell)
    - ❌ Migrantenanteil in Prestigestudiengängen nach Uni
    - ❌ Generationstrauma bei Gastarbeiterkindern
    - ❌ Psychische Gesundheit von Kopftuchträgerinnen
    - ❌ Hochbegabung bei Migrantenkindern
    
    ### Warum ist das selbst ein Problem?
    > *Was nicht gemessen wird, existiert nicht.*
    > *Das Problem wird unsichtbar gemacht*
    > *indem man nicht hinschaut.*
    """)

with tab3:
    st.subheader("📖 Bücher & Ressourcen")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Auf Deutsch:**
        - 📗 Tupoka Ogette – *exit RACISM*
        - 📗 Noah Sow – *Deutschland Schwarz Weiß*
        - 📗 Emilia Roig – *Why We Matter*
        - 📗 Hadija Haruna-Oelker – *Die schönste Version*
        - 📗 Fatma Aydemir – *Ellbogen*
        """)
    
    with col2:
        st.markdown("""
        **Auf Englisch:**
        - 📘 Ibram X. Kendi – *How to be an Antiracist*
        - 📘 Reni Eddo-Lodge – *Why I'm No Longer Talking to White People About Race*
        - 📘 Joy DeGruy – *Post Traumatic Slave Syndrome*
        - 📘 Audre Lorde – *Sister Outsider*
        - 📘 bell hooks – *all about love*
        """)
    
    st.markdown("""
    **Anlaufstellen in Deutschland:**
    - 🏛️ Antidiskriminierungsstelle des Bundes
    - 🤝 CLAIM – Allianz gegen Islam- und Muslimfeindlichkeit  
    - 💙 Each One Teach One (EOTO)
    - 🧠 Psychenet – psychische Gesundheit mehrsprachig
    """)
