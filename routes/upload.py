from flask import request, jsonify
from routes import upload_bp
from parsers import DatasetParser

@upload_bp.route('/upload', methods=['POST'])
def upload_json():
    try:
        # Get JSON data from request body
        json_data = request.get_json()
        
        if not json_data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Parse the dataset directly without schema validation
        parser = DatasetParser(json_data)
        result, error = parser.parse()
        
        if error:
            return jsonify({"error": "Failed to parse dataset", "details": error}), 400
            
        # Create response in desired order
        response = {
            "success": True,
            "data": result
        }
            
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500