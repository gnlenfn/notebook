from collections import defaultdict
def solution(record):
    logs = []
    room = defaultdict(int)
    for log in record:
        command = log.split()
        if command[0] == "Leave":
            status, user_id = command
        else:
            status, user_id, name = command

        if status == "Enter":
            room[user_id] = name
            logs.append([user_id, "Enter"])
        elif status == "Leave":
            logs.append([user_id, "Leave"])
        else:
            room[user_id] = name

    answer = []
    for result in logs:
        if result[1] == "Enter":
            text = room[result[0]]+ "님이 들어왔습니다."
        else:
            text = room[result[0]]+ "님이 나갔습니다."
        answer.append(text)
    return answer

def solution(record):
    answer = []
    logs = dict()
    text = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for log in record:
        status = log.split()
        if status[0] in ['Enter', 'Change']:
            logs[status[1]] = status[2]
    
    for log in record:
        status = log.split()
        if status[0] != "Change":
            answer.append(logs[status[1]] + text[status[0]])
    
    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))