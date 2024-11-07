import json , time

file_name = 'youtube.txt'

def load_data():
    try:
        with open(file_name,'r') as file:
            test =  json.load(file)
            # print(test)
            return test
    except FileNotFoundError:
        print("hyy user ! ,file not found ")
        return []


def save_data_helper(videos):
    with open(file_name,'w') as file:
        json.dump(videos,file)
        


def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index ,video in enumerate(videos , start=1) :
        
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    
    print("\n")
    print("*"*70)

def add_videos(videos):
    name = input("Enter video name: ")
    Time = input("Enter video time: ")
    videos.append({'name':name ,'time':Time})
    save_data_helper(videos)
    print("video Adding.....")
    time.sleep(4)  #for user friendly intervention
    print("video Added !")

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("enter the video No. to update: "))
    if 1 <= index <= len(videos):
        name = input("enter the new video name: ")
        Time = input("enter the new video Time: ")
        videos[index-1] = {'name':name , 'time':Time}
        save_data_helper(videos)
        print("video Description is Updateding....")
        time.sleep(2)  #for user friendly intervention
        print("Updated")

    else: print("invalid index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video No. to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("deleting....")
        time.sleep(2) #for user friendly intervention
    else:
        print("invailid index selected")

def main():


    videos = load_data()

    

    while True :
        print("\n Youtube Manager")
        print("1. List all youtubbe videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _ :
                print("Invalid choice") 
            
# thunder:
if __name__ == "__main__" :
    main() 