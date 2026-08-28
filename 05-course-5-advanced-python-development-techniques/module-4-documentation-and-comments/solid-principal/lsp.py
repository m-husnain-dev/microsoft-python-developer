class Bird:

    def move(self):
        print("Moving around")


class FlyingBird(Bird):

    def fly(self):
        print("Flying in the sky")


class Eagle(FlyingBird):

    pass  # Eagle ud sakta hai


class Penguin(Bird):

    def swim(self):
        print("Swimming in water")  # Penguin ud nahi sakta, sirf swim/move