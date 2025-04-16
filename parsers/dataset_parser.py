from .base_parser import BaseParser
from .components.basicdata_parser import BasicDataParser
from .components.porepressure_parser import PorePressureParser
from .components.fracpressure_parser import FracPressureParser
from .components.collapsepressure_parser import CollapsePressureParser
from .components.minstress_parser import MinstressPressureParser
from .components.schematic_parser import SchematicParser  
from .components.trajectory_parser import TrajectoryParser

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
                        
            # Add pore pressure
            formation_data = data.get('formation', {}).get('pore_pressure', [])
            porepressure_parser = PorePressureParser(formation_data)
            ordered_result["pore_pressure"] = porepressure_parser.parse()
            
            # Add frac pressure
            formation_data = data.get('formation', {}).get('fracture_pressure', [])
            fracpressure_parser = FracPressureParser(formation_data)
            ordered_result["frac_pressure"] = fracpressure_parser.parse()

            # Add collapse pressure
            formation_data = data.get('formation', {}).get('collapse_pressure', [])
            collapsepressure_parser = CollapsePressureParser(formation_data)
            ordered_result["collapse_pressure"] = collapsepressure_parser.parse()

            # Add minimum horisontal pressure
            formation_data = data.get('formation', {}).get('min_horizontal_stress', [])
            minstresspressure_parser = MinstressPressureParser(formation_data)
            ordered_result["minumum_horisontal_stress_pressure"] = minstresspressure_parser.parse()

            # Add well schematic information
            casing_scheme_data = data.get('casing', {}).get('scheme', [])
            schematic_parser = SchematicParser(casing_scheme_data)
            ordered_result["well_schematic"] = schematic_parser.parse()

            # Add trajectory information
            trajectory_data = data.get('sites', [])[0].get('wells', [])[0].get('model', [])
            trajectory_parser = TrajectoryParser(trajectory_data)
            ordered_result["well_trajectory"] = trajectory_parser.parse()

            return ordered_result, None
            
        except Exception as e:
            return None, str(e)