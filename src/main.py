from ChatApplication import *


if __name__ == "__main__":
    DEBUG_MOD = 1
    MODEL = "deepseek-r1:8b"

    app = ChatApplication(DEBUG_MOD, MODEL)
    app.run()
