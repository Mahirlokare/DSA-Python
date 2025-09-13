def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    selected = [activities[0]]
    last_end = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            selected.append(activities[i])
            last_end = activities[i][1]
    return selected

start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]
print("Selected activities:", activity_selection(start, end))
