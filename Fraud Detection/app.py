from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('source\\Random_Forest.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')




@app.route('/result', methods=['POST'])
def posting():
    data0 = int(request.form['step'])
    data1 = int(request.form['type'])
    data2 = float(request.form['amount'])
    data3 = float(request.form['balance-1'])
    data4 = float(request.form['balance-2'])
    data5 = float(request.form['balance-3'])

    #applying  prediction
    input_data = np.array([[data0,data1, data2, data3,data4,data5]])
    prediction = int(model.predict(input_data))
    return render_template('result.html', data=prediction)


if __name__ == '__main__':
    app.run(debug=True)