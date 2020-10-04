def solution(numbers, hand):
    answer = ''
    pad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), "#": (3, 2)}
    hand_position = ["*", "#"]
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            hand_position[0] = num
            
        elif num in [3, 6, 9]:
            answer += "R"
            hand_position[1] = num
            
        else:
            near_hand = get_near_hand(hand_position[0], hand_position[1], num, pad, hand)
            if near_hand == "left":
                answer += "L"
                hand_position[0] = num
            else:
                answer += "R"
                hand_position[1] = num
    return answer

def get_near_hand(l, r, num, pad, hand):
    left_distance = abs(pad[l][0] -  pad[num][0]) + abs(pad[l][1] - pad[num][1])
    right_distance = abs(pad[r][0] - pad[num][0]) + abs(pad[r][1] - pad[num][1])
    if left_distance < right_distance:
        return "left"
    elif left_distance > right_distance:
        return "right"
    else:
        return hand