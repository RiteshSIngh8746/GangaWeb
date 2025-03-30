from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

FILES_DIRECTORY = r"D:\GJFS_Web\files"

@app.route('/list-files', methods=['GET'])
def list_files():
    try:
        files = os.listdir(FILES_DIRECTORY)
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment
    app.run(host='0.0.0.0', port=port)        # Bind to 0.0.0.0 for external access
