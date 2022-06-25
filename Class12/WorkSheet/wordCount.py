def wordCount():
    count = len(open("STORY.txt").read().split())
    print("Total number of words inthe file : " count)