class InvalidTelevisionData(Exception):
    """Custom exception for invalid TV data."""
    pass


class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def get_input(self):
        try:
            self.model_no = int(input("Enter model number (max 4 digits): "))
            if self.model_no > 9999:
                raise InvalidTelevisionData("Model number cannot exceed 4 digits!")

            self.screen_size = int(input("Enter screen size in inches (12–70): "))
            if not (12 <= self.screen_size <= 70):
                raise InvalidTelevisionData("Screen size must be between 12 and 70 inches!")

            self.price = float(input("Enter price (0–5000 Rs): "))
            if not (0 <= self.price <= 5000):
                raise InvalidTelevisionData("Price must be between 0 and 5000 Rs!")

        except (ValueError, InvalidTelevisionData) as e:
            print("\n❌ Error:", e)
            print("Setting all values to 0...\n")
            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\n----- Television Details -----")
        print(f"Model Number: {self.model_no}")
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Price: Rs. {self.price}")
        print("------------------------------")


# ------------------ MAIN PROGRAM -------------------
def main():
    tv = Television()
    tv.get_input()
    tv.display()


# Run the program
main()
