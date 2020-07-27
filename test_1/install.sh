source /test_1/venv/bin/activate
# Install pytest
pip install pytest

# Install your project
pip install -e /test_1

# Create requirements.txt
pip freeze > /test_1/requirements.txt


# pytest the code
pytest /test_1/src/tests -v
