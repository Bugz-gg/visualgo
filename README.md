# PFA 11A - VisuAlgo


```golang
██╗   ██╗██╗███████╗██╗   ██╗ █████╗ ██╗      ██████╗  ██████╗ 
██║   ██║██║██╔════╝██║   ██║██╔══██╗██║     ██╔════╝ ██╔═══██╗
██║   ██║██║███████╗██║   ██║███████║██║     ██║  ███╗██║   ██║
╚██╗ ██╔╝██║╚════██║██║   ██║██╔══██║██║     ██║   ██║██║   ██║
 ╚████╔╝ ██║███████║╚██████╔╝██║  ██║███████╗╚██████╔╝╚██████╔╝
  ╚═══╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ 
```

## Documentation 
This is a documentation of how to use and also how to extend (at your own risks) the project https://bugz-gg.github.io/visualgo/.

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

## CeCILL Free Software License

The CeCILL Free Software License is a legal document that outlines the terms and conditions for using, modifying, and distributing software. It ensures users' access to the source code, granting them extended rights typical of free software. The license is compliant with French law, providing protection to both users and authors. Users are encouraged to read and understand the terms before using the software. Redistribution is allowed under certain conditions, and users must acknowledge the original authors. The license also addresses liability, warranties, and dispute resolution. Click on [Licence](LICENSE) to have more details or on the website for english speakers [CeCILL Website](http://www.cecill.info/index.en.html).
