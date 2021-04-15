from flask import Flask, render_template, request
import pickle
import pandas as pd
# Python program to read 
# image using matplotlib
  
# importing matplotlib modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
  
# Read Images
img = mpimg.imread('aa.jpg')
  
# Output Images


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/database', methods=['POST', 'GET'])
def database ():
    data = pd.read_csv('credit_train.csv')
    dataArray = [data.columns.values.tolist()] + data.values.tolist()
    return render_template('dataset.html', dataArray = dataArray, row = len(dataArray), col = len(dataArray[0]))

@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        user = request.form.to_dict()
        
        # print(user)

        if 850 >= int(user['credit score']) >= 720.0 :
            user['credit score'] = 'Excellent'
        elif int(user['credit score']) >= 690.0 :
            user['credit score'] = 'Good'
        elif int(user['credit score']) >= 630.0 :
            user['credit score'] = 'Fair'
        elif int(user['credit score']) <= 629.0 :
            user['credit score'] = 'Poor'

        df_to_predict = pd.DataFrame({
            'current loan amount': [user['current loan amount']], # name yang nanti diprediksi
            'term': [user['term']],
            'credit score': [user['credit score']],
            'annual income': [user['annual income']],
            'years in current job': [user['years in current job']],
            'home ownership': [user['home ownership']],
            'purpose': [user['purpose']],
            'monthly debt': [user['monthly debt']],
            'years of credit history': [user['years of credit history']],
            'number of open accounts': [user['number of open accounts']],
            'number of credit problems': [user['number of credit problems']],
            'current credit balance': [user['current credit balance']],
            'maximum open credit': [user['maximum open credit']],
            'bankruptcies': [user['bankruptcies']],
            'tax liens': [user['tax liens']]
        })
        

        prediksi = model.predict_proba(df_to_predict)[:,0]
        # print(prediksi)

        if prediksi < 0.498691:
            hasil = 'Congratulations! Your loan is approved.', plt.imshow(img)
        else:
            hasil = 'Sorry, your loan is not approved', plt.imshow(img)

        return render_template('result.html', data=user, pred=hasil)


if __name__ == '__main__':

    filename = 'abc_final.sav'
    model = pickle.load(open(filename, 'rb'))

    app.run(debug=True, port=5000)
