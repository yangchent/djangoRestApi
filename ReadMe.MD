## deploy in heroku 

- installed waitress  and changed Procfile

- check hero build pack for python

`heroku buildpacks`
`heroku buildpacks:clear`
`heroku buildpacks:add heroku/python`

- problem heroku 20 doesn't support python 3.8.10
- set environment path 
- pip install -r requirements.txt error
    error: subprocess-exited-with-error

    × python setup.py egg_info did not run successfully.
    │ exit code: 1
    ╰─> [25 lines of output]

### solution 
delete requirement.txt and create a new requirement
install django, run server and install all the dependencies and than 
`pip freeze > requirements.txt`


### solution to fix heroku version with python 3.10.5
install heroku cli 
set heroku 22
    `heroku stack:set heroku-22`

### Error: Django admin DoesNotExist at /admin/

- Solution: the sites framework if you only run one site from the project, so the easiest fix would be to remove the following item from your INSTALLED_APPS and the error should go away:

    `django.contrib.sites`

- You can also re-create the missing Site object from shell. Run python manage.py shell and then:

    `from django.contrib.sites.models import Site
    Site.objects.create(pk=1, domain='www.example.com', name='example.com')`