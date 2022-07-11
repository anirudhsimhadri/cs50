def main():
    file = input("File name: ")
    file = file.strip().lower()
    print(check_file_type(file))

def check_file_type(f):
    if ".gif" in f:
        return "image/gif"
    elif ".jpg" in f:
        return "image/jpeg"
    elif ".jpeg" in f:
        return "image/jpeg"
    elif ".png" in f:
        return "image/png"
    elif ".pdf" in f:
        return "application/pdf"
    elif ".txt" in f:
        return "text/plain"
    elif ".zip" in f:
        return "application/zip"
    else:
        return "application/octet-stream"

main()