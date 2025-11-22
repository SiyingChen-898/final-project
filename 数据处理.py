# 1. 导入工具包
import pandas as pd

# 2. 读取数据
#wealth的象征——可用
GDP_per_capita_data = pd.read_csv("./data/share-of-population-urban.csv")
#人均CO2排放量——可用
co2_data = pd.read_csv("./data/人均二氧化碳排放量co2-emissions-per-capita.csv")
#人均能源消耗——可用
energy_data = pd.read_csv("./data/人均能源消耗energy-use-per-person.csv") 
#碳强度——可用
carbon_strength_data = pd.read_csv("./data/碳强度数据 1990到2024.csv")
share_of_population_urban_data = pd.read_csv("./data/share-of-population-urban.csv")
gdp_vs_agriculture_employment_data = pd.read_csv("./data/gdp-vs-agriculture-employment.csv")
gdp_vs_manufacturing_gdp_data = pd.read_csv("./data/gdp-vs-manufacturing-gdp.csv")
gdp_vs_services_employment_data = pd.read_csv("./data/gdp-vs-services-employment.csv")

# 3. 打印数据看一下
print("人均GDP数据前5行：")
print(GDP_per_capita_data.head())
print("\nCO2数据前5行:")
print(co2_data.head())
print("\n能源数据前5行:")
print(energy_data.head())
print("\n碳强度数据前5行")
print(carbon_strength_data.head())
print("\n城市人口占比前5行：")
print(share_of_population_urban_data.head())
print("\n农业产业结构占比前5行:")
print(gdp_vs_agriculture_employment_data.head())
print("\n工业产业结构占比前5行：")
print(gdp_vs_manufacturing_gdp_data.head())
print("\n服务业产业结构占比前5行：")
print(gdp_vs_services_employment_data.head())

# 4. 缺失值统计
print("人均GDP数据缺失情况：")
print(GDP_per_capita_data.isnull().sum())
print("\nCO2数据缺失情况:")
print(co2_data.isnull().sum())
print("\n能源数据缺失情况:")
print(energy_data.isnull().sum())
print("\n碳强度数据缺失情况")
print(carbon_strength_data.isnull().sum())
print("\n城市人口占比缺失情况：")
print(share_of_population_urban_data.isnull().sum())
print("\n农业产业结构占比缺失情况:")
print(gdp_vs_agriculture_employment_data.isnull().sum())
print("\n工业产业结构占比缺失情况：")
print(gdp_vs_manufacturing_gdp_data.isnull().sum())
print("\n服务业产业结构占比缺失情况：")
print(gdp_vs_services_employment_data.isnull().sum())

#5选择需要的列（简化处理）
simple_GDP = GDP_per_capita_data[['Entity', 'Code', 'Year', 'Urban population (% of total population)']
]
simple_energy = energy_data[['Entity', 'Year', 'Primary energy consumption per capita (kWh/person)']]
simple_carbon_strength = carbon_strength_data[['Country', 'Year', 'CO2_per_capita', 'GDP_per_capita', 'Carbon_Intensity']]

# 6合并数据
merged_data_GDP_energy = pd.merge(simple_GDP, simple_energy, on=['Entity', 'Year'], how='inner')
merged_data_GDP_co2 = pd.merge(simple_GDP, simple_carbon_strength, left_on=['Entity', 'Year'], right_on=['Country', 'Year'], how='inner')
merged_data_energy_co2 = pd.merge(simple_energy, simple_carbon_strength, left_on=['Entity', 'Year'], right_on=['Country', 'Year'], how='inner')

#7过滤时间范围
filtered_data_GDP_energy = merged_data_GDP_energy[(merged_data_GDP_energy['Year'] >= 1990) & (merged_data_GDP_energy['Year'] <= 2020)]
filtered_data_GDP_co2 = merged_data_GDP_co2[(merged_data_GDP_co2['Year'] >= 1990) & (merged_data_GDP_co2['Year'] <= 2020)]
filtered_data_energy_co2 = merged_data_energy_co2[(merged_data_energy_co2['Year'] >= 1990) & (merged_data_energy_co2['Year'] <= 2020)]

# 8处理缺失值 - 简单方法：删除有缺失的行
clean_data_GDP_energy = filtered_data_GDP_energy.dropna()
clean_data_GDP_co2 = filtered_data_GDP_co2.dropna()
clean_data_energy_co2 = filtered_data_energy_co2.dropna()

print("清洗后数据形状:", clean_data_GDP_energy.shape)
clean_data_GDP_energy.to_csv("./data/cleaned_data_GDP_energy.csv", index=False)

print("清洗后数据形状:", clean_data_GDP_co2.shape)
clean_data_GDP_co2.to_csv("./data/cleaned_data_GDP_co2.csv", index=False)

print("清洗后数据形状:", clean_data_energy_co2.shape)
clean_data_energy_co2.to_csv("./data/cleaned_data_energy_co2.csv", index=False)



