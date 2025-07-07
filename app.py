from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    uname=request.form['username']
    rno=request.form['rollno']
    email=request.form['email']
    year=request.form['year']
    return render_template('result.html',name=uname,rollno=rno,email=email,yr=year) 
if __name__=="__main__":
    app.run(debug=True)
