from .base_parser import BaseParser
from .components.blowoutkill_parser import BlowoutKillParser
from .components.annularflex_parser import AnnularFlexParser

class DatasetParser(BaseParser):
    def parse(self):
        """Parse the complete dataset"""
        try:
            dataset = self.data.get('datasetdb', {})
            
            # Extract basic information
            result = {
                "dataset_id": dataset.get('datasetid'),
                "user_id": dataset.get('userid'),
                "group_id": dataset.get('groupid'),
                "name": dataset.get('name'),
                "category": dataset.get('category'),
                "type": dataset.get('type'),
                "sort_fields": {
                    "sort1": dataset.get('sort1'),
                    "sort2": dataset.get('sort2'),
                    "sort3": dataset.get('sort3'),
                    "sort4": dataset.get('sort4')
                }
            }
            
            # Extract data section
            data = dataset.get('data', {})
            
            # Parse blowoutkill data if present
            blowoutkill_data = data.get('blowoutkill', [])
            blowoutkill_parser = BlowoutKillParser(blowoutkill_data)
            result["blowoutkill"] = blowoutkill_parser.parse()
            
            # Parse annularflex data if present
            annularflex_data = data.get('annularflex', [])
            annularflex_parser = AnnularFlexParser(annularflex_data)
            result["annularflex"] = annularflex_parser.parse()
            
            return result, None
            
        except Exception as e:
            return None, str(e)