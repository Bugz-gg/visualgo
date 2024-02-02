#!/bin/sh

python3 -m venv myenv
source myenv/bin/activate
pip install -e .
pip install -r ./requirements_dev.txt
deactivate && pip install -r ./requirements_dev.txt # Cette ligne est la pour éviter les porblème avec Pytest.
