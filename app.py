import streamlit as st
from streamlit_folium import st_folium #(#pip install streamlit-folium)
import streamlit.components.v1 as components
 
import pandas as pd
import folium
 

st.set_page_config(page_title='Mapa', layout = 'wide', page_icon = 'Favicon.png', initial_sidebar_state = 'auto')


def create_map():
    # Carregar o arquivo CSV com as coordenadas
    df = pd.read_csv(r'enderecos_com_coordenadas_teste.csv', sep = ',')
    
    # Coordenadas de Encantado, RS
    latitude_encantado = -29.2361
    longitude_encantado = -51.8706
    
    # Inicializar o mapa centralizado em Encantado, RS
    mapa = folium.Map(location=[latitude_encantado, longitude_encantado], zoom_start=13)
    
    # Adicionar marcadores para cada endereço
    for index, row in df.iterrows():
        if not pd.isna(row['Latitude']) and not pd.isna(row['Longitude']):
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['endereco_completo']
            ).add_to(mapa)
    
    # Salvar o mapa como um arquivo HTML
    mapa.save('mapa_enderecos.html')
    
    return mapa


def main():


    tab_mapa, tab_contato = st.tabs(['Mapa', 'Contato'])


    with tab_mapa:
        col1, col2, col3 = st.columns(3)

        with col1:
            pass#st.slider('')
        with col2:
                    #Exibir o mapa no Streamlit 
            st.title('Mapa de Endereços')


            
            mapa = create_map()
            #st_folium(mapa)


            path_to_html = r"mapa_enderecos.html" 

            with open(path_to_html,'r', encoding='utf-8') as f: 
                html_data = f.read()

            # Show in webpage
            #st.header("Mapa de Endereços")
            st.components.v1.html(html_data, scrolling=True, height=700, width=1000)
            

            st.write('Um oferecimento Evcomx')
        with col3:
            pass #st.button('Start')

    with tab_contato:
        st.write('Informaçoes da Evcomx')
    return


if __name__ == '__main__':
    
    main()