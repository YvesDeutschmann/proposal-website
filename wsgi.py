from index import app

application=app.server

if __name__=='__main__':
   application.run(debug=False)