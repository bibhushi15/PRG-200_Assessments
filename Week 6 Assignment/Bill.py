# Name: Bibhushi Karki
import random
random.seed(42)
friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750
def split_bill(friends, total):
    return total / len(friends)

def pick_lucky(friends):
    return random.choice(friends)

def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky = pick_lucky(friends)

    # Everyone pays equal share first
    for friend in friends:
        print(f"{friend} pays NPR {share:.2f}")

    lucky_total = share + 50   # lucky person pays extra 50

    print(f"Lucky person: {lucky}")
    print(f"{lucky}'s final amount: NPR {lucky_total:.2f}")

final_summary(friends, total_bill)