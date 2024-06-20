from datetime import datetime, timedelta

# Define the football schedule
football_schedule = [
    {"match": "Denmark vs England", "date": "2024-06-21", "time": "00:00"},
    {"match": "Spain vs Italy", "date": "2024-06-21", "time": "03:00"},
    {"match": "Slovakia vs Ukraine", "date": "2024-06-21", "time": "21:00"},
    {"match": "Poland vs Austria", "date": "2024-06-22", "time": "00:00"},
    {"match": "Netherlands vs France", "date": "2024-06-22", "time": "03:00"},
    {"match": "Georgia vs Czechia", "date": "2024-06-22", "time": "21:00"},
    {"match": "Türkiye vs Portugal", "date": "2024-06-23", "time": "00:00"},
    {"match": "Belgium vs Romania", "date": "2024-06-23", "time": "03:00"},
    {"match": "Slovenia vs Serbia", "date": "2024-06-20", "time": "21:00"},
    {"match": "Switzerland vs. Germany", "date": "2024-06-24", "time": "03:00"},
    {"match": "Scotland vs. Hungary", "date": "2024-06-24", "time": "03:00"},
    {"match": "Albania vs. Spain", "date": "2024-06-25", "time": "03:00"},
    {"match": "Croatia vs. Italy", "date": "2024-06-25", "time": "03:00"},
    {"match": "France vs. Poland", "date": "2024-06-26", "time": "00:00"},
    {"match": "Netherlands vs. Austria", "date": "2024-06-26", "time": "00:00"},
    {"match": "Denmark vs. Serbia", "date": "2024-06-26", "time": "03:00"},
    {"match": "England vs. Slovenia", "date": "2024-06-26", "time": "03:00"},
    {"match": "Slovakia vs. Romania", "date": "2024-06-27", "time": "00:00"},
    {"match": "Ukraine vs. Belgium", "date": "2024-06-27", "time": "00:00"},
    {"match": "Georgia vs. Portugal", "date": "2024-06-27", "time": "03:00"},
    {"match": "Czechia vs. Türkiye", "date": "2024-06-27", "time": "03:00"},

]

# Function to get matches for a specific date and time
def get_matches_for_date(date_str):
    matches = [match for match in football_schedule if match["date"] == date_str]
    return matches

def main():
    while True:
        user_input = input("Enter 'today' or 'tomorrow' to see the list of matches: ").strip().lower()
        
        if user_input in ["today", "tomorrow"]:
            break
        else:
            print("Invalid input. Please enter 'today' or 'tomorrow'.")

    if user_input == "today":
        target_date = datetime.now()
    elif user_input == "tomorrow":
        target_date = datetime.now() + timedelta(days=1)

    # Format the date to match the 'date' field in the schedule
    date_str = target_date.strftime("%Y-%m-%d")
    matches = get_matches_for_date(date_str)

    if matches:
        print(f"Matches for {user_input}:")
        for match in matches:
            print(f"{match['match']} at {match['time']}")
    else:
        print(f"No matches scheduled for {user_input}.")

if __name__ == "__main__":
    main()
