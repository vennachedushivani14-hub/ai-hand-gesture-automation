import os

print("AI Gesture Control System")
print("1 - Finger Counter")
print("2 - Virtual Mouse")
print("3 - Presentation Controller")
print("4 - Volume Controller")

choice = input("Select module: ")

if choice == "1":
    os.system("py -3.11 finger_counter.py")

elif choice == "2":
    os.system("py -3.11 virtual_mouse.py")

elif choice == "3":
    os.system("py -3.11 gesture_controller.py")

elif choice == "4":
    os.system("py -3.11 gesture_volume.py")

else:
    print("Invalid choice")