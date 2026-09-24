from inspection.camera_mode import run_camera_mode
from inspection.image_mode import run_image_mode


while True:

    print("\n========================")
    print(" Godrej InspectIQ ")
    print("========================")
    print("1. Live Camera")
    print("2. Test Image")
    print("3. Exit")

    choice = input("\nEnter choice : ")

    if choice == "1":

        run_camera_mode()

    elif choice == "2":

        image_path = input(
            "\nImage Path : "
        )

        run_image_mode(image_path)

    elif choice == "3":
        break