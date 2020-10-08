def solution(bridge_length, max_weight, truck_weights):
    # FIFO 문제.
    bridge = [0]*bridge_length
    curr_weight = 0
    ans = 0
    while len(truck_weights) > 0:
        ans += 1
        ar = bridge.pop(0)
        curr_weight -= ar
        if curr_weight + truck_weights[0] > max_weight:
            bridge.append(0)            
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            curr_weight += truck
    while curr_weight > 0:
        ans += 1
        ar = bridge.pop(0)
        curr_weight -= ar
    return ans
