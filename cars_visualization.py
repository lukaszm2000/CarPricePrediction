import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data()
def load_data():
    df = pd.read_csv('final_cars.csv')
    return df

def main():

    st.title('Dashboard samochodowy')

    df = load_data()

    def format_number(x,decimals=0):
        return f"{x:.{decimals}f}" if pd.notnull(x) else ""
    

    def extract_brand(full_name):
        words = full_name.split()
        return words[0]    

    st.write('### Dane samochodow:')
    st.dataframe(df.style.format({
        'registered_year': lambda x: format_number(x, 0),
        'engine_capacity [cc]': lambda x: format_number(x, 0),
        'kms_driven': lambda x: format_number(x, 0),
        'max_power [hp]': lambda x: format_number(x, 0),
        'seats': lambda x: format_number(x, 0),
        'resale_price [USD]': lambda x: format_number(x, 0)
    }))

    df[['Brand','Model']] = df['full_name'].str.split(' ',expand=True)

    avg_brand_cost = df.groupby('Brand')['resale_price [USD]'].mean().reset_index().sort_values(by='resale_price [USD]',ascending=False)
    avg_brand_cost.columns = ['Marka','Sredni koszt (USD)']

    brand_count = df['Brand'].value_counts().reset_index()
    brand_count.columns = ['Marka','Ilosc']

    registration_count_per_year = df['registered_year'].value_counts().reset_index()
    registration_count_per_year.columns = ['Rok rejestracji samochodu','Ilosc']

    transmission_type_count = df['transmission_type'].value_counts().reset_index()
    transmission_type_count.columns = ['Rodzaj skrzyni','Ilosc']

    insurance_type = df['insurance'].value_counts().reset_index()
    insurance_type.columns = ['Ubezpieczenie','Ilosc']

    number_of_owner = df['owner_type'].value_counts().reset_index()
    number_of_owner.columns = ['Wlasciciel','Ilosc']

    fuel_type_count = df['fuel_type'].value_counts().reset_index()
    fuel_type_count.columns = ['Rodzaj paliwa/gazu','Ilosc']

    correlation_matrix = df.corr(numeric_only=True)

    df['Marka'] = df['full_name'].apply(extract_brand)

    df['wiek'] = 2024 - df['registered_year']

    brand_max_power_mean = df.groupby('Marka')['max_power [hp]'].mean().reset_index()
    brand_max_power_mean = brand_max_power_mean.sort_values(by='max_power [hp]',ascending=False)
    brand_max_power_mean.columns = ['Marka','Srednia moc silnika']

    body_type_count = df['body_type'].value_counts().reset_index()
    body_type_count.columns = ['Typ nadwozia','Ilosc']
    body_type_count.sort_values(by='Ilosc',ascending=False).reset_index()

    average_price_by_year = df.groupby('wiek')['resale_price [USD]'].mean().reset_index()
    average_price_by_year.columns = ['Wiek','Srednia cena [USD]']

    fig1 = px.bar(brand_count,x='Marka',y='Ilosc',title='Ilosc samochodow danej marki',color='Marka')
    fig2 = px.bar(avg_brand_cost,x='Marka',y='Sredni koszt (USD)',title='Sredni koszt za marke',color='Marka')
    fig3 = px.bar(average_price_by_year,x='Wiek',y='Srednia cena [USD]',title='Sredni koszt samochodu z danym wiekiem',color='Wiek')
    fig4 = px.bar(registration_count_per_year,x='Rok rejestracji samochodu',y='Ilosc',title = 'Ilosc rejestracji samochodow w danym roku',color = 'Rok rejestracji samochodu')
    fig5 = px.bar(transmission_type_count,x='Rodzaj skrzyni',y='Ilosc',title='Ilosc skrzyni biegu danego rodzaju',color='Rodzaj skrzyni')
    fig6 = px.bar(fuel_type_count,x='Rodzaj paliwa/gazu',y='Ilosc',title='Ilosc samochodow z danym paliwem/gazem',color='Rodzaj paliwa/gazu')
    fig7 = px.bar(brand_max_power_mean,x='Marka',y='Srednia moc silnika',color='Marka',title='Srednia moc silnika dla danej marki')
    fig8 = px.bar(body_type_count,x='Typ nadwozia',y='Ilosc',title='Ilosc samochodow z danym typem nadwozia',color='Typ nadwozia')
    fig9 = px.histogram(df,x='wiek',title='Rozklad wieku samochodow')
    fig10 = px.histogram(df,x='engine_capacity [cc]',title='Rozklad pojemnosci silnika',nbins=25)
    fig11 = px.box(df,x='Marka',y='kms_driven',title='Rozklad wartosci przebiegu wedlug marki',color='Marka')
    fig12 = px.pie(number_of_owner,values='Ilosc',names='Wlasciciel',title='Rozkład ilosci poprzednich właścicieli samochodów')
    fig13 = px.imshow(correlation_matrix,labels=dict(color='Korelacja'),x=correlation_matrix.columns, y=correlation_matrix.columns, color_continuous_scale='Viridis',title='Mapa korelacji czynnikow numerycznych')
    
    


    for i in range(len(correlation_matrix.columns)):
        for j in range(len(correlation_matrix.columns)):
            fig13.add_annotation(x=i, y=j, text=str(round(correlation_matrix.iloc[i, j], 2)),
                               showarrow=False, font=dict(color='white'))


    st.plotly_chart(fig1)
    st.write("Bazując na wykresie, widzimy iż topowymi markami pod względem sprzedaży są Maruti, Hyundai oraz Toyota.")

    st.plotly_chart(fig2)

    st.plotly_chart(fig3)
    st.write("Tutaj widoczny jest naturalny spadek ceny rynkowej aut wraz ze wzrostem wieku.")

    st.plotly_chart(fig4)

    st.plotly_chart(fig5)
    st.write("Zdecydowanie przeważają samochody z manualna skrzynią biegów.")

    st.plotly_chart(fig6)

    st.plotly_chart(fig7)
    st.write("Widzimy na podstawie wykresu, że bardziej luksusowe auta mają większą, średnią moc silnika.")

    st.plotly_chart(fig8)
    st.write("Najbardziej liczne auta to te z nadwoziem typu hatchback, sedan i SUV.")

    st.plotly_chart(fig9)

    st.plotly_chart(fig10)

    st.plotly_chart(fig11)
    st.write("Największe przebiegi uzyskują auta marki Toyota.")
    
    st.plotly_chart(fig12)

    st.plotly_chart(fig13)



if __name__ == '__main__':
    main()