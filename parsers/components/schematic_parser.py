from ..base_parser import BaseParser

class SchematicParser(BaseParser):
    def parse(self):
        """Parse well schematic and string information"""
        result = {}
        
        # Assuming self.data is a list of casing scheme objects
        for i, casing in enumerate(self.data):
            # Create a string index
            string_index = i + 1
            
            # Extract the base casing data
            string_data = {
                "index": string_index,
                "top_depth": casing.get("top"),
                "bottom_depth": casing.get("bottom"),
                "top_of_cement": casing.get("toc"),
                "string_function": casing.get("name"),
                "string_type": casing.get("type"),
                "float_depth": casing.get("float"),
                "mud_density": casing.get("mudatshoe"),
                "section_depth": casing.get("holedepth"),
                "hole_size": casing.get("holesize"),
            }
            
            # Extract string section information
            sections = {}
            for j, string in enumerate(casing.get("strings", [])):
                section_index = j + 1
                section_data = {
                "index": section_index,
                "id": string.get("id"),
                "od": string.get("od"),
                "top": string.get("top"),
                "drift_id": string.get("int_drift"),
                "nominal_weight": string.get("nominal_weight"),
                "grade": string.get("grade"),
                "collapse_rating": string.get("casing_obj", {}).get("casing", {}).get("collapse"),
                "burst_rating": string.get("casing_obj", {}).get("casing", {}).get("burst"),
                "axial_rating": string.get("casing_obj", {}).get("casing", {}).get("axial"),  
                "youngs_modulus": string.get("casing_obj", {}).get("materialProperties", {}).get("youngs_modulus"),
                "specific_heat_capacity": string.get("casing_obj", {}).get("materialProperties", {}).get("specific_heat_capacity"),
                "thermal_conductivity": string.get("casing_obj", {}).get("materialProperties", {}).get("thermal_conductivity"),
                "string_density": string.get("casing_obj", {}).get("materialProperties", {}).get("density"),
                "poison_ratio": string.get("casing_obj", {}).get("materialProperties", {}).get("poissons_ratio"),
                
                }
                sections[section_index] = section_data
            
            # Add string sections to the string data
            string_data["sections"] = sections
            
            # Add to result using the index as the key
            result[string_index] = string_data
        
        return result