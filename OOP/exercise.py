class ekzersaiz:
    def __init__(self, tpoic, course_name,judge_contest_link, problems):
        self.topic = tpoic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


data_list = input().split(" -> ")

exma_list = []

while not data_list[0] == "go go go":
    topic_name = data_list[0]
    course_name = data_list[1]
    judge_contest_link = data_list[2]
    problems = data_list[3].split(", ")

    exercise = ekzersaiz(topic_name, course_name, judge_contest_link, problems)
    exma_list.append(exercise)

    data_list = input().split(" -> ")


for thang in exma_list:
    print(f"Exercises: {thang.topic}")
    print(f"Problems for exercises and homework for the \"{thang.course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {thang.judge_contest_link}")
    counter = 1
    for problem in thang.problems:
        print(f"{counter}. {problem}")
        counter += 1
