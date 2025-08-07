Setup Instructions 
- 1) Install Python

    Download and install Python from: https://www.python.org/downloads/

    During installation, make sure to tick the box that says “Add Python to PATH”

    To check installation, open Command Prompt and type:

    python --version

- 2) Fix PIP if Not Found

    If you see error like 'pip' is not recognized, reinstall Python and make sure “Add to PATH” is ticked.

    Then check:

    pip --version

- 3) Install Required Libraries

In the same folder as your project, open Command Prompt and run:

pip install flask
pip install pycryptodome

These will install Flask (for web server) and PyCryptodome (for AES encryption).
- 4)  Create Project Folder Structure

You can use VS Code or any editor. Create the folder like this:

secure_file_share/
├── app.py
├── templates/
│   └── index.html
└── uploads/
    ├── original/
    ├── encrypted/
    └── decrypted/

- 5) Run Your Project

In Command Prompt, go to your project folder:

cd path\to\secure_file_share

Then run:

After you run this in Command Prompt:

python app.py

You should see something like this:

 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat

This means the Flask server is running successfully on your local machine.
What to do next?

- 6) Open in Browser

After running the command above, open:

http://127.0.0.1:5000
