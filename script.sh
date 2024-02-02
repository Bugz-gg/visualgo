#!/bin/bash

python3 -m venv myenv2 && source myenv2/bin/activate && pip install -e . && pip install -r ./requirements_dev.txt
