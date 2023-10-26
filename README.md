# NetCDF Unpacker
 
NetCDF Unpacker is a Python library designed to simplify the process of working with NetCDF files containing satellite weather data. With this library, you can easily explore the contents of NetCDF files and extract specific weather variables, making it convenient for data analysis and visualization. NetCDF files are commonly used for storing geospatial and time-series data, including atmospheric and climate data.
 
## Features
 
- **Variable Information:** Explore the available variables in NetCDF files, along with their shapes and attributes.
- **Variable Extraction:** Extract specific weather variables from the NetCDF file and create a pandas DataFrame for further analysis.
- **Geospatial Filtering:** Specify a location using latitude and longitude and extract data for that specific point.
- **Time Handling:** Utilize the time component in NetCDF files to create a time series in the DataFrame.
- **User-Friendly Interface:** A user-friendly command-line interface for selecting variables and setting extraction parameters.
 
## Installation
 
You can install NetCDF Unpacker using pip:
 
```bash
pip install netcdf-unpacker
```
 
## Usage
 
### 1. Initialize NetCDF Unpacker
 
```python
from netcdf-unpacker import NetCDF_Unpacker
 
# Provide the path to your NetCDF file
nc_unpacker = NetCDF_Unpacker("path_to_your_file.nc")
```
 
### 2. Explore Variable Information
 
```python
# Get information about the variables in the NetCDF file
nc_unpacker.info()
```
 
### 3. Extract Weather Variables
 
```python
# Extract weather variables for a specific location and time component
latitude = 40.0  # Your desired latitude
longitude = -75.0  # Your desired longitude
variable_index = 4  # Index of the variable to extract
time_variable = "time"  # The time component variable name
 
# Extract the data and get a DataFrame
weather_data = nc_unpacker.unpack(latitude, longitude, variable_index, time_variable)
```

 
### 4. Analyze and Visualize Data
 
With the extracted data in a DataFrame, you can now perform data analysis, visualization, and other operations using popular Python libraries such as pandas, matplotlib, and seaborn.
 
## Example
 
Here's a simple example of extracting and visualizing data from a NetCDF file:
 
```python
import matplotlib.pyplot as plt
 
# Extract temperature data
temperature_data = nc_unpacker.unpack(latitude, longitude, variable_index, time_variable)
 
# Plot the temperature time series
plt.figure(figsize=(12, 6))
plt.plot(temperature_data["Date"], temperature_data[variable_name])
plt.title(f"Temperature at Lat {latitude}, Lon {longitude}")
plt.xlabel("Date")
plt.ylabel(f"{variable_name}")
plt.grid(True)
plt.show()
```
 
## Support and Contributions
 
If you encounter any issues, have suggestions, or would like to contribute to this project, please visit the github repository or feel free to reach out to us via mail.

-Ananya Giliyal - giliyal.ananya@gmail.com

-Isha Paranjpe - ishaparanjpe.work@gmail.com

-Mansi Katgire - katgiremansi@gmail.com

-Atishay Gwari - atishay345@gmail.com
 
## License
 
This library is open-source and available under the [MIT License](LICENSE).
 
---
 
NetCDF Unpacker simplifies working with NetCDF files, making it easy to extract and analyze weather data. Give it a try and unlock the potential of your satellite weather data for research, analysis, and visualization.
 
