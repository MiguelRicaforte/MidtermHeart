from flask import Flask, jsonify, request

app = Flask(__name__)

HeartInfo = [
    {
        "heart_id": "85291",
        "date": "08/11/2024",
        "heart_rate": "80 Bpm"
    },
    {
        "heart_id": "84932",
        "date": "08/10/2024",
        "heart_rate": "93 Bpm"
    }
]

@app.route('/heartInf/<heart_id1>', methods=['GET'])
def get_heart_info(heart_id1):
    heart_data = None
    for info in HeartInfo:
        if info['heart_id'] == heart_id1:
            heart_data = info
    if heart_data:
        return jsonify(heart_data)
    else:
        return jsonify({"error": "Heart information not found"}), 404

@app.route('/heartInf', methods=['POST'])
def addInf():
    newInf = request.get_json()  
    if newInf:  
        HeartInfo.append(newInf)
        return jsonify({"Successful": True, "Heart Info Added!": newInf}), 201 
    else:
        return jsonify({"error": "No data provided"}), 400

@app.route('/heartInf/<heartID>', methods=['DELETE'])
def delInf(heartID):
    index = next((i for i, info in enumerate(HeartInfo) if info["heart_id"] == heartID), None)
    
    if index is not None:
        deleted_record = HeartInfo.pop(index)
        return jsonify({"message": "Heart record deleted successfully", "deleted_record": deleted_record}), 200
    else:
        return jsonify({"error": "Heart record not found"}), 404


@app.route('/heartInf/<heart_id>', methods=['PUT'])
def update_heart_info(heart_id):
    heart_data = None
    for info in HeartInfo:
        if info['heart_id'] == heart_id:
            heart_data = info
    if heart_data:
        data = request.get_json()
        heart_data['date'] = data.get('date', heart_data['date'])
        heart_data['heart_rate'] = data.get('heart_rate', heart_data['heart_rate'])
        return jsonify({"message": "Heart record updated successfully", "updated_record": heart_data}), 200
    else:
        return jsonify({"error": "Heart information not found"}), 404


if __name__ == '__main__':
    app.run()
