from datetime import datetime
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
message = f"{timestamp} - Script was run.\n"
with open('C:/Users/premj/OneDrive/Desktop/example2.txt', 'a') as file:
    file.write(message)
