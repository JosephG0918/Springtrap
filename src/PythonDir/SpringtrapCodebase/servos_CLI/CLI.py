from servos_package import *

COMMANDS = {
    "Face / Head": [
        "left face",
        "right face",
        "left incline",
        "right incline",
        "center face",
    ],
    "Jaw": [
        "open jaw",
        "close jaw",
        "jaw half closed",
    ],
    "Chin": [
        "chin down",
        "chin up",
        "chin straight",
    ],
    "Eyes": [
        "eyes straight",
        "eyes left",
        "eyes right",
    ],
    "Eyelids": [
        "eye lids normal",
        "eye lids wide",
        "eye lids low",
    ],
    "Special": [
        "dance",
    ],
}

print(
    "=== Servos Command-Line Interface ===\n"
    "Control the servos and animatronic parts using text commands.\n\n"
    "Type '1' to see the list of commands.\n"
    "Press Ctrl+C to exit.\n"
)

while True:
    cmd = input(">>> ")

    match cmd:
        case "1":
            print("Available Commands:\n===================")
            for section, cmds in COMMANDS.items():
                print(f"\n{section}:")
                for cmd in cmds:
                    print(f"  {cmd}")
        case "left face":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                full_left_turn(x)
            except:
                full_left_turn()
        case "right face":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                full_right_turn(x)
            except:
                full_right_turn()
        case "left incline":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                half_left_turn(x)
            except:
                half_left_turn()
        case "right incline":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                half_right_turn(x)
            except:
                half_right_turn()
        case "center face":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                center_turn(x)
            except:
                center_turn()
        case "dance":
            try:
                x = int(input("Rounds // Press enter for default: "))
            except:
                x = 1
            try:
                y = float(input("Step delay (milliseconds) // Press enter for default: "))
                dance(x, y)
            except:
                dance(x)
        case "chin down":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                chin_down(x)
            except:
                chin_down()
        case "chin up":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                chin_up(x)
            except:
                chin_up()
        case "chin straight":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                chin_straight(x)
            except:
                chin_straight()
        case "open jaw":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                open_jaw(x)
            except:
                open_jaw()
        case "close jaw":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                close_jaw(x)
            except:
                close_jaw()
        case "jaw half closed":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                jaw_halfway_closed(x)
            except:
                jaw_halfway_closed()
        case "eyes straight":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                eyes_straight(x)
            except:
                eyes_straight()
        case "eyes left":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                eyes_left(x)
            except:
                eyes_left()
        case "eyes right":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                eyes_right(x)
            except:
                eyes_right()
        case "eye lids normal":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                eye_lids_normal(x)
            except:
                eye_lids_normal()
        case "eye lids wide":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                eye_lids_wide(x)
            except:
                eye_lids_wide()
        case "eye lids low":
            try:
                x = float(input("Step delay (milliseconds) // Press enter for default: "))
                eye_lids_lower(x)
            except:
                eye_lids_lower()
        case _:
            print("Invalid command.")
