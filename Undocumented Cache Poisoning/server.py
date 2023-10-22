from flask import Flask, request, send_from_directory
from werkzeug.exceptions import NotFound
import os
import re

app = Flask(__name__)

# تحديد مكان مجلد الـ static
STATIC_DIR = 'static'

# التحقق من وجود المجلد، وإنشاؤه إذا لم يكن موجودًا
if not os.path.exists(STATIC_DIR):
    os.mkdir(STATIC_DIR)

class Dispatcher:
    def __init__(self):
        self._cache = {}

    def _get_sensitive_info(self):
        sensitive_data = {
            "email": "secret@email.com",
            "password": "SuperSecretPassword123"
        }
        
        html_content = f"""
        <html>
        <body>
            <h2>Sensitive Information</h2>
            <p>Email: {sensitive_data["email"]}</p>
            <p>Password: {sensitive_data["password"]}</p>
        </body>
        </html>
        """
        
        return html_content

    def dispatch(self, data_type):
        if data_type in self._cache:
            return self._cache[data_type]

        response = self._get_sensitive_info()
        self._cache[data_type] = response
        return response

dispatcher = Dispatcher()

@app.route('/data', methods=['GET'])
def get_data():
    raw_query = request.query_string.decode('utf-8')
    
    if '&' in raw_query:
        # استخدم التعبير النمطي للبحث عن اسم الملف بامتداد .js
        match = re.search(r'([\w\d_-]+\.js)', raw_query)
        
        if match:
            filename = match.group(1)
            sensitive_data = dispatcher.dispatch("sensitive_info")
            with open(os.path.join(STATIC_DIR, filename), 'w') as file:
                file.write(sensitive_data)
            return jsonify({"response": f"JavaScript file '{filename}' with HTML content has been created!"})
    
    # رمي استثناء NotFound لتظهر صفحة الخطأ 404 الافتراضية
    raise NotFound()

@app.route('/static/<path:filename>', methods=['GET'])
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
