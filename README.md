# flexisaf-django-task
This is the git repo for the small HR software task..

## Prerequisites
-   ``python >= 3.5``
-   ``python3-dev & default-libmysqlclient-dev`` # Debian / Ubuntu
-   Mac Users [follow this link](https://github.com/PyMySQL/mysqlclient-python) to get the prerequisites

## Installation
Open terminal in desired directory

    git clone git@github.com:Paplow/flexisaf-django-task.git
    cd flexisaf-django-task
    pip3 install -r requirements.txt

Then open ``.dbconfig`` environment file and update database details and lastly run

    python3 manage.py collectstatic
    python3 manage.py runserver

Create super user which will manage the staffs

    python3.6 manage.py createsuperuser --email name@domain.com --username name

## How is works
-   Only the super user can create staffs
-   Staffs can then login to update their profile with other required details
-   The super user can browser staff data
-   Search by 'email', 'phone', 'department', 'position'
-   And also filter by 'department' and 'work status'