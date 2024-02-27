from Quiz.questions import rust_questions, rust_answers

questions = ["one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]


def rust_quiz():
    final_score = 0
    for i in questions:
        print(rust_questions[i])
        a_1 = int(input("Enter your choice: "))
        if a_1 == rust_answers[i]:
            final_score += 1

    print("-" * 50)
    print(f"Your final score for this session is {final_score}")


if __name__ == "__main__":
    rust_quiz()
