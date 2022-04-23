import requests
import json
from dotenv import load_dotenv
import os

# The API URL and API token for the Todoist API.
API_URL = "https://api.todoist.com/sync/v8"

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

def get_projects():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    params = {
        "sync_token": "*",
        "resource_types": "["
        "\"projects\""
        "]"
    }

    r = requests.post(f'{API_URL}/sync', headers=headers, data=json.dumps(params))
    return r.json()

def get_project_data(project_id):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    params = {
        "project_id": project_id,
    }

    r = requests.post(f'{API_URL}/projects/get_data', headers=headers, data=json.dumps(params))
    return r.json()

def get_items(item_id):

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    params = {
        "item_id": item_id,
    }

    r = requests.post(f'{API_URL}/items/get', headers=headers, data=json.dumps(params))
    return r.json()

def get_tasks(project_id, section_id):
    task_description = []
    project_data = get_project_data(project_id)
    for task in project_data["items"]:

        if task["section_id"] == int(section_id):
            # Get task ID
            task_id = task["id"]
            task_name = task["content"]
            task_description.extend((f"# {task_name}", task["description"].replace("```", "").strip()))

            task_comments = get_items(task_id)
            if "notes" in task_comments:
                task_description.extend(note["content"].replace("```", "").strip() for note in task_comments["notes"])

    with open("setup.sh", "w") as file:
        for line in task_description:
            if line.strip():
                if line.startswith("#"):
                    file.write("\n" + line + "\n")
                else:
                    file.write(line + "\n")

def main():
    options_id = []
    options_section_id = []
    projects = get_projects()
    for project in projects["projects"]:
        print(project["name"] + ": " + str(project["id"]))
        options_id.append(project["id"])

    while True:
        project_id = input("Enter a project id: ")
        if project_id in str(options_id):
            print(f"\n\nYou have selected {project_id}\n\n")
            break
        else:
            print("Invalid project id.")

    project_data = get_project_data(project_id)
    with open("todoist.json", "w") as f:
        json.dump(project_data, f, indent=4)
    for section in project_data["sections"]:
        options_section_id.append(section["id"])
        print(section["name"] + ": " + str(section["id"]))

    while True:
        section_id = input("Enter a section id: ")
        if section_id in str(options_section_id):
            print(f"\n\nYou have selected {section_id}\n\n")
            break
        else:
            print("Invalid section id.")

    get_tasks(project_id, section_id)


if __name__ == "__main__":
    main()
