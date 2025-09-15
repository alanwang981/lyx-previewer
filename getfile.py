import requests
from frontend import displayError

has_perm = True

# download a file from Google Drive using its file_id and saves it to the path "destination" 
def download_drive_file(file_id, destination):
    URL = "https://drive.google.com/uc?export=download" # base URL for direct Google Drive download

    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True) # request to start the download

    # check if script can access file
    content_type = response.headers.get('Content-Type', '')
    if 'text/html' in content_type.lower():
        displayError("The file must have unrestricted general access. Please relaunch the program.")
        global has_perm 
        has_perm = False

    save_response_content(response, destination) # save the downloaded content to the destination file

# save the file content from the HTTP response to a local file in chunks.
def save_response_content(response, destination, chunk_size=32768):
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:  # filter out keep-alive chunks
                f.write(chunk)