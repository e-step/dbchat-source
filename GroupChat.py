import mysql.connector

print("GroupChat 1.2.1 plus\n \n")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="channel"
)

mycursor = mydb.cursor()

def add_message():
    name = input("username: ")
    message = input("message: ")

    sql = "INSERT INTO messages (name, message) VALUES (%s, %s)"
    val = (name, message)

    mycursor.execute(sql, val)
    mydb.commit()

    print("your message was saved.")

while True:
    mycursor.execute("SELECT * FROM messages")
    messages = mycursor.fetchall()

    print("saved messages: ")
    for msg in messages:
        print(f"{msg[1]}: {msg[2]}")


    add_message()
