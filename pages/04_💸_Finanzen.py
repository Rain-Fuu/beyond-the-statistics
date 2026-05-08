import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Finanzen & BAföG", page_icon="💸", layout="wide")
st.title("💸 Finanzen, BAföG & die unsichtbare Armut")

st.markdown("""
> *BAföG Maximum: 934€. Durchschnittliche Miete Berlin: 850€. 
> Was bleibt für Essen, Bücher, Leben?*
""")

tab1, tab2, tab3 = st.tabs(["💶 BAföG Realität", "🏠 Miete vs. Einkommen", "💼 Nebenjobs"])

with tab1:
    st.subheader("BAföG – Wer bekommt es wirklich?")
    
    st.markdown("""
    **BAföG Maximum 2024: 934€/Monat**
    """)
    
    kategorien = ['Bekommen BAföG', 'Hätten Anspruch\naber beantragen nicht', 
                  'Kein Anspruch\n(Elterneinkommen)', 'Ausländische\nStudierende ohne Anspruch']
    
    ohne_migration = [28, 15, 45, 0]
    mit_migration = [22, 25, 30, 12]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Ohne Migrationshintergrund', 
                         x=kategorien, y=ohne_migration, marker_color='steelblue'))
    fig.add_trace(go.Bar(name='Mit Migrationshintergrund', 
                         x=kategorien, y=mit_migration, marker_color='tomato'))
    fig.update_layout(barmode='group', height=400, yaxis_title='Prozent der Studierenden',
                      title='BAföG-Situation nach Migrationshintergrund')
    st.plotly_chart(fig, use_container_width=True)
    
    st.warning("""
    **Warum beantragen viele BAföG nicht obwohl sie Anspruch haben?**
    - Niemand hat ihnen erklärt dass es BAföG gibt
    - Formulare zu kompliziert ohne Hilfe
    - Angst vor Behörden
    - Scham
    - Falsche Annahme: "Das ist nicht für uns"
    
    **Das ist Informationsarmut – nicht Faulheit.**
    """)

with tab2:
    st.subheader("🏠 Miete vs. Einkommen in Uni-Städten")
    
    staedte = ['München', 'Berlin', 'Hamburg', 'Frankfurt', 
               'Köln', 'Stuttgart', 'Düsseldorf', 'Leipzig']
    miete_wg = [750, 680, 650, 700, 600, 680, 630, 420]
    bafoeg_max = 934
    
    df_miete = pd.DataFrame({'Stadt': staedte, 'WG-Zimmer Miete (€)': miete_wg})
    df_miete['Verbleib nach Miete (€)'] = bafoeg_max - df_miete['WG-Zimmer Miete (€)']
    df_miete['Farbe'] = df_miete['Verbleib nach Miete (€)'].apply(
        lambda x: 'tomato' if x < 200 else ('orange' if x < 350 else 'green'))
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=df_miete['Stadt'], y=df_miete['WG-Zimmer Miete (€)'],
                          name='Miete WG-Zimmer', marker_color='tomato'))
    fig2.add_hline(y=bafoeg_max, line_dash="dash", line_color="green",
                   annotation_text="BAföG Maximum (934€)")
    fig2.update_layout(height=400, title='Miete vs BAföG Maximum',
                       yaxis_title='Euro pro Monat')
    st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("**München:** Nur 184€ für Essen, Bücher, Leben")
    with col2:
        st.error("**Berlin:** Nur 254€ für alles andere")
    
    st.markdown("""
    **Wer überbrückt die Lücke?**
    
    | Gruppe | Wie wird Lücke überbrückt? |
    |---|---|
    | Akademikerkind | Eltern zahlen einfach dazu |
    | Arbeiterkind | Nebenjob, Kredit |
    | Migrantenkind | Mehrere Nebenjobs, Verzicht |
    | Migrantenkind (Familie arm) | Wohnt zuhause, pendelt |
    """)

with tab3:
    st.subheader("💼 Nebenjobs & Studiendauer")
    
    gruppen = ['Akademikerkind', 'Arbeiterkind\n(deutsch)', 
               'Migrantenkind\nBrennpunkt', 'Migrantenkind\n+ Familie versorgen']
    
    stunden_job = [8, 15, 22, 30]
    regelstudienzeit = [100, 115, 135, 160]
    
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name='Wochenstunden Nebenjob',
                          x=gruppen, y=stunden_job, marker_color='orange'))
    fig3.update_layout(height=350, title='Wochenstunden Nebenjob nach Gruppe',
                       yaxis_title='Stunden pro Woche')
    st.plotly_chart(fig3, use_container_width=True)
    
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(name='Studiendauer (% der Regelstudienzeit)',
                          x=gruppen, y=regelstudienzeit, marker_color='steelblue'))
    fig4.add_hline(y=100, line_dash="dash", annotation_text="Regelstudienzeit")
    fig4.update_layout(height=350, title='Tatsächliche Studiendauer vs. Regelstudienzeit',
                       yaxis_title='% der Regelstudienzeit')
    st.plotly_chart(fig4, use_container_width=True)
    
    st.info("""
    **Was das bedeutet:**
    - Längere Studienzeit = weniger BAföG (läuft aus!)
    - Mehr Nebenjob = weniger Zeit zum Lernen
    - Weniger Lernen = schlechtere Noten
    - Schlechtere Noten = kein Stipendium
    - Kein Stipendium = mehr Nebenjob
    
    **Ein Kreislauf der schwer zu durchbrechen ist.**
    """)
