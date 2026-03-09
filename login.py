def login(username, password):
      correct_username = "admin"
      correct_password = "1234"
      
      if username == correct_username and password == correct_password:
        return True
      return False
