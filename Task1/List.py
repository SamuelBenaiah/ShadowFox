# Initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members in the Justice League
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

# 2. Add Batgirl and Nightwing to the list
justice_league.extend(["Batgirl", "Nightwing"])
print("Justice League after adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning of the list
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after moving Wonder Woman to the beginning:", justice_league)

# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("Justice League after moving Green Lantern between Aquaman and Flash:", justice_league)

# 5. Replace the existing list with the new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Justice League after replacing with new members:", justice_league)

# 6. Sort the Justice League alphabetically
justice_league.sort()
print("Justice League after sorting alphabetically:", justice_league)

# Determine the new leader
new_leader = justice_league[0]
print("New leader of the Justice League:", new_leader)
