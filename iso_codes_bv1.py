# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:15:54 2024

@author: BTB Data Solutions - Convert NER locations to country and
get iso code with lat long for plotting.
"""
import pandas as pd
import country_converter as coco


# Convert countrys to full contry name
def country_name(x):
    try:       
        standard_name = coco.convert(names=x, to='name_short')
        return standard_name
    except:
        return x
    
# get iso3 from country name
def get_iso3(x):
    try:
        iso3_code = coco.convert(names=x, to='ISO3')
        return iso3_code
    except:
        return x

# get lat from iso3 code
def get_lat(x):
    iso3_keys = ['AFG', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG', 'ATG', 
            'ARG', 'ARM', 'ABW', 'AUS', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BRB', 
            'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BIH', 'BIH', 'BWA', 
            'BVT', 'BRA', 'IOT', 'BRN', 'BGR', 'BFA', 'BDI', 'KHM', 'CMR', 'CAN',
            'CPV', 'CYM', 'CAF', 'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK', 'CCK', 
            'COL', 'COM', 'COG', 'COD', 'COK', 'CRI', 'CIV', 'HRV', 'CUB', 'CYP', 
            'CZE', 'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI',
            'EST', 'ETH', 'FLK', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF',
            'ATF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL', 'GRD', 
            'GLP', 'GUM', 'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'HMD', 'HMD', 
            'VAT', 'VAT', 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRN', 
            'IRQ', 'IRL', 'IMN', 'ISR', 'ITA', 'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 
            'KEN', 'KIR', 'PRK', 'KOR', 'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 
            'LBR', 'LBY', 'LIE', 'LTU', 'LUX', 'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 
            'MDV', 'MLI', 'MLT', 'MHL', 'MTQ', 'MRT', 'MUS', 'MYT', 'MEX', 'FSM', 
            'MDA', 'MCO', 'MNG', 'MNE', 'MSR', 'MAR', 'MOZ', 'MMR', 'NAM', 'NRU',
            'NPL', 'NLD', 'ANT', 'NCL', 'NZL', 'NIC', 'NER', 'NGA', 'NIU', 'NFK',
            'MNP', 'NOR', 'OMN', 'PAK', 'PLW', 'PSE', 'PAN', 'PNG', 'PRY', 'PER',
            'PHL', 'PCN', 'POL', 'PRT', 'PRI', 'QAT', 'REU', 'ROU', 'RUS', 'RWA',
            'SHN', 'SHN', 'SHN', 'KNA', 'KNA', 'LCA', 'SPM', 'SPM', 'VCT', 'VCT', 
            'WSM', 'SMR', 'SMR', 'STP', 'SAU', 'SEN', 'SRB', 'SYC', 'SLE', 'SGP',
            'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'SGS', 'SGS', 'SSD', 'ESP', 'LKA',
            'SDN', 'SUR', 'SJM', 'SJM', 'SWZ', 'SWE', 'CHE', 'SYR', 'TWN', 'TJK',
            'TZA', 'THA', 'TLS', 'TGO', 'TKL', 'TON', 'TTO', 'TTO', 'TUN', 'TUR', 
            'TKM', 'TCA', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR', 'USA', 'UMI', 
            'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'VIR', 'WLF', 'WLF', 'ESH', 
            'YEM', 'ZMB', 'ZWE']
    
    lat_values = [33.0, 41.0, 28.0, -14.3333, 42.5, -12.5, 18.25, -90.0, 17.05, 17.05,
                  -34.0, 40.0, 12.5, -27.0, 47.3333, 40.5, 24.25, 26.0, 24.0, 13.1667,
                  53.0, 50.8333, 17.25, 9.5, 32.3333, 27.5, -17.0, 44.0, 44.0, -22.0, 
                  -54.4333, -10.0, -6.0, 4.5, 43.0, 13.0, -3.5, 13.0, 6.0, 60.0, 16.0,
                  19.5, 7.0, 7.0, 15.0, -30.0, 35.0, -10.5, -12.5, -12.5, 4.0, -12.1667,
                  -1.0, 0.0, -21.2333, 10.0, 8.0, 45.1667, 21.5, 35.0, 49.75, 56.0, 11.5,
                  15.4167, 19.0, -2.0, 27.0, 13.8333, 2.0, 15.0, 59.0, 8.0, -51.75, -51.75,
                  62.0, -18.0, 64.0, 46.0, 4.0, -15.0, -43.0, -1.0, 13.4667, 42.0, 51.0, 8.0,
                  36.1833, 39.0, 72.0, 12.1167, 16.25, 13.4667, 15.5, 49.5, 11.0, 12.0, 5.0,
                  19.0, -53.1, -53.1, 41.9, 41.9, 15.0, 22.25, 47.0, 65.0, 20.0, -5.0, 32.0,
                  32.0, 33.0, 53.0, 54.23, 31.5, 42.8333, 18.25, 36.0, 49.21, 31.0, 48.0, 1.0,
                  1.4167, 40.0, 37.0, 29.3375, 41.0, 18.0, 57.0, 33.8333, -29.5, 6.5, 25.0,
                  47.1667, 56.0, 49.75, 22.1667, 41.8333, -20.0, -13.5, 2.5, 3.25, 17.0, 35.8333,
                  9.0, 14.6667, 20.0, -20.2833, -12.8333, 23.0, 6.9167, 47.0, 43.7333, 46.0, 42.0,
                  16.75, 32.0, -18.25, 22.0, -22.0, -0.5333, 28.0, 52.5, 12.25, -21.5, -41.0, 13.0,
                  16.0, 10.0, -19.0333, -29.0333, 15.2, 62.0, 21.0, 30.0, 7.5, 32.0, 9.0, -6.0,
                  -23.0, -10.0, 13.0, -24.7, 52.0, 39.5, 18.25, 25.5, -21.1, 46.0, 60.0, -2.0,
                  -15.9333, -15.9333, -15.9333, 17.3333, 17.3333, 13.8833, 46.8333, 46.8333,
                  13.25, 13.25, -13.5833, 43.7667, 43.7667, 1.0, 25.0, 14.0, 44.0, -4.5833,
                  8.5, 1.3667, 48.6667, 46.0, -8.0, 10.0, -29.0, -54.5, -54.5, 8.0, 40.0, 
                  7.0, 15.0, 4.0, 78.0, 78.0, -26.5, 62.0, 47.0, 35.0, 23.5, 39.0, -6.0, 15.0,
                  -8.55, 8.0, -9.0, -20.0, 11.0, 11.0, 34.0, 39.0, 40.0, 21.75, 21.75, -8.0, 
                  1.0, 49.0, 24.0, 54.0, 38.0, 19.2833, -33.0, 41.0, -16.0, 8.0, 16.0, 18.5,
                  18.3333, -13.3, -13.3, 24.5, 15.0, -15.0, -20.0]
    
    # make dict
    lat_dict = dict(zip(iso3_keys, lat_values))
    
    # parse value from key
    if lat_dict.get(x) is not None:
        value = lat_dict[x]
        return value       
    else:
        pass

 ########################################################### 
# get long from iso3 code
def get_long(x): 
    iso3_keys = ['AFG', 'ALB', 'DZA', 'ASM', 'AND', 'AGO', 'AIA', 'ATA', 'ATG', 'ATG', 
            'ARG', 'ARM', 'ABW', 'AUS', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BRB', 
            'BLR', 'BEL', 'BLZ', 'BEN', 'BMU', 'BTN', 'BOL', 'BIH', 'BIH', 'BWA', 
            'BVT', 'BRA', 'IOT', 'BRN', 'BGR', 'BFA', 'BDI', 'KHM', 'CMR', 'CAN',
            'CPV', 'CYM', 'CAF', 'CAF', 'TCD', 'CHL', 'CHN', 'CXR', 'CCK', 'CCK', 
            'COL', 'COM', 'COG', 'COD', 'COK', 'CRI', 'CIV', 'HRV', 'CUB', 'CYP', 
            'CZE', 'DNK', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI',
            'EST', 'ETH', 'FLK', 'FLK', 'FRO', 'FJI', 'FIN', 'FRA', 'GUF', 'PYF',
            'ATF', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GRL', 'GRD', 
            'GLP', 'GUM', 'GTM', 'GGY', 'GIN', 'GNB', 'GUY', 'HTI', 'HMD', 'HMD', 
            'VAT', 'VAT', 'HND', 'HKG', 'HUN', 'ISL', 'IND', 'IDN', 'IRN', 'IRN', 
            'IRQ', 'IRL', 'IMN', 'ISR', 'ITA', 'JAM', 'JPN', 'JEY', 'JOR', 'KAZ', 
            'KEN', 'KIR', 'PRK', 'KOR', 'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 
            'LBR', 'LBY', 'LIE', 'LTU', 'LUX', 'MAC', 'MKD', 'MDG', 'MWI', 'MYS', 
            'MDV', 'MLI', 'MLT', 'MHL', 'MTQ', 'MRT', 'MUS', 'MYT', 'MEX', 'FSM', 
            'MDA', 'MCO', 'MNG', 'MNE', 'MSR', 'MAR', 'MOZ', 'MMR', 'NAM', 'NRU',
            'NPL', 'NLD', 'ANT', 'NCL', 'NZL', 'NIC', 'NER', 'NGA', 'NIU', 'NFK',
            'MNP', 'NOR', 'OMN', 'PAK', 'PLW', 'PSE', 'PAN', 'PNG', 'PRY', 'PER',
            'PHL', 'PCN', 'POL', 'PRT', 'PRI', 'QAT', 'REU', 'ROU', 'RUS', 'RWA',
            'SHN', 'SHN', 'SHN', 'KNA', 'KNA', 'LCA', 'SPM', 'SPM', 'VCT', 'VCT', 
            'WSM', 'SMR', 'SMR', 'STP', 'SAU', 'SEN', 'SRB', 'SYC', 'SLE', 'SGP',
            'SVK', 'SVN', 'SLB', 'SOM', 'ZAF', 'SGS', 'SGS', 'SSD', 'ESP', 'LKA',
            'SDN', 'SUR', 'SJM', 'SJM', 'SWZ', 'SWE', 'CHE', 'SYR', 'TWN', 'TJK',
            'TZA', 'THA', 'TLS', 'TGO', 'TKL', 'TON', 'TTO', 'TTO', 'TUN', 'TUR', 
            'TKM', 'TCA', 'TCA', 'TUV', 'UGA', 'UKR', 'ARE', 'GBR', 'USA', 'UMI', 
            'URY', 'UZB', 'VUT', 'VEN', 'VNM', 'VGB', 'VIR', 'WLF', 'WLF', 'ESH', 
            'YEM', 'ZMB', 'ZWE']
    
    long_values = [65.0, 20.0, 3.0, -170.0, 1.6, 18.5, -63.1667, 0.0, -61.8, -61.8, -64.0,
            45.0, -69.9667, 133.0, 13.3333, 47.5, -76.0, 50.55, 90.0, -59.5333,
            28.0, 4.0, -88.75, 2.25, -64.75, 90.5, -65.0, 18.0, 18.0, 24.0, 3.4,
            -55.0, 71.5, 114.6667, 25.0, -2.0, 30.0, 105.0, 12.0, -95.0, -24.0,
            -80.5, 21.0, 21.0, 19.0, -71.0, 105.0, 105.6667, 96.8333, 96.8333, -72.0,
            44.25, 15.0, 25.0, -159.7667, -84.0, -5.0, 15.5, -80.0, 33.0, 15.5, 10.0,
            43.0, -61.3333, -70.6667, -77.5, 30.0, -88.9167, 10.0, 39.0, 26.0, 38.0,
            -59.0, -59.0, -7.0, 175.0, 26.0, 2.0, -53.0, -140.0, 67.0, 11.75, -16.5667,
            43.5, 9.0, -2.0, -5.3667, 22.0, -40.0, -61.6667, -61.5833, 144.7833, -90.25,
            -2.56, -10.0, -15.0, -59.0, -72.4167, 72.5167, 72.5167, 12.45, 12.45, -86.5,
            114.1667, 20.0, -18.0, 77.0, 120.0, 53.0, 53.0, 44.0, -8.0, -4.55, 34.75, 
            12.8333, -77.5, 138.0, -2.13, 36.0, 68.0, 38.0, 173.0, 127.0, 127.5, 47.6581,
            75.0, 105.0, 25.0, 35.8333, 28.5, -9.5, 17.0, 9.5333, 24.0, 6.1667, 113.55,
            22.0, 47.0, 34.0, 112.5, 73.0, -4.0, 14.5833, 168.0, -61.0, -12.0, 57.55,
            45.1667, -102.0, 158.25, 29.0, 7.4, 105.0, 19.0, -62.2, -5.0, 35.0, 98.0,
            17.0, 166.9167, 84.0, 5.75, -68.75, 165.5, 174.0, -85.0, 8.0, 8.0, -169.8667, 
            167.95, 145.75, 10.0, 57.0, 70.0, 134.5, 35.25, -80.0, 147.0, -58.0, -76.0,
            122.0, -127.4, 20.0, -8.0, -66.5, 51.25, 55.6, 25.0, 100.0, 30.0, -5.7, -5.7,
            -5.7, -62.75, -62.75, -61.1333, -56.3333, -56.3333, -61.2, -61.2, -172.3333,
            12.4167, 12.4167, 7.0, 45.0, -14.0, 21.0, 55.6667, -11.5, 103.8, 19.5, 15.0,
            159.0, 49.0, 24.0, -37.0, -37.0, 30.0, -4.0, 81.0, 30.0, -56.0, 20.0, 20.0,
            31.5, 15.0, 8.0, 38.0, 121.0, 71.0, 35.0, 100.0, 125.5167, 1.1667, -172.0, 
            -175.0, -61.0, -61.0, 9.0, 35.0, 60.0, -71.5833, -71.5833, 178.0, 32.0,
            32.0, 54.0, -2.0, -97.0, 166.6, -56.0, 64.0, 167.0, -66.0, 106.0, -64.5,
            -64.8333, -176.2, -176.2, -13.0, 48.0, 30.0, 30.0]
    
    # make dict
    long_dict = dict(zip(iso3_keys, long_values)) 
    # parse value from key
    if long_dict.get(x) is not None:
        value = long_dict[x]
        return value
    else:
       pass

    
# Convert State abbreviations and names to country statdard name.
def state_to_counrty(x):
    df = pd.read_csv(r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\iso_analytics\states.csv')
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
              'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
              'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
              'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
              'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
              'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
              'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
              'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 
              'Wisconsin', 'Wyoming', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 
                'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
                'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'PA',
                'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    if x in states:
        rslt = 'United States'
        return rslt
    else:
        return x


