from telegram import Bot, InputMediaDocument
import datetime
import pytz
import sys

def main():
    # Periksa apakah argumen yang diperlukan telah diberikan
    if len(sys.argv) < 3:
        print("Penggunaan: python nama_skrip.py <BOT_TOKEN> <CHAT_ID>")
        sys.exit(1)

    # Ambil BOT_TOKEN dan CHAT_ID dari argumen baris perintah
    BOT_TOKEN = sys.argv[1]
    CHAT_ID = sys.argv[2]
    
    current_time = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
    bot = Bot(BOT_TOKEN)
    file_paths = (
        "ss_configs.txt",
        "ssr_configs.txt",    
        "trojan_configs.txt",
        "vlees_configs.txt",
        "vmess_configs.txt",
    )
    # From 2 to 10 items in one media group
    # https://core.telegram.org/bots/api#sendmediagroup
    media_group = list()
    for f in file_paths:
        with open(f, "rb") as fin:
            # Up to 1024 characters.
            # https://core.telegram.org/bots/api#inputmediadocument
            caption = f"Daily Update for subapi: https://api.vmess.free.nf/{f} \n\n Total Accounts: {len(fin.readlines())}\n Updated on: {current_time}"
            # After the len(fin.readlines()) file's current position
            # will be at the end of the file. seek(0) sets the position
            # to the begining of the file so we can read it again during
            # sending.
            fin.seek(0)
            media_group.append(InputMediaDocument(fin, caption=caption))

    bot.send_media_group(CHAT_ID, media=media_group)


if __name__ == "__main__":
    main()
