from view.main_app import MainApplication
import sys


if __name__ == "__main__":
    main_application = MainApplication(sys.argv)
    print('starting app')
    sys.exit(main_application.exec())
    