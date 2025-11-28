def player(prev_play, opponent_history=[], my_history=[], play_order=[{}]):
    counter = {'R': 'P', 'P': 'S', 'S': 'R', '': 'R'}
    
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        play_order[0] = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
    
    opponent_history.append(prev_play)
    n = len(opponent_history)
    
    quincy_pattern = ["R", "P", "P", "S", "R"]
    
    quincy_score = 0
    if n > 1:
        for i in range(1, n):
            expected = quincy_pattern[(i - 1) % 5]
            if opponent_history[i] == expected:
                quincy_score += 1
    quincy_match_rate = quincy_score / max(1, n - 1) if n > 1 else 0
    
    kris_score = 0
    if n > 2 and len(my_history) >= 1:
        checks = min(n - 2, len(my_history))
        for i in range(checks):
            expected_kris = counter.get(my_history[i], 'R')
            if i + 2 < len(opponent_history) and opponent_history[i + 2] == expected_kris:
                kris_score += 1
    kris_match_rate = kris_score / max(1, min(n - 2, len(my_history))) if n > 2 and len(my_history) >= 1 else 0
    
    mrugesh_score = 0
    mrugesh_checks = 0
    if n > 10 and len(my_history) >= 10:
        for i in range(10, min(n - 1, len(my_history) + 1)):
            last_ten = my_history[max(0, i - 10):i]
            if last_ten and len(last_ten) >= 5:
                most_freq = max(set(last_ten), key=last_ten.count)
                expected_mrugesh = counter[most_freq]
                mrugesh_checks += 1
                if i + 1 < len(opponent_history) and opponent_history[i + 1] == expected_mrugesh:
                    mrugesh_score += 1
    mrugesh_match_rate = mrugesh_score / max(1, mrugesh_checks) if mrugesh_checks > 0 else 0
    
    if quincy_match_rate >= 0.9 and n >= 10:
        next_quincy_idx = (n - 1) % 5
        next_quincy = quincy_pattern[next_quincy_idx]
        guess = counter[next_quincy]
        my_history.append(guess)
        return guess
    
    if kris_match_rate >= 0.8 and n >= 10 and len(my_history) >= 1:
        his_next = counter[my_history[-1]]
        guess = counter[his_next]
        my_history.append(guess)
        return guess
    
    if mrugesh_match_rate >= 0.7 and n >= 15 and len(my_history) >= 10:
        last_ten = my_history[-10:]
        most_freq = max(set(last_ten), key=last_ten.count)
        mrugesh_move = counter[most_freq]
        guess = counter[mrugesh_move]
        my_history.append(guess)
        return guess
    
    if len(my_history) >= 2:
        last_two = "".join(my_history[-2:])
        if last_two in play_order[0]:
            play_order[0][last_two] += 1
    
    if len(my_history) >= 1:
        potential_plays = [
            my_history[-1] + "R",
            my_history[-1] + "P",
            my_history[-1] + "S",
        ]
        sub_order = {k: play_order[0].get(k, 0) for k in potential_plays}
        abbey_prediction = max(sub_order, key=sub_order.get)[-1:]
        abbey_move = counter[abbey_prediction]
        guess = counter[abbey_move]
        my_history.append(guess)
        return guess
    
    guess = "P"
    my_history.append(guess)
    return guess
