from ..base_parser import BaseParser

class CollapsePressureParser(BaseParser):
    def parse(self):
        """Parse collapse pressure data"""
        result = []
        units = {}
        
        # Assuming self.data is the 2D array
        if len(self.data) > 1:
            # Extract units from the first row
            unit_row = self.data[0]
            if len(unit_row) >= 3:
                units = {
                    "depth": unit_row[0],      
                    "specific_gravity": unit_row[1],  
                    "pressure": unit_row[2]    
                }
            
            # Process data rows (skip the header row)
            for item in self.data[1:]:
                if len(item) >= 3:
                    parsed_item = {
                        "depth": item[0],
                        "specific_gravity": item[1],
                        "pressure": item[2]
                    }
                    result.append(parsed_item)
        
        return {
            "data": result,
            "units": units
        }