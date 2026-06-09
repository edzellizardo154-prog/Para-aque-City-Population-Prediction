import time
from collections import deque

class Process:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.state = "New"

    def __str__(self):
        return f"P{self.pid} - {self.name}"

# Process List
processes = [
    Process(1, "Facial Recognition", 2),
    Process(2, "Medical Record Retrieval", 2),
    Process(3, "Staff Authentication", 3),
    Process(4, "Emergency Patient Verification", 1),  # Highest priority
    Process(5, "QR Verification", 2)
]

ready_queue = deque()

print("\n=== RAPIDCARE OS PROCESS MANAGEMENT SIMULATION ===\n")

# NEW -> READY
for p in processes:
    p.state = "Ready"
    ready_queue.append(p)
    print(f"{p} : New -> Ready")

time.sleep(1)

# Hybrid Scheduling (Priority-Based)
ready_queue = deque(sorted(ready_queue, key=lambda x: x.priority))

while ready_queue:

    current = ready_queue.popleft()

    current.state = "Running"
    print(f"\nCPU Assigned to {current}")
    print(f"State: Running")

    time.sleep(1)

    # Context Switching Example
    if current.name == "Facial Recognition":

        print("\n*** Context Switch Occurred ***")
        print("Saving Facial Recognition state...")

        current.state = "Waiting"

        qr_process = Process(6, "QR Verification", 1)
        qr_process.state = "Running"

        print("QR Verification Running...")
        time.sleep(1)

        print("Verification Complete")
        qr_process.state = "Terminated"

        print("Resuming Facial Recognition...")
        current.state = "Running"
        time.sleep(1)

    # Simulate I/O Waiting
    if current.name == "Medical Record Retrieval":

        print("Waiting for database response...")
        current.state = "Waiting"
        time.sleep(1)

        print("Database response received.")
        current.state = "Running"

    # Process Completion
    current.state = "Terminated"
    print(f"{current} : Terminated")

print("\n=== ALL PROCESSES COMPLETED ===")