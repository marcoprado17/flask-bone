#parse("header.py")


class ${UPPER_NAME}Resources:
    def __init__(self):
        self.string = self.__Strings()
        self.id = self.__Ids()

    class __Strings:
        def __init__(self):
            self.example = "example"

    class __Ids:
        def __init__(self):
            self.example = "example"
            
R = ${UPPER_NAME}Resources()
${LOWER_NAME}_R = ${UPPER_NAME}Resources()
