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