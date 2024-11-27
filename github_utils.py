import streamlit as st


# Function to list files and folders in a GitHub repository
def list_repo_contents(repo, path=""):
    """
    Recursively lists files and folders in a GitHub repository.

    Args:
        repo: GitHub repository object.
        path: Path within the repository to start listing from.

    Returns:
        List of dictionaries containing file and folder information.
    """
    contents = repo.get_contents(path)
    files = []
    for content in contents:
        if content.type == "dir":
            files.append({"type": "dir", "path": content.path})
            # Recursively list directory contents
            files.extend(list_repo_contents(repo, content.path))
        else:
            files.append({"type": "file", "path": content.path})
    return files


# Function to display file content
def display_file_content(repo, file_path):
    """
    Displays the content of a file from a GitHub repository.

    Args:
        repo: GitHub repository object.
        file_path: Path of the file within the repository.
    """
    file_content = repo.get_contents(file_path).decoded_content.decode()
    file_extension = file_path.split(".")[-1]
    # Display content based on file extension
    if file_extension in ["py", "js", "html", "css", "java", "cpp"]:
        st.code(file_content, language=file_extension)
    elif file_extension in ["md", "txt"]:
        st.text(file_content)
    else:
        st.write(file_content)
