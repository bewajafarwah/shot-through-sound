import numpy as np

def before(values):
    total = 0
    l = len(values)
    for i in range(l):
        total += abs(values[i])
    try:
        print('Vad: ' + str(len(values)) + ' ' + str(total/l))
        return (total / l)
    except:
        #print(total, l, values)
        return 0

def check_for_one(values):
    for val in values:
        if abs(val) > 0.87:
            return True
    return False

# while i < len(y):
#     if gate:
#         if y[i] >= 0.5:
#             high.append(y[i])
#             count+=1
#         else:
#             if count > 15 and before(low) < 0.15 and check_for_one(high):
#                 print(i / 44100)
#                 khazana.write(str(round((i / 44100), 2)) + '\n')
#             count = 0
#             i+=999
#             gate = False
#             low = []
#             high = []
#     else:
#         if y[i] >= 0.5:
#             count+=1
#             high.append(y[i])
#             gate = True
#         else:
#             low.append(y[i])
#     i+=1

def get_answer(y):
    i = 0
    count = 0
    indices = []
    low = []
    high = []
    gate = False

    answer = []

    print('Finding Shots:')
    while i < len(y):
        if gate:
            if y[i] >= 0.5:
                high.append(y[i])
                count+=1
            else:
                if count > 15 and before(low) < 0.15 and check_for_one(high):
                    answer.append(i/44100)
                    print(len(answer))
                count = 0
                low = []
                high = []
                gate = False
                i+=4999
        else:
            if y[i] >= 0.5:
                low = []
                high.append(y[i])
                count+=1
                gate = True
            else:
                low.append(y[i])
        i+=1
    return answer