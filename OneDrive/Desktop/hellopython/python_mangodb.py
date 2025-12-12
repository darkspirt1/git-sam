from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://youtubepy:youtubepy@cluster0.jq5aywp.mongodb.net/")

db = client["ytmanager"]
videos_collection = db["videos"]

print(videos_collection )

def list_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})

def update_video(id, name, time):
    videos_collection.update_one(
        {"_id": id}, {"$set": {"name": name, "time": time}})
    
def delete_video(id):
    videos_collection.delete_one({"_id": id})


def main():
    while True:
        print("\n==============================")
        print("YouTube Manager using MongoDB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case "3":
                id = input("Enter video id to update: ")
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                update_video(id, name, time)
            case "4":
                id = input("Enter video id to delete: ")
                delete_video(id)
            case "5":
                print("Exiting YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()