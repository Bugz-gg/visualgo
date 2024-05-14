# PFA 11A - VisuAlgo


```golang
██╗   ██╗██╗███████╗██╗   ██╗ █████╗ ██╗      ██████╗  ██████╗ 
██║   ██║██║██╔════╝██║   ██║██╔══██╗██║     ██╔════╝ ██╔═══██╗
██║   ██║██║███████╗██║   ██║███████║██║     ██║  ███╗██║   ██║
╚██╗ ██╔╝██║╚════██║██║   ██║██╔══██║██║     ██║   ██║██║   ██║
 ╚████╔╝ ██║███████║╚██████╔╝██║  ██║███████╗╚██████╔╝╚██████╔╝
  ╚═══╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ 
```


## Project Overview

This is the repository for PFA 11A - VisuAlgo, a Python project that visualizes algorithms. The project structure and setup instructions are outlined below.

## Project Structure

Write your code in ```src/visualgo/``` and your tst in ```tests/```.

```
project-root/
├── src/
│   └── visualgo/
│       ├── data_structure/
│       ├── flow_control/
│       ├── visu/
│
├── tests/
│   └── test_main.py
│
├── myenv
├── pyproject.toml
├── README.md
├── requirements_dev.txt
├── requirements.txt
├── script.sh
├── setup.cfg
├── setup.py
```

## Getting Started

To set up the project, follow these steps:

1. Create a Python virtual environment:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

2. Install the required packages and make `visualgo` a package:

    ```bash
    pip install -e .
    ```

    Note: If you make changes in `visualgo`, reexecute the command. Also, if you use different packages, update the `requirements.txt` file with the corresponding versions.

### Testing

For testing, you can set up a virtual environment with the development requirements:

```bash
pip install -r ./requirements_dev.txt
```

Run various tests with the following commands:

- **pytest**: Run tests and measure coverage
    ```bash
    pytest
    ```

- **flake**: Check for code style issues
    ```bash
    flake
    ```

- **mypy**: Type checking
    ```bash
    mypy
    ```

### Documentation

In order to build the documentation, install the required packages and modules with :
```bash
pip install -r ./requirements_dev.txt
sudo apt-get install python3-sphinx
```


`make html` can then be run to build the documentation in `./build/`. 


### Usage

Activate the virtual environment whenever you want to use the project:

```bash
source myenv/bin/activate 
```

To deactivate the environment, use:

```bash
deactivate
```

This setup ensures a clean and isolated environment for running and testing the project.
