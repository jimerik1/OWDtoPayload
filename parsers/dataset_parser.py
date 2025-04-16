from .base_parser import BaseParser
from .components.blowoutkill_parser import BlowoutKillParser
from .components.basicdata_parser import BasicDataParser
from .components.formationdata_parser import FormationDataParser

class DatasetParser(BaseParser):
    def parse(self):
        """Parse the complete dataset"""
        try:
            dataset = self.data.get('datasetdb', {})
            
            # Create an empty result dict
            result = {}
            
            # Extract data section
            data = dataset.get('data', {})
            
            # Create a new dictionary in the specific order we want
            ordered_result = {}
            
            # 1. Add basic_info 
            basic_data_parser = BasicDataParser(dataset)
            ordered_result["basic_info"] = basic_data_parser.parse()
            
            # 2. Add blowoutkill 
            blowoutkill_data = data.get('blowoutkill', [])
            blowoutkill_parser = BlowoutKillParser(blowoutkill_data)
            ordered_result["blowoutkill"] = blowoutkill_parser.parse()
            
            # Add formationdata
            formation_data = data.get('formationdata', [])
            formationdata_parser = FormationDataParser(formation_data)
            ordered_result["formationdata"] = formationdata_parser.parse()
            
            return ordered_result, None
            
        except Exception as e:
            return None, str(e)