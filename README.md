# wps-repository-configurator



## Target

This is an django admin interface to build json configuration files
that can work with

https://github.com/riesgos/gfz-command-line-tool-repository

Some of the example files can be found here:

- https://github.com/gfzriesgos/quakeledger/blob/master/metadata/quakeledger.json
- https://github.com/gfzriesgos/shakyground/blob/master/metadata/shakyground.json
- https://github.com/gfzriesgos/deus/blob/master/metadata/deus.json

A more explicit definition of the format can be found [here](https://github.com/riesgos/gfz-command-line-tool-repository/blob/master/doc/HowToAddOwnProcess.md#write-the-json-configuration).

## How to start

You can use docker-compose to start the project:

```bash
docker-compose build
docker-compose up
```

To create a super user you must run:

```bash
docker exec -ti wps-repository-configurator bash 
```

and then inside the container:

```
cd project
python3 manage.py createsuperuser
```

With that you can open http://localhost:8000/admin
and log in.

## Admin interface

The admin interface to build the json files via a UI.
Click on the + Add button for the processes to create one.

## Export the files

When you are in the overview page of the processes, you can click on
the `json` link to open a process configuration in the json format.

You can also select one or more configurations in the list & use the `Export json to folder` action.

By default it will put the json files in the configurations subfolder of the project.
