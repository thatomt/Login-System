def login(username, password):
      correct_username = "admin"
      correct_password = "1234"
      
      if username == correct_username and password == correct_password:
        return True
      return False

while True: 
  user = input("Enter username: ")
  pwd = input("Enter password: ")

  if login(user, pwd):
      print("Login successful!")
      break
  else: 
      print("Login failed.") 