To set up a Python virtual environment and isolate the required packages, follow these steps. This approach ensures a clean and manageable workspace.

### Create and Activate a Virtual Environment

Run the following commands to create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### Install Required Packages

After activating the virtual environment, install the necessary packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Deactivate the Virtual Environment

To deactivate the virtual environment, simply run:

```bash
deactivate
```