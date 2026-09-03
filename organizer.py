import os
import shutil
import sqlite3
from datetime import datetime
from config import FILE_CATEGORIES


APP_NAME = "Smart File Organizer"
VERSION = "1.0"

print(f"===== {APP_NAME} v{VERSION} =====")


def show_current_folder():
    print("Current folder:")
    print(os.getcwd())


def scan_files():
    print("\nFiles and folders:")

    all_items = os.listdir("Input")

    items = []

    for item in all_items:
        file_path = os.path.join("Input", item)

        if os.path.isfile(file_path):
            items.append(item)

    for item in items:
        print(item)

    return items


def check_items(items):
    print("\nChecking items:")

    for item in items:
        if os.path.isfile(os.path.join("Input", item)):
            print(item, "→ File")
        else:
            print(item, "→ Folder")


def identify_file_types(items):
    print("\nFile types:")

    for item in items:
        for extension, category in FILE_CATEGORIES.items():
            if item.lower().endswith(extension):
                print(item, "→", category)
                break


def create_folders():
    print("\nCreating folders:")

    folders = list(set(FILE_CATEGORIES.values()))

    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(folder, "→ Created")
        else:
            print(folder, "→ Already exists")


def setup_database():
    connection = sqlite3.connect("organizer.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        action TEXT,
        category TEXT,
        timestamp TEXT
    )
    """)

    connection.commit()
    connection.close()


def log_activity(message, action, category, file_name):
    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    with open("organizer.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")

    connection = sqlite3.connect("organizer.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO file_history (file_name, action, category, timestamp)
    VALUES (?, ?, ?, ?)
    """, (file_name, action, category, timestamp))

    connection.commit()
    connection.close()


def get_unique_filename(folder, file_name):
    name, extension = os.path.splitext(file_name)

    counter = 1
    new_name = file_name

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{extension}"
        counter += 1

    return new_name


def organize_files(items):
    print("\nOrganizing files:")

    moved_count = 0
    error_count = 0
    category_counts = {}

    for item in items:

        for extension, folder in FILE_CATEGORIES.items():

            if item.lower().endswith(extension):

                source = os.path.join("Input", item)
                destination = os.path.join(folder, item)

                try:

                    if os.path.exists(destination):
                        new_name = get_unique_filename(folder, item)
                        destination = os.path.join(folder, new_name)

                        shutil.move(source, destination)

                        print(item, "→", new_name)

                        log_activity(
                            f"{item} renamed to {new_name} and moved to {folder}",
                            "RENAMED",
                            folder,
                            new_name
                        )

                        moved_count += 1

                        category_counts[folder] = (
                            category_counts.get(folder, 0) + 1
                        )

                    else:
                        shutil.move(source, destination)

                        print(item, "→", folder)

                        log_activity(
                            f"{item} moved to {folder}",
                            "MOVED",
                            folder,
                            item
                        )

                        moved_count += 1

                        category_counts[folder] = (
                            category_counts.get(folder, 0) + 1
                        )

                except Exception as e:
                    print("Error moving", item, ":", e)

                    log_activity(
                        f"Error moving {item}: {e}",
                        "ERROR",
                        folder,
                        item
                    )

                    error_count += 1

                break

    print("\n===== ORGANIZATION SUMMARY =====")
    print("Files moved:", moved_count)
    print("Errors:", error_count)

    print("\nCategory Summary:")

    for category, count in category_counts.items():
        print(category, ":", count)


def main():
    setup_database()

    show_current_folder()

    items = scan_files()

    check_items(items)

    identify_file_types(items)

    create_folders()

    organize_files(items)


if __name__ == "__main__":
    main()