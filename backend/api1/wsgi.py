from app import create_app

dev = create_app()

if __name__ == '__main__':
    dev.run()