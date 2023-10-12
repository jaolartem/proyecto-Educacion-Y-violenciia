import os
import glob
from excel_to_csv import load_excel_to_dict
from csv_to_df import load_csv_to_dict

# Define the global dictionary
ALL_DFS = {}

class Extract:
    """
    Class responsible for data extraction.
    """
    def __init__(self):
        self.converted_files = []

    def from_excel(self, path):
        """
        Extracts data from Excel and converts it to DataFrames stored in ALL_DFS.
        
        Args:
        - path (str): Path to the Excel file or directory containing multiple Excel files.
        """
        global ALL_DFS
        
        try:
            
            dfs_dict = load_excel_to_dict(path)
            ALL_DFS.update(dfs_dict)

        except Exception as e:
            print(f"Error in extraction process. Error: {e}")
            
    def from_csv(self, csv_path): 
        """
        Extracts data from CSVs and loads them into DataFrames stored in ALL_DFS.
        
        Args:
        - csv_path (str): Path to the CSV file or directory containing multiple CSV files.
        """
        global ALL_DFS
        try:
            loaded_data = load_csv_to_dict(csv_path)
            ALL_DFS.update(loaded_data)
        except Exception as e:
            print(f"Error in extraction process. Error: {e}")
        

class Transformation:
    """
    Class responsible for data transformation.
    """

    def transform_and_save(self, sheet_name, dataframe):
        """
        Logic to transform and save the dataframe.
        Can be extended in the future for more complex transformations.
        
        Args:
        - sheet_name (str): Name of the DataFrame/sheet.
        - dataframe (pd.DataFrame): DataFrame to be transformed.
        
        Returns:
        - pd.DataFrame: Transformed DataFrame.
        """
        # Current logic is a placeholder. Actual transformation logic should replace this.
        return dataframe

    def Violence_pivot(self):
        """
        Transforms DataFrames that match certain conditions.
        
        Updates:
        - ALL_DFS: Global dictionary containing transformed DataFrames.
        
        Returns:
        - dict: Dictionary containing transformed DataFrames.
        """
        global ALL_DFS
        for df_name, df in list(ALL_DFS.items()):
            if "municipio del hecho" in df_name.lower():  # Case-insensitive check
                transformed_df = self.transform_and_save(df_name, df)
                ALL_DFS[df_name] = transformed_df  
        return ALL_DFS
    
if __name__ == "__main__":
    folder_name = '/path/to/your/folder'
    extractor = Extract()
    extractor.from_excel(folder_name)
    extractor.from_csv(folder_name)
    transformer = Transformation()
    dfs_dict = transformer.Violence_pivot()
    print(dfs_dict)
