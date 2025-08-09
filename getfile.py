import requests

# Downloads a file from Google Drive using its file_id and saves it to the path "destination" 
def download_drive_file(file_id, destination):
    URL = "https://drive.google.com/uc?export=download" # Base URL for direct Google Drive download

    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True) # First request to start the download

    save_response_content(response, destination) # Save the downloaded content to the destination file

# Saves the file content from the HTTP response to a local file in chunks.
def save_response_content(response, destination, chunk_size=32768):
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:  # filter out keep-alive chunks
                f.write(chunk)
