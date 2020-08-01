def solution(bridge_length, max_weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    cur_weight = 0

    while truck_weights:
        cur = truck_weights.pop(0)
        time += 1
        cur_weight -= cur
        