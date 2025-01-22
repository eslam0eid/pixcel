
# Odoo Project and Employee Modules with REST API

This repository contains Odoo modules to manage projects and employees. It also includes a REST API to fetch employees with their active projects.

## Modules Overview

1. **Project Module**:
   - Manages project details including GitHub repository info, Odoo version, hosting type, and collaborators.
   
2. **Employee Module**:
   - Tracks employee details, including a GitHub account, and allows toggling of active/inactive status.
   - Displays the projects an employee is working on (active/inactive status).

3. **REST API**:
   - A controller to fetch all employees and their active projects via a GET request.

---

## Requirements

- Odoo 16 or later.
- Python 3.x with required dependencies installed.
- PostgreSQL database (default for Odoo).
- Basic knowledge of Odoo development and module installation.

---

## Setup Instructions

### 1. **Install the Modules**

- Clone this repository or copy the module files into your Odoo's `addons` directory.
- Make sure the modules are inside the Odoo `addons` folder:
  
- After placing the modules, restart the Odoo server.

### 2. **Install the Modules in Odoo**

- Go to the Odoo backend (`http://localhost:8069` or your Odoo instance URL).
- Update the app list:
  - Navigate to `Apps` and click on the `Update Apps List`.
- Search for the modules:
  - **Project Module** and **Employee Module** and pixles_task.
- Install both modules by clicking the `Install` button.

### 3. **Configure the Modules**

#### Project Module:
-add fields and page in this model

#### Employee Module:
-add fields and page in this model

---

## Testing the REST API

1. **Start Odoo**:
   - Ensure that your Odoo instance is running.

2. **API Endpoint**:
   - The endpoint for fetching employees with their active projects is:
   
     ```
     GET /api/employees/projects
     ```

3. **Authentication**:
   - The API uses Basic Authentication. Encode the username and password as base64 (e.g., `username:password`).
   
4. **Test API with `curl`**:

   Example using `curl` (replace `<your_odoo_url>` with your Odoo instance URL):

   ```bash
   curl -u username:password http://<your_odoo_url>/api/employees/projects
   ```

5. **Expected Response**:

   - **Success**:

     ```json
     {
       "status": "success",
       "data": [
         {
           "employee_name": "John Doe",
           "active_projects": ["Project A", "Project B"]
         },
         {
           "employee_name": "Jane Smith",
           "active_projects": ["Project C"]
         }
       ]
     }
     ```

   - **Error**:

     ```json
     {
       "status": "error",
       "message": "An error occurred."
     }
     ```




