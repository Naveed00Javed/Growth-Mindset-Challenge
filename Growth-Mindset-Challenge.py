import time

def welcome_message():
    print("\n🌱 Welcome to the Growth Mindset Challenge! 🌱")
    print("Let's build a better version of YOU, step by step!\n")

def set_goal():
    goal = input("🚀 What is your big goal you want to achieve? ")
    return goal

def daily_check_in(goal):
    print(f"\n🗓️ Daily Check-In for your goal: {goal}")
    action = input("✅ What small positive action did you take today? ")
    feeling = input("😊 How do you feel about your progress today? ")
    return action, feeling

def motivational_quote():
    quotes = [
        "🌟 Mistakes are proof that you are trying.",
        "🌟 Progress, not perfection!",
        "🌟 You can do hard things!",
        "🌟 A little progress each day adds up to big results."
    ]
    import random
    return random.choice(quotes)

def main():
    welcome_message()
    goal = set_goal()

    days = int(input("\n📅 How many days do you want to track your growth? "))

    for day in range(1, days + 1):
        print(f"\n=================== Day {day} ===================")
        action, feeling = daily_check_in(goal)
        print("\n💬 Today's Reflection:")
        print(f"- Action Taken: {action}")
        print(f"- Feeling: {feeling}")

        print("\n✨ Motivation for You:")
        print(motivational_quote())

        if day != days:
            input("\nPress Enter to continue to next day...")

    print("\n🎉 Congratulations on completing your Growth Mindset Challenge! Keep growing and glowing! 🌟")

if __name__ == "__main__":
    main()
