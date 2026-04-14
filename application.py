from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def msg():
    return "Hello"

@app.route('/freq',methods=["POST"])
def freq():
    data = request.json.get("data")
    if not data:
        return {'error':'Invalid input'},400
    frequ={}
    sdata = list(set(data))
    for i in sdata:
        count = data.count(i)
        frequ.update({i:count})

    return frequ

if __name__=="__main__":
    app.run()