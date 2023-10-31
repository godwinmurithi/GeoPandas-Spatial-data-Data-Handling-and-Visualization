#Import Libraries
import pandas as pd
import geopandas as gpd

#read population data
pop =pd.read_csv('/home/godwin/GeoPandas-Spatial-data-Data-Handling-and-Visualization/Part 2/2023_pop.csv')
pop

#read district data
districts = gpd.read_file("/home/godwin/GeoPandas-Spatial-data-Data-Handling-and-Visualization/Part 1/districtes.geojson")
districts

'''To perform an attribute join between the district data and the population, we must ensure that the district name column 
in both datasets contains identical values. In the districts dataset, the districts are currently represented by their respective 
codes. To align them with the population dataset, we'll convert these codes to district names. After this transformation, we can 
proceed with the merge operation based on the shared district name column.'''

#the following code views the district codes
districts.DISTRICTE

#rename the DISTRICTE Column to district_name

districts.rename(columns={'DISTRICTE': 'district_name'}, inplace=True)
districts.district_name

'''Now, we create a dictionary with the district code as the key and district name as the value and use it 
to map names to the codes in our new column.'''

#dictionary
district_mapping = {
    '01': 'Old City',
    '02': 'Eixample',
    '03': 'Sants-Montjuïc',
    '04': 'Les Corts',
    '05': 'Sarrià-Sant Gervasi',
    '06': 'Gràcia',
    '07': 'Horta-Guinardó',
    '08': 'Nou Barris',
    '09': 'Sant Andreu',
    '10': 'Sant Martí'
}

#replacing the codes with the names
districts['district_name'] = districts['district_name'].replace(district_mapping)

#view if district names 
districts.district_name

#merge the district data and the population data
pop = pd.DataFrame(pop.groupby('Nom_Districte')['Valor'].sum()).reset_index()
pop.columns=['district_name','population_22']
districts = districts.merge(pop)
districts
