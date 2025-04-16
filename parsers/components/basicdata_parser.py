from ..base_parser import BaseParser

class BasicDataParser(BaseParser):
    def parse(self):
        """Parse basic dataset information"""
        # Extract fields from the data object
        return {
            "design_name": self.data.get('name'),
            "designUUID": self.data.get('uniqueid'),
            "status_category": self.data.get('category'),
            "hierarchy": {
                "field": self.data.get('sort1'),
                "site": self.data.get('sort2'),
                "well": self.data.get('sort3'),
                "wellbore": self.data.get('sort4'),
            },
            "well_configuration": self.data.get('data', {}).get('configuration', {}).get('well_configuration', ''),
            "drilling_rig": self.data.get('data', {}).get('configuration', {}).get('drilling_unit', ''),
            "water_depth": self.data.get('data', {}).get('formation', {}).get('temperature', {}).get('water_depth', ''),
            "wellhead_depth": self.data.get('data', {}).get('formation', {}).get('temperature', {}).get('wellhead_depth', ''),
            "ground_elevation": self.data.get('data', {}).get('formation', {}).get('temperature', {}).get('ground_elevation', ''),
        }