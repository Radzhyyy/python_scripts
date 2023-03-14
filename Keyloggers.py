import keyboard

keys = []

# open file to store keys
with open("keys.txt", "w") as f:
    # record keys until ENTER is pressed
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            if event.name == "enter":
                break
            keys.append(event.name)
            f.write(event.name + "\n")

# replay the recorded keys
keyboard.play(keys)

# print the recorded keys
print(keys)
