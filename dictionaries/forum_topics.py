forum_posts = {}

while True:

    entry = input()

    if entry == "filter":
        break

    entered_data = [el for el in entry.split(" -> ")]
    data_tags = list(map(str,entered_data[1].split(", ")))

    if entered_data[0] in forum_posts:
        for hashtag in data_tags:
            if item not in forum_posts[entered_data[0]]:
                forum_posts[entered_data[0]].append(hashtag)
    else:
        forum_posts[entered_data[0]] = data_tags

filtered_data = {}
get_filter = [el for el in input().split(", ")]

for key,value in forum_posts.items():
    exists = True
    for condition in get_filter:
        if condition not in value:
            exists = False
    if exists:
        filtered_data[key]=value

for item in filtered_data.keys():
    print(f"{item} | {', '.join('#'+str(x) for x in filtered_data[item])}")