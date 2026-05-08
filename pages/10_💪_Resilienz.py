import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Resilienz", page_icon="💪", layout="wide")
st.title("💪 Resilienz – Die unsichtbare Stärke")

st.markdown("""
> *Die stärksten Menschen sind nicht die die nie gefallen sind.*
> *Sie sind die die jedes Mal alleine wieder aufgestanden sind –*
> *ohne dass jemand zugeschaut hat.* 💙
""")

tab1, tab2, tab3 = st.tabs([
    "📊 Resilienz & Hindernisse",
    "💔 Der Preis der Stärke",
    "💙 Echte Geschichten"
])

with tab1:
    st.subheader("Je mehr Hindernisse – desto größer die Resilienz")
    
    gruppen = ['Akademikerkind', 'Arbeiterkind\n(deutsch)',
               'Migrantenkind\n2. Generation', 'Migrantenkind\nBrennpunkt',
               'Migrant+Kopftuch\n+Brennpunkt+alleine']
    
    hindernisse = [15, 35, 55, 75, 95]
    resilienz = [40, 55, 68, 80, 92]
    psychische_last = [20, 40, 58, 75, 88]
    burnout_risiko = [15, 35, 52, 70, 85]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hindernisse, y=resilienz,
                              mode='markers+text',
                              text=gruppen,
                              textposition='top center',
                              marker=dict(size=15, color=resilienz,
                                         colorscale='Viridis'),
                              name='Resilienz'))
    fig.update_layout(height=500,
                      title='Hindernisse vs. Resilienz – Je mehr Feuer, desto stärker',
                      xaxis_title='Anzahl Hindernisse (Index)',
                      yaxis_title='Resilienz-Score')
    st.plotly_chart(fig, use_container_width=True)
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(name='Resilienz', x=gruppen, 
                          y=resilienz, marker_color='green'))
    fig2.add_trace(go.Bar(name='Psychische Last', x=gruppen,
                          y=psychische_last, marker_color='tomato'))
    fig2.add_trace(go.Bar(name='Burnout-Risiko', x=gruppen,
                          y=burnout_risiko, marker_color='orange'))
    fig2.update_layout(barmode='group', height=400,
                       title='Resilienz hat einen Preis',
                       yaxis_title='Index (0-100)')
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("💔 Was nie anerkannt wird")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Akademikerkind lernt Resilienz durch:**
        - 📚 Bücher über Resilienz
        - 🧘 Resilienz-Coaching
        - 💰 Bezahlte Seminare
        - 🎤 TED Talks
        - 👨‍👩‍👧 Eltern die es erklären
        """)
    
    with col2:
        st.markdown("""
        **Migrantenkind hat echte Resilienz durch:**
        - 💔 Echten Schmerz
        - 🔄 Echte Niederlagen
        - 💪 Alleine aufstehen
        - 🌊 Jeden Sturm ohne Netz
        - 👁️ Ohne dass jemand zuschaut
        
        *Und wird dafür bestraft:*
        *"Zu emotional", "Zu kämpferisch"*
        """)
    
    st.error("""
    **Post-Traumatic Growth (Tedeschi & Calhoun):**
    Trauma kann zu Wachstum führen – ABER nur mit Unterstützung.
    Ohne Support = nur Trauma, kein Growth.
    
    **Weathering Hypothesis (Arline Geronimus):**
    Chronischer Stress durch Diskriminierung führt zu
    biologisch schnellerer Alterung.
    Stärke hat einen körperlichen Preis.
    """)

with tab3:
    st.subheader("💙 Echte Geschichten – Anonym")
    
    st.markdown("""
    > *"Realschulempfehlung. Obwohl ich mehr konnte.
    > Dann Gymnasium erkämpft. Dann zurück.
    > Realschulabschluss 1,0. Wieder Gymnasium.
    > Abitur 2,1 trotz allem was zuhause passierte.
    > 4 Jahre Pause. Jetzt Psychologie. Alleine.
    > Ohne dass mir jemand erklärt hat wie das geht."*
    >
    > — 3. Generation, Kopftuch, Deutschland 💙
    
    ---
    
    > *"Mein Vater war Ingenieur in seiner Heimat.
    > Hier fährt er Taxi. Sein Abschluss gilt nichts.
    > Ich studiere damit sein Opfer nicht umsonst war.
    > Das ist kein Traum – das ist Schuld und Liebe gleichzeitig."*
    >
    > — 2. Generation, Studentin 💙
    
    ---
    
    > *"Im Hörsaal bin ich die einzige mit Kopftuch.
    > Manchmal schauen alle.
    > Manchmal fragen sie ob ich wirklich hier studiere.
    > Ja. Ich studiere hier. Und ich werde besser sein
    > als ihre Erwartungen an mich."*
    >
    > — Psychologiestudentin, Deutschland 💙
    """)
    
    st.info("""
    **Möchtest du deine Geschichte teilen?**
    Anonym natürlich. Diese App lebt von echten Erfahrungen.
    Schreib an: [beyondthestatistics@proton.me]
    """)
