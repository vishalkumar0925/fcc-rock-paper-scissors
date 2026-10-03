def player(prev_play, opponent_history=[], play_order={}):
    if prev_play == "":
        opponent_history.clear()
        play_order.clear()

    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R"
    n = 4

    if len(opponent_history) >= n:
        pattern = "".join(opponent_history[-n:])
        play_order[pattern] = play_order.get(pattern, 0) + 1

        last_few_moves = "".join(opponent_history[-(n - 1):])
        possible_next_moves = [last_few_moves + move for move in ["R", "P", "S"]]

        predictive_counts = {
            move[-1]: play_order.get(move, 0) for move in possible_next_moves
        }

        predicted_move = max(predictive_counts, key=predictive_counts.get)
        winning_counter = {"R": "P", "P": "S", "S": "R"}
        guess = winning_counter[predicted_move]

    return guess