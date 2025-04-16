from ..base_parser import BaseParser

class TrajectoryParser(BaseParser):
    def parse(self):
        """Parse main trajectory data from the model array"""
        result = []
        units = {}
        
        # Access the trajectory data through the correct path
        trajectory_data = self.data.get("datasetdb", {}).get("data", {}).get("sites", [])[0].get("wells", [])[0].get("model", [])
        
        if trajectory_data and len(trajectory_data) > 0:
            # Extract units from the first row if it's a units row
            first_item = trajectory_data[0]
            if first_item.get("type") == "Units":
                units = {
                    "md": first_item.get("md"),
                    "tvd": first_item.get("tvd"),
                    "inc": first_item.get("inc"),
                    "azi": first_item.get("azi"),
                    "dls": first_item.get("dls"),
                    "ns": first_item.get("ns"),
                    "ew": first_item.get("ew"),
                    "cl": first_item.get("cl"),
                    "tf": first_item.get("tf"),
                    "tr": first_item.get("tr"),
                    "br": first_item.get("br")
                }
            
            # Process all trajectory points (including units if needed)
            for item in trajectory_data:
                point_type = item.get("type")
                
                # Create a trajectory point
                trajectory_point = {
                    "type": point_type,
                    "md": item.get("md"),
                    "tvd": item.get("tvd"),
                    "inc": item.get("inc"),
                    "azi": item.get("azi"),
                    "dls": item.get("dls"),
                    "ns": item.get("ns"),
                    "ew": item.get("ew"),
                    "cl": item.get("cl"),
                    "tf": item.get("tf"),
                    "tr": item.get("tr"),
                    "br": item.get("br")
                }
                
                # For complex types with nested data (like Opt.Align or DLS Hold)
                if "rows" in item:
                    trajectory_point["rows"] = item.get("rows")
                
                if "buildToTarget" in item:
                    trajectory_point["buildToTarget"] = item.get("buildToTarget")
                
                # Add to result list
                result.append(trajectory_point)
        
        return {
            "data": result,
            "units": units
        }