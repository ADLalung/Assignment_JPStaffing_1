from flask import Flask, request, jsonify

app = Flask(__name__)

# This is the API endpoint YOU are creating for Step 1
@app.route('/api/signup', methods=['POST'])
def automate_signup():
    user_data = request.json

    # Here is where your code would send a request to Indeed/Capgemini's hidden API
    # For now, we are simulating that external request
    print(f"Automating signup for {user_data.get('email')}...")

    # Simulated success response from your API
    return jsonify({
        "status": "success",
        "message": "User signed up automatically on target portals",
        "mock_token": "abc-123-token",
    }), 201


# This is the API endpoint YOU are creating for Step 2
@app.route('/api/apply', methods=['POST'])
def automate_application():
    data = request.json
    job_id = data.get('job_id')

    # Here is where your code would send the resume to the portal's hidden API
    print(f"Automating application for Job ID: {job_id}")

    return jsonify({
        "status": "success",
        "message": f"Successfully applied to job {job_id} using API only",
    }), 200


if __name__ == '__main__':
    # This runs your API server
    app.run(debug=True, port=8080)
                                                                                                                