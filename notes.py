import json
import os

FILE_NAME = "notes.json"

# Load existing notes from file
def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save notes to file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)

# Add a new note
def add_note():
    title = input("📝 Enter note title: ").strip()
    content = input("🗒️ Enter note content: ").strip()
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print("✅ Note saved successfully!")

# View all notes
def view_notes():
    notes = load_notes()
    if not notes:
        print("📭 No notes found.")
        return
    print("\n📚 Your Notes:")
    for i, note in enumerate(notes, start=1):
        print(f"\n{i}. 🏷️ {note['title']}\n   📄 {note['content']}")

# Search notes by title
def search_notes():
    keyword = input("🔍 Enter keyword to search: ").strip().lower()
    notes = load_notes()
    found = [n for n in notes if keyword in n['title'].lower()]
    if found:
        print(f"\n🔎 Found {len(found)} note(s):")
        for note in found:
            print(f"\n🏷️ {note['title']}\n📄 {note['content']}")
    else:
        print("❌ No matching notes found.")

# Delete note by title
def delete_note():
    title = input("🗑️ Enter title of note to delete: ").strip()
    notes = load_notes()
    new_notes = [n for n in notes if n['title'].lower() != title.lower()]
    if len(new_notes) < len(notes):
        save_notes(new_notes)
        print("✅ Note deleted.")
    else:
        print("❌ No note found with that title.")

# Main menu loop
def main():
    while True:
        print("\n🗂️ NOTES MANAGER")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("👋 Exiting Notes Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
