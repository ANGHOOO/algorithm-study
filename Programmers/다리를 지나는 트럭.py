def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridges = [0] * bridge_length
    current_weight = 0
    
    while truck_weights:
        answer += 1
        
        current_weight -= bridges.pop(0)
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridges.append(truck_weights.pop(0))
        else:
            bridges.append(0)
            
    return answer + bridge_length