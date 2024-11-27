import streamlit as st
from github_utils import list_repo_contents, display_file_content
from github import Github

# Set page configuration to wide mode
st.set_page_config(layout="wide")


# Streamlit app
def main():
    st.title("GitHub Repo Explorer")

    # Input field for GitHub repository name
    repo_name = st.text_input("Enter the GitHub repository (e.g., 'username/repo'):")

    if repo_name:
        # Authenticate with GitHub using token from Streamlit secrets
        g = Github(st.secrets["github_token"]["token"])
        repo = g.get_repo(repo_name)
        contents = list_repo_contents(repo)

        # Create two columns for directory structure and file content
        col1, col2 = st.columns([1, 2])

        with col1:
            st.header("Directory Structure")
            # Display directory structure
            for content in contents:
                if content["type"] == "dir":
                    st.write(f"📁 {content['path']}")
                else:
                    if st.button(f"📄 {content['path']}"):
                        st.session_state.selected_file = content["path"]

        with col2:
            st.header("File Content")
            # Display file content if a file is selected
            if "selected_file" in st.session_state:
                display_file_content(repo, st.session_state.selected_file)


if __name__ == "__main__":
    main()
