import pickle
from flask import Flask,render_template,request

app=Flask(__name__)
model = pickle.load(open('linear-model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['GET','POST'])
def result():
    temp=request.form.get('temperature')
    prediction=model.predict([[temp]])
    print(prediction)
    res=round(prediction[0],2)
    print(res)
    return render_template('result.html',result=res,temp =temp)

if __name__ == '__main__':
    app.run(debug=True)    