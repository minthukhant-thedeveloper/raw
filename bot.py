import ftfy
import os
from pyrogram import Client, filters

# Replace with your Telegram bot token
BOT_TOKEN = "6756300061:AAE2ebDyTMtXI6p8xvmLI6Wqya1-6ZPLtK8"

api_id = 7433927
api_hash = "9a54fdf0026773141032074b018cb01e"

app = Client("fmt_charset_bot", api_id=api_id, api_hash=api_hash)


# Handler for private messages
@app.on_message(filters.private & filters.command("charset_fix", prefixes="/"))
def handle_private_messages(client, message):
    # Create a folder for each user using their user ID
    user_folder = str(message.from_user.id)


    # Create user folder if it doesn't exist
    os.makedirs(user_folder, exist_ok=True)
    user_folder_path = f"downloads/{user_folder}/"
    
    file_name = message.document.file_name
    file_id = message.document.file_id

    corrected_file_name = "corrected_" + file_name

    message.reply_text('Processing now, Please wait')

    # Download the file and save it in the user's folder
    file_path = app.download_media(message, file_name=user_folder_path)


    corrected_file_path = os.path.abspath(os.path.join(user_folder_path, corrected_file_name))
    # Open the original and corrected files for reading and writing
    error_file = open(file_path, 'r')
    corrected_file = open(corrected_file_path, 'w')


    # Iterate through each line in the original file, fix it, and write to the corrected file
    lines = error_file.readlines()
    for line in lines:
        fix = ftfy.fix_text(line)
        corrected_file.write(fix)

    # Close the files
    error_file.close()
    corrected_file.close()

    # Send the corrected file back to the user
    app.send_document(
        chat_id=message.chat.id,
        document=corrected_file_path,
        caption="Here is your file"
    )

    # Remove the temporary files
    os.remove(file_path)
    os.remove(corrected_file_path)


@app.on_message(filters.private)
def handle_private_messages(client, message):
    message.reply_text('Welcome to FMT bot. \n send file using /charset_fix command to fix broken charset' )



# Run the application
if __name__ == "__main__":
    app.run()
