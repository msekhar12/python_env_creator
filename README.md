# python_env_creator
Python script to create a structured python environment

The script `create_project.py` creates a Python project with the following structure:

    <project_location>/<project_name>/src/
                                         |--__init__.py
                                         |--programs
                                            |--__init__.py
                                         |--tests
                                            |--__init__.py
                                            |test_calculator.py
                                         |--examples
                                            |--__init__.py
                                            |--argparse_example.py
                                            |--calculator.py
                                         |--exceptions.py
                                         
    <project_location>/<project_name>/setup.py
    <project_location>/<project_name>/requirements.txt
    <project_location>/<project_name>/venv

    The directory details are given below:
    <project_location>: Location of the project.
                        Defaults to current working directory
                        (or) --location argument (if supplied)

    <project_name>: Name of the project. --name argument

    src: directory that contains the source code of the project

    programs: This is where your programs will reside

    tests: This is where you will create your pytest cases

    examples: Contains some example python scripts.
              Contains calculator.py and argparse_example.py files

    setup.py: contains the following code:
        from setuptools import setup, find_packages
        setup(name='<project_name>', version='1.0', packages=find_packages())

    requirements.txt: Contains the packages. Usually the copy of the requirements
                      you supply as input along with the pytest module.
                      When you release the project, please generate a new
                      requirements file using the following commands:

                      1. Change directory to parent dir of /<project_location>
                      2. Activate your virtual env
                         source venv/bin/activate
                      3. Execute this command:
                         pip freeze > requirements.txt

    venv: Your virtual environment (will be auto generated)


# Program options
    There can be 4 arguments:
    --name or -n:           Project name
    --location or -l:       Directory location where the project will be created
    --requirements or -r:   Path to your requirements file (optional)
    --overwrite or -o:      If you want to overwrite the existing project folder
                            Default is False

# Example - 1
To create a project named `test_1` use the following command:
`./create_project.py -n test_1 -l ./`

The above command will create a folder shown below:
`/test_1`

This folder will have the following files and directories:
`setup.py`
`install.sh`
`venv`
`requirements.txt`
`src`


# Example - 2
To overwrite a project folder, use `-o` option as shown below:
`./create_project.py -n test_1 -l ./ -o`

# Example - 3
Assume that you need to install the following packages inside your project's virtual environment. 
Assume that you received a file named `initial_requirements.txt` from your collegue. 
You can use `-r` option to include these in your project.

`./create_project.py -n test_1 -l ./ -o -r ./initial_requirements.txt`
