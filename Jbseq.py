def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result = [-1]*n
    profit = 0
    for job in jobs:
        for j in range(min(n, job[1])-1, -1, -1):
            if result[j] == -1:
                result[j] = job[0]
                profit += job[2]
                break
    print("Jobs scheduled:", [j for j in result if j != -1])
    print("Total Profit:", profit)

n = int(input("Enter number of jobs: "))
jobs = []
print("Enter job details (JobID Deadline Profit):")
for _ in range(n):
    jobid, deadline, profit = input().split()
    jobs.append((jobid, int(deadline), int(profit)))
job_sequencing(jobs, n)

# Complexity: O(n^2)
