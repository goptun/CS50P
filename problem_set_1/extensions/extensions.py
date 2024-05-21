def main():
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    file_name = input("File name: ").strip().lower()

    for extension in media_types:
        if file_name.endswith(extension):
            print(media_types[extension])
            return

    print("application/octet-stream")


if __name__ == "__main__":
    main()
