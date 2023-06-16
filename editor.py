import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="Editor code",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': 'https://jasserabedrazzek-message-compts-ce1kav.streamlit.app/',
        'About': '# Tools For U, enjoy it and if you encounter any problems, we are here to help.'
    }
)

python_initial = '''print('Hello, World!')'''
requirements_intial = "numpy==1.24.3"
initial_html = """<!DOCTYPE html>
<html>
<head>
  <title>My Web Page</title>
</head>
<body>
  <h1>Welcome to My Web Page</h1>
  <p>This is a paragraph of text.</p>
</body>
</html>
"""

st.title('Welcome to the online editor')
t1, t2 = st.tabs(['Python', 'HTML, CSS, and JavaScript'])

with t1:
    st.title('Python Editor')
    st.header('Create requirements.txt (optional)')
    requirements = st.text_area('requirements.txt', requirements_intial, height=100)
    python_code = st.text_area('Python Code', python_initial, height=450)

    if st.button('Run Code'):
        if python_code != "":
            # Save the Python code to a temporary file
            with open('temp.py', 'w', encoding='utf-8') as file:
                file.write(python_code)

            # Install requirements.txt if provided
            if requirements != "":
                with open('requirements.txt', 'w') as file:
                    file.write(requirements)
                subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

            # Execute the Python code
            process = subprocess.Popen(['python', 'temp.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Display the output
            if stdout:
                st.code(stdout.decode('utf-8'), language='python')
            if stderr:
                st.error(stderr.decode('utf-8'))

            # Remove temporary files
            os.remove('temp.py')
            if os.path.exists('requirements.txt'):
                os.remove('requirements.txt')
with t2:
    st.title("HTML, CSS & JS Editor")
    Html, Css = st.columns(2)
    with Html:
        st.subheader('Create index.html')
        html_code = st.text_area('index.html', initial_html, height=450)

    with Css:
        st.subheader('Create style.css')
        css_code = st.text_area('style.css', height=450)
        st.subheader('Create script.js')
    js_code = st.text_area('script.js', height=450)
    run_button = st.button('Run Code Page')
    full_code = f"{html_code}\n<style>{css_code}</style>\n<script>{js_code}</script>"
    if run_button:
        st.markdown(full_code, unsafe_allow_html=True)
