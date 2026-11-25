# SmartFind – Frontend & Backend Contract

**Project:** SmartFind – College Lost & Found Portal  
**Framework:** Python Django MVT  
**Database:** SQLite  
**Frontend:** HTML, CSS, Bootstrap 5, JavaScript  
**Team:** Ajay and Arjun

## 1. Team responsibilities

### Ajay – Backend
- Django models
- Django views
- Django forms
- Authentication
- Database operations
- Validation and permissions
- Smart matching algorithm

### Arjun – Frontend
- HTML templates
- CSS and Bootstrap
- Navigation and layouts
- Registration and login pages
- Student and staff dashboards
- Item cards and search interfaces

## 2. User registration

**URL:** `/accounts/register/`  
**Method:** POST

| Field name | Type | Required |
|---|---|---|
| first_name | Text | Yes |
| last_name | Text | Yes |
| username | Text | Yes |
| email | Email | Yes |
| password | Password | Yes |
| confirm_password | Password | Yes |
| role | Select | Yes |

Available roles:
- student
- staff

College Admin accounts will be created through an authorized admin process.

Backend rules:
- Username must be unique.
- Email must be unique.
- Passwords must match.
- Password must be validated securely.
- College email must be verified before account activation.

`confirm_password` is only for validation. It is not stored in the database.

## 3. Login

**URL:** `/accounts/login/`  
**Method:** POST

| Field name | Type | Required |
|---|---|---|
| username | Text | Yes |
| password | Password | Yes |

After successful login, redirect users according to their role.

## 4. Lost item report

**URL:** `/items/report/lost/`  
**Method:** POST

| Field name | Type | Required |
|---|---|---|
| item_name | Text | Yes |
| category | Select | Yes |
| description | Textarea | Yes |
| color | Text | Yes |
| location | Text | Yes |
| item_date | Date | Yes |
| item_image | Image | No |

## 5. Found item report

**URL:** `/items/report/found/`  
**Method:** POST

Use the same fields as the lost item report.

Backend will distinguish reports using `item_type`:
- lost
- found

The frontend does not need to submit `item_type` if the URL already determines it.

## 6. Browse and search items

**URL:** `/items/`  
**Method:** GET

Search parameters:
- search
- category
- color
- location
- item_type

Example:

`/items/?search=wallet&item_type=found`

## 7. Item details

**URL:** `/items/<id>/`  
**Method:** GET

Display:
- Item name
- Category
- Description
- Color
- Location
- Date
- Image
- Report status

Private ownership verification information must never be displayed publicly.

## 8. Ownership claim

**URL:** `/claims/submit/<item_id>/`  
**Method:** POST

| Field name | Type | Required |
|---|---|---|
| ownership_proof | Textarea | Yes |
| additional_details | Textarea | No |

Backend rules:
- Only authenticated users can submit claims.
- Users cannot claim their own found reports.
- Claims must be reviewed by authorized staff/admin.
- Approval or rejection must be recorded.

## 9. Common Django URL names

| Feature | URL name |
|---|---|
| Register | register |
| Login | login |
| Logout | logout |
| Home | home |
| Item list | item_list |
| Lost report | report_lost |
| Found report | report_found |
| Item details | item_detail |
| Submit claim | submit_claim |
| Student dashboard | student_dashboard |
| Staff dashboard | staff_dashboard |

## 10. Frontend and backend rules

1. Both developers must use the exact agreed field names.
2. All POST forms must include Django CSRF protection.
3. Image upload forms must use `enctype="multipart/form-data"`.
4. Dates must be submitted in `YYYY-MM-DD` format.
5. Django views will handle validation and database operations.
6. Django messages will display success and error notifications.
7. Frontend must not directly access the database.
8. Users must only access pages permitted by their roles.
9. Private ownership details must not be exposed publicly.
10. Any change to fields or URLs must be discussed by both developers first.

## 11. GitHub workflow

- Ajay works on the `ajay` branch.
- Arjun works on the `arjun` branch.
- `main` contains the reviewed, stable project.
- Features are merged through Pull Requests.

## 12. Development order

1. Project setup
2. Authentication
3. Item management
4. Frontend integration
5. Smart matching
6. Ownership claims
7. Dashboards
8. Testing
9. Advanced features
10. Deployment

**Project tagline:** SmartFind – Lost it? Let's find it!