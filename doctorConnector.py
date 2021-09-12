from flask import Flask, request

app = Flask(__name__)

publicKeys = {}

@app.route("/start_share", methods=['POST'])
def handleStartShare():
    publicKey = request.get_json()
    publicKeys[publicKey] = None

    return "DONE"

@app.route("/upload", methods=['POST'])
def handleUpload():
    data = request.get_json()
    for k in data:
        if (k in publicKeys.keys()):
            publicKeys[k] = data[k]
    return "DONE"

@app.route("/data", methods=['POST'])
def handleData():
    data = request.get_json()
    if (data in publicKeys.keys() and publicKeys[data] != None):
        return str(publicKeys[data])
    else:
        return ""

@app.route("/stop_share", methods=['POST'])
def handleStopShare():
    keyToRemove = request.get_json()
    if (keyToRemove in publicKeys.keys()):
        del publicKeys[keyToRemove]
    return "DONE"


if __name__ == '__main__':
	app.run(debug=True)

