import pickle
import warnings
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from flask import Flask , render_template  , request

warnings.filterwarnings ('ignore')

app = Flask(__name__, template_folder= "template")

@app.route("/")
def home():
   return render_template("home.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    rmean = int(request.form['rmean'])
    pmean = int(request.form['pmean'])
    amean = int(request.form['amean'])
    cmean = int(request.form['cmean'])
    wmean = int(request.form['wmean'])
    awmean = int(request.form['awmean'])
    pwmean = int(request.form['pwmean'])
    cwmean = int (request.form ['cwmean'])
    model = pickle.load (open ('D://Projects//Mini Project SEM V Secured//Breast_Cancer_PY//model.sav', 'rb'))

    def predict_cancer (lst):
        if model.predict (lst)[0] == 0:
         return ('Benign Cancer detected !!!')
        else:
         return ('Malignant Cancer detected !!!')

    patient_detail = [[rmean, pmean, amean, cmean, wmean, pwmean, awmean, cwmean]]
    result = predict_cancer (patient_detail)    
  
    return render_template('home.html' , predict  = result)

if __name__ == '__main__':
    app.run(debug = True)