#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run tests and generate an HTML report
pytest tests/test_ui.py --html=test_report.html

# Print the test results to the console
cat test_report.html