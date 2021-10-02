scores = []
for i in range(5):
    scores.append(float(input("Enter a test score:")))

print("All scores:", scores)

print("Students who scored below 60 get 10 extra points.")

scores1 = []

for i in scores:
    if i < 60:
        scores1.append(i + 10)
    else:
        scores1.append(i)

print("All scores:", scores1)

print("Students whose scores have changed:")

for i in range(5):
    if scores[i] == scores1[i]:
        continue
    print("Old Score:", scores[i], "New Score:", scores1[i])
