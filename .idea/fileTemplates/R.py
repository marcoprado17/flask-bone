#parse("header.py")

class ${UPPER_NAME}Resources:
    def __init__(self):
        self.string = self.Strings()
        self.id = self.Ids()

    class Strings:
        def __init__(self):
            self.example = "example"

    class Ids:
        def __init__(self):
            self.example = "example"


R = ${UPPER_NAME}Resources()
${LOWER_NAME}_R = ${UPPER_NAME}Resources()