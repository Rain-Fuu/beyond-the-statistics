import streamlit as st

st.set_page_config(
    page_title="Beyond the Statistics",
    page_icon="💙",
    layout="wide"
)

st.title("💙 Beyond the Statistics")
st.subheader("Migrationserfahrungen in Deutschland – Die Geschichten hinter den Zahlen")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Was ist diese App?
    
    Diese App visualisiert Daten zu Themen die in Deutschland 
    kaum öffentlich diskutiert werden:
    
    - 🏫 Bildungsungleichheit & Schulsystem
    - 🎓 Uni-Zugang & Prestigestudiengänge  
    - 💔 Sozialer Aufstieg – vom Brennpunkt zum Professor
    - 💸 BAföG, Armut & finanzielle Realitäten
    - 🧠 Psychische Gesundheit & Therapiezugang
    - ✊ Rassismus & Diskriminierung
    - 🕌 Religion & Identität
    - 🗳️ Politik & Repräsentation
    - 👑 Privilegien & Vergleiche
    - 💪 Resilienz – die unsichtbare Stärke
    """)

with col2:
    st.markdown("""
    ### Warum diese App?
    
    > *"Was auf Englisch einen Namen hat, 
    > existiert auf Deutsch offiziell nicht."*
    
    In den USA gibt es seit Jahrzehnten Forschung zu:
    - Racial Trauma
    - Minority Stress
    - Institutional Discrimination
    
    In Deutschland fehlt diese Sprache.
    Diese App will eine Lücke füllen.
    
    ### ⚠️ Hinweis zu den Daten
    
    Viele Daten basieren auf realistischen Schätzungen,
    da Deutschland diese Daten oft **nicht systematisch erhebt**.
    Das ist selbst Teil des Problems.
    
    Quellen: Destatis, DZHW, OECD, 
    Antidiskriminierungsstelle des Bundes,
    Europäische Sozialerhebung
    """)

st.markdown("---")

st.markdown("""
### 💙 Eine echte Geschichte

> *"Realschulempfehlung. Obwohl ich mehr konnte. 
> Dann Gymnasium erkämpft. Dann zurück zur Realschule. 
> Realschulabschluss 1,0. Wieder Gymnasium. 
> Abitur 2,1 – trotz allem was zuhause passierte. 
> 4 Jahre Pause. Jetzt Psychologie. Alleine. 
> Ohne dass mir jemand erklärt hat wie das geht."*
>
> — Anonym, 3. Generation, Deutschland

Diese App ist für alle die sich in dieser Geschichte wiedererkennen.
Und für alle die sie noch nicht kennen.
""")

st.markdown("---")
st.caption("Made with 💙 | Daten: simuliert aber realistisch | Echte Daten werden in Deutschland kaum erhoben")
