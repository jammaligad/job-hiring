# job-hiring
Django-based web application as a platform for posting and applying jobs | A final exam django project.

##### Project Members
* Jan Daniel Ko
* Gabriel John S. Pil
* Juan Alphonso D. Maligad
###### Project Deadline
MARCH 4-9, 2019

### Project Checklist
* User - Registration
* User - Login
    * User must be logged in before being able to do any action.
* User - Post a Job
    * Must have imagefield/file in the job post.
    * Must show number of applicants.
    * Posted Jobs can be updated.
    * Posted Jobs can be deleted. (as Boolean field, not deleted from database but only from view.)
    * Posted Jobs are tied to respected Users. (Authentication)
* User - Apply for Job
    * Form for application. (Details, Years of Experience, etc.)
    * Number of applicants are incremented after a User applies for that specific job.
* Bonus
    * Users who posted a job may be able to view the users that applied for that job.