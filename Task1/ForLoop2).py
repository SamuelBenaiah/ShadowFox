def main():
    total_jumping_jacks = 100
    per_set = 10
    remaining_jacks = total_jumping_jacks
    sets_completed = 0

    while remaining_jacks > 0:
        sets_completed += 1
        if remaining_jacks >= per_set:
            remaining_jacks -= per_set
        else:
            remaining_jacks = 0

        print(f"Set {sets_completed} completed. {remaining_jacks} jumping jacks remaining.")

        tired_response = input("Are you tired? (yes/no): ").strip().lower()

        if tired_response == "yes" or tired_response == "y":
            skip_remaining = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip_remaining == "yes" or skip_remaining == "y":
                break

    if remaining_jacks == 0:
        print(f"Congratulations! You completed the workout of {total_jumping_jacks} jumping jacks.")
    else:
        print(f"You completed a total of {total_jumping_jacks - remaining_jacks} jumping jacks.")


if __name__ == "__main__":
    main()
