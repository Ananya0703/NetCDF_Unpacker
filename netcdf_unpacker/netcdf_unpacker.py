import pandas as pd
import numpy as np
from netCDF4 import Dataset
from datetime import datetime, timedelta

class NetCDF_Unpacker:
    
    """
    A class for unpacking and analyzing data from NetCDF files.

    Parameters:
        path (str): The path to the NetCDF file.
    
    """
    def __init__(self, path: str):
        """
        Initialize a nc_unpack object with the specified NetCDF file path.

        Args:
            path (str): The path to the NetCDF file.
        """
        self.path = path

    def info(self):

        """
        Display information about the available variables in the NetCDF file.

        Allows the user to select a variable for further inspection.

        Usage:
        1. Create an nc_unpack object with the NetCDF file path.
        2. Call this method to display variable information interactively.

        """
        try:
            data = Dataset(self.path, 'r')
            variable_names = list(data.variables.keys())

            while True:
                print("Available variables:")
                for idx, variable in enumerate(variable_names):
                    print(f"'{variable}' at index {idx}")

                variable_index = input("Enter the index of the variable you want information for (or 'q' to quit): ")

                if variable_index.lower() == 'q':
                    break  # Exit the loop if the user enters 'q'

                try:
                    variable_index = int(variable_index)
                    if 0 <= variable_index < len(variable_names):
                        selected_variable = variable_names[variable_index]
                        variable_info = data.variables[selected_variable]
                        print(f"Variable: '{selected_variable}'")
                        print(f"Shape: {variable_info.shape}")
                        print(f"Attributes: {variable_info}")
                    else:
                        print("Invalid variable index. Please enter a valid index.")
                except ValueError:
                    print("Invalid input. Please enter a valid index or 'q' to quit.")

        except Exception as e:
            print(f"An error occurred while opening the file: {str(e)}")
            return None

    def unpack(self, lat_location: int, lon_location: int, variable_index: int, time_variable: str):

        """
        Extract and unpack data from the NetCDF file for a specific location and variable.

        Args:
            lat_location (int): Latitude location.
            lon_location (int): Longitude location.
            variable_index (int): Index of the variable to unpack.
            time_variable (str): The name of the time component in the NetCDF file. Example: 'time' or 'day'

        Returns:
            pd.DataFrame or None: A Pandas DataFrame containing the extracted data or None in case of an error.

        Usage:
        1. Create an nc_unpack object with the NetCDF file path.
        2. Call this method to extract data for a specific location and variable.
        """
        try:
            data = Dataset(self.path, 'r')
        except Exception as e:
            print(f"An error occurred while opening the file: {str(e)}")
            return None

        try:
            variable_name = list(data.variables.keys())[variable_index]
        except IndexError:
            print(f"Invalid variable index: {variable_index}")
            return None

        if time_variable not in data.variables:
            print(f"Time component '{time_variable}' not found in the file.")
            return None

        lat = data.variables['lat'][:]
        lon = data.variables['lon'][:]

        sq_diff_lat = (lat - lat_location) ** 2
        sq_diff_lon = (lon - lon_location) ** 2

        min_index_lat = sq_diff_lat.argmin()
        min_index_lon = sq_diff_lon.argmin()

        feature = data.variables[variable_name]

        date_str = data.variables[time_variable].units[11:]
        date_format = "%Y-%m-%d %H:%M:%S"

        date_obj = datetime.strptime(date_str, date_format)
        formatted_date = date_obj.strftime("%Y-%m-%d")

        days = data.variables[time_variable]
        start_date = datetime(1900, 1, 1)
        dates = [start_date + timedelta(days=int(day)) for day in days]

        df = pd.DataFrame(columns=['Date', variable_name])
        df['Date'] = dates

        dt = np.arange(0, data.variables[time_variable].size)

        for time_index in dt:
            feature_values = feature[time_index, min_index_lat, min_index_lon]
            df.at[time_index, variable_name] = feature_values

        return df
    



