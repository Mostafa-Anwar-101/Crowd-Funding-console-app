from datetime import datetime
from utils import load_json, save_json

PROJECTS_FILE = "projects.json"

def generate_incremental_id():
    projects = load_json(PROJECTS_FILE)
    max_id=0
    if projects:
        for project in projects:
            if project["id"] > max_id:
                max_id=project["id"]
        return max_id + 1
    return 1 

def create_project(user_email):
    projects = load_json(PROJECTS_FILE)

    title = input("Enter project title: ")
    details = input("Enter project details: ")
    target_amount = input("Enter target amount: ")
    
    if not target_amount.isdigit():
        print("Invalid target amount. Must be a number.")
        return

    start_date = input("Enter start date (DD-MM-YYYY): ")
    end_date = input("Enter end date (DD-MM-YYYY): ")

    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")
    if start_date_obj >= end_date_obj:
        print("End date must be after start date.")
        return
    
    project = {
        "id": generate_incremental_id(),
        "title": title,
        "details": details,
        "target_amount": int(target_amount),
        "start_date": start_date,
        "end_date": end_date,
        "owner": user_email
    }
    
    projects.append(project)
    save_json(PROJECTS_FILE, projects)
    print("Project created successfully!")

def view_projects():
    projects = load_json(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return

    for project in projects:
        print(f"\nID: {project["id"]}\nTitle: {project['title']}\nDetails: {project['details']}\nTarget: {project['target_amount']} EGP\nStart: {project['start_date']}\nEnd: {project['end_date']}\nOwner: {project['owner']}\n")

def edit_project(user_email):
    projects = load_json(PROJECTS_FILE)
    project_id = int(input("Enter project ID to edit: "))

    for project in projects:
        if project["id"] == project_id and project["owner"] == user_email:
            project["title"] = input("New title: ") or project["title"]
            project["details"] = input("New details: ") or project["details"]
            target_amount = input("New target amount: ")
            if target_amount.isdigit():
                project["target_amount"] = int(target_amount)

            project["start_date"] = input("New start date (YYYY-MM-DD): ") or project["start_date"]
            project["end_date"] = input("New end date (YYYY-MM-DD): ") or project["end_date"]
            
            save_json(PROJECTS_FILE, projects)
            print("Project updated successfully!")
            return

    print("Project not found or you are not the owner.")

def delete_project(user_email):
    projects = load_json(PROJECTS_FILE)
    project_id = int(input("Enter project ID to delete: "))

    for project in projects:
        if project["id"] == project_id and project["owner"] == user_email:
            projects.remove(project)
            save_json(PROJECTS_FILE, projects)
            print("Project deleted successfully!")
            return

    print("Project not found or you are not the owner.")
