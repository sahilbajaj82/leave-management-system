from app import create_app

configuration = 'default'

app = create_app()

if __name__ == '__main__':
    app.run()
