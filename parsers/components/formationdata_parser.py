from ..base_parser import BaseParser

class FormationDataParser(BaseParser):
    def parse(self):
        """Parse formation data"""
        result = []
        
        if self.data and isinstance(self.data, list) and len(self.data) > 1:
            # Get column headers from first row
            headers = self.data[0]
            
            # Process each data row (skip the header row)
            for item in self.data[1:]:
                if len(item) >= 3:  # Ensure we have at least depth, sg, and pressure values
                    parsed_item = {
                        "depth": item[0],          # depth in meters
                        "specific_gravity": item[1],  # sg value
                        "pressure": item[2]        # pressure in bar
                    }
                    result.append(parsed_item)
        
        return {
            "data": result
        }
