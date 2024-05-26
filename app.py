from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    # 處理表單數據，例如保存到數據庫或發送郵件
    return '表單提交成功！'

if __name__ == '__main__':
    app.run(debug=True)
