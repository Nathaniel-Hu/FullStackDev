from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)


@app.route('/')
def index()
    return render_template('index.html')


@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo):
    userInfo = json.loads(userInfo)
    print()
    print('PRODUCT INFO RECEIVED')
    print(------------------------)
    print(f"Product Name: {userInfo['name']}")
    print(f"Product Description: {userInfo['type']}")
    print()

    return 'Info Received Successfully'

if __name__ == "__main__":
    app.run(debug=True)