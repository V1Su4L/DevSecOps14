from flask import Flask, request, jsonify

app = Flask(__name__)

game_sessions = {}  # Dictionary to store game sessions


@app.post('/start')
def startGame():
    global game_sessions
    game_id = len(game_sessions) + 1
    game_sessions[game_id] = {"player1_score": 0, "player2_score": 0}
    return {"message": "Game started successfully.", "game_id": game_id}, 200


@app.post('/score')
def recordScore():
    data = request.json
    game_id = data.get('game_id')
    player_id = data.get('player_id')

    if game_id is None or player_id is None or player_id not in [1, 2]:
        return {"error": "Invalid request data"}, 400

    global game_sessions
    if game_id not in game_sessions:
        return {"error": "Game ID not found"}, 404

    game_sessions[game_id][f"player{player_id}_score"] += 1

    return {"message": "Score recorded successfully."}, 200


@app.get('/score')
def getScore():
    global game_sessions
    game_id = request.args.get('game_id')

    if game_id is None:
        return {"error": "Game ID is missing"}, 400

    try:
        game_id = int(game_id)
    except ValueError:
        return {"error": "Invalid Game ID"}, 400

    if game_id not in game_sessions:
        return {"error": "Game ID not found"}, 404

    scores = game_sessions[game_id]
    return jsonify(scores), 200


@app.post('/end')
def endGame():
    data = request.json
    game_id = data.get('game_id')

    if game_id is None:
        return {"error": "Game ID is missing"}, 400

    global game_sessions
    if game_id not in game_sessions:
        return {"error": "Game ID not found"}, 404

    player1_score = game_sessions[game_id]['player1_score']
    player2_score = game_sessions[game_id]['player2_score']

    if player1_score > player2_score:
        winner = 'Player 1'
    elif player1_score < player2_score:
        winner = 'Player 2'
    else:
        winner = 'No one (It\'s a tie)'

    del game_sessions[game_id]  # Remove the game session

    return {"message": f"Game ended successfully. {winner} wins!"}, 200


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
