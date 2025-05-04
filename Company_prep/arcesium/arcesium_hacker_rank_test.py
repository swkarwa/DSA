"""
Process scheduling algorithms are used by a CPU to optimally schedule the running processes. A core can execute one process at a time, but a CPU may have multiple cores.
There are n processes where the ith process starts its execution at startfil and ends at end[il, both inclusive. Find the minimum number of cores required to execute the processes.
Example
n = 3
start = [1, 3, 4]
end = [3, 5, 6].
If the CPU has only one core, the first process starts at 1 and ends at 3. The second process starts at 3. Since both processes need a processor at 3, they overlap. There must be more than 1 core.


"""
def min_cores_required(start, end):
    # Create a list of events
    events = []
    for s in start:
        events.append((s, 'start'))  # Process starts
    for e in end:
        events.append((e + 1, 'end'))  # Process ends (end + 1)

    # Sort events
    events.sort(key=lambda x: (x[0], x[1] == 'start'))

    max_cores = 0
    current_cores = 0

    # Count the number of cores needed
    for event in events:
        if event[1] == 'start':
            current_cores += 1  # A new process starts
        else:
            current_cores -= 1  # A process ends
        max_cores = max(max_cores, current_cores)

    return max_cores

# Example usage
n = 3
start = [1, 3, 4]
end = [3, 5, 6]
print(min_cores_required(start, end))  # Output: 2
