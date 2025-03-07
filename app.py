import requests
import json
import os

# Load Asana API Token from Environment Variables
ASANA_ACCESS_TOKEN = os.getenv("2/1204220771478700/1209557208654124:14e1caffe986d2899907f8fabb501f14")
ASANA_PROJECT_ID = os.getenv("1209353707682767")

# Set up headers for API requests
HEADERS = {
    "Authorization": f"Bearer {ASANA_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def get_project_tasks():
    """Fetch tasks from the Asana project."""
    url = f"https://app.asana.com/api/1.0/projects/{ASANA_PROJECT_ID}/tasks"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error fetching tasks: {response.text}")
        return []

def summarize_tasks(tasks):
    """Generate summary statistics for project tasks."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.get("completed", False))
    
    return f"Total Tasks: {total_tasks}, Completed: {completed_tasks}"

def update_project_status(summary):
    """Update the Asana project status with the summary."""
    url = f"https://app.asana.com/api/1.0/projects/{ASANA_PROJECT_ID}"
    data = {
        "data": {
            "notes": summary
        }
    }
    response = requests.put(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        print("Project status updated successfully.")
    else:
        print(f"Error updating project status: {response.text}")

def main():
    tasks = get_project_tasks()
    summary = summarize_tasks(tasks)
    update_project_status(summary)

if __name__ == "__main__":
    main()
