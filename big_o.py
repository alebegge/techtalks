import pandas as pd 
import matplotlib.pyplot as plt


index = [2,3,4,5,6]
time_bob = [0.1,3,58,597,2052]
time_marc = [0.01,0.9,15,247,900]

# df = pd.DataFrame(zip(index,time_bob,time_marc), columns=["log(n)", "Time Bob", "Time Marc"])
# print(df)

# plt.plot(df["log(n)"], df["Time Bob"],'o-', color='#4495A2', label='Bob')
# plt.plot(df["log(n)"], df["Time Marc"],'o-', color='#F9D448', label='Marc')
# plt.title("Time (s) per n input for each solution.", pad=20)
# plt.xlabel('log(n)')
# plt.ylabel('Time(s)')
# plt.legend()
# plt.show()

# x**3 

def bob_solution(n):
    solutions = 0
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                if a+b+c == n:
                    solutions += 1
    return solutions

print(bob_solution(10))

def marc_solution(n):
    solutions = 0
    for a in range(n+1):
        for b in range(n+1):
            c = n-(a+b)
            if c >= 0:
                solutions +=1
    return solutions

print(marc_solution(10))


