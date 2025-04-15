from ..base_parser import BaseParser

class BlowoutKillParser(BaseParser):
    def parse(self):
        """Parse blowoutkill data"""
        result = []
        
        for item in self.data:
            parsed_item = {
                "name": item.get('name'),
                "time": item.get('time'),
                "casing_id": item.get('casingid'),
                "frames": item.get('frames'),
                "xgrid": item.get('xgrid'),
                "ygrid": item.get('ygrid'),
                "init_cond": item.get('init_cond'),
                "kill_time": item.get('kill_time')
            }
            result.append(parsed_item)
            
        return {
            "count": len(result),
            "data": result
        }