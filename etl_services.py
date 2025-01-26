import pandas as pd
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from datetime import datetime
from abc import ABC, abstractmethod


# Define file path and database details
file_path = "test_data/Exportaciones.xlsx"  
db_path = "exportaciones.db"
table_name = "coffee_exports"


class ExtractService(ABC):
    @abstractmethod
    def extract(self):
        pass

class XlSXExtractService(ExtractService):
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):

        data = pd.read_excel(file_path)
        return data
    

    
class TransformService(ABC):
    @abstractmethod
    def transform(self, data):
        pass

class BasicTransformService(TransformService):
    def transform(self, data):

        data = pd.read_excel("test_data/Exportaciones.xlsx",sheet_name="7. Destino_Tipo_Vol_Val",header=7,usecols="C:I")
        data = data.dropna(how='all')
        metadata_start_index = data[data.iloc[:, 0].astype(str).str.contains("\* Cifras preliminares", na=False)].index
        if not metadata_start_index.empty:
            last_valid_index = metadata_start_index[0] - 1
            data = data.loc[:last_valid_index]

        data['Año'] = data['Año'].astype(float)
        data['Mes'] = data['Mes'].astype(float)
        data['País de destino'] = data['País de destino']
        data['Sacos de 60 Kg. Exportados'] = data['Sacos de 60 Kg. Exportados'].astype(float)
        
        return data
    

class LoadService(ABC):
    @abstractmethod
    def load(self, data):
        pass

class SQLiteLoadService(LoadService):
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name

    def load(self, data):
        engine = create_engine(f'sqlite:///{self.db_path}')
        data['timestamp'] = datetime.now()
        data.to_sql(self.table_name, con=engine, if_exists='replace', index=False)


class ETLPipeline:
    def __init__(self, extractor: ExtractService, transformer: TransformService, loader: LoadService):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        extracted_data = self.extractor.extract()
        transformed_data = self.transformer.transform(extracted_data)
        self.loader.load(transformed_data)
        

# Instantiate services
extract_service = XlSXExtractService(file_path)
transform_service = BasicTransformService()
load_service = SQLiteLoadService(db_path, table_name)

# Run the pipeline
pipeline = ETLPipeline(extract_service, transform_service, load_service)
pipeline.run()

print("ETL pipeline executed successfully!")