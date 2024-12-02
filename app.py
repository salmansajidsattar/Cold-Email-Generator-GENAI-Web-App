from flask import Flask, render_template, request, redirect, url_for, flash
from utils import Chain
import os
import others as ot
from portfolio import Portfolio
from flask_cors import CORS

app = Flask(__name__,template_folder='templates')
app.secret_key = os.urandom(24)
app.config['CORS_HEADERS'] = "application/json"
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/generate": {"origins": "http://localhost:5000"}})
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    print("enter into generate")
    if request.method == 'POST':
        data=request.get_json()
        links=data['Link']
        # links = request.args.get('link')
        print("test",links)
        if(len(links)==0):
            return 0
        else:
            print(links)
            chain = Chain()
            portfolio = Portfolio()
            try:
                result=ot.get_email(links, chain, portfolio)
                print(result)
                # chain = Chain()
                # email = chain.write_mail(job_description, links)
                return {"message":result}
                # return render_template('index.html', email=email)
            except Exception as e:
                print(e)
                return {"flag":"error"}
        
if __name__ == '__main__':
    app.run(port=5000,debug=True)