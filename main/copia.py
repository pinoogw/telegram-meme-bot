import botogram
import hashlib
import os
import time
import re
import random



bot = botogram.create("your api token")

@bot.message_contains("#suggerimento")#command for user who want a new features on bot
def suggest(chat,bot,message):
    bot.chat("your channel").send("@"+message.sender.username + " send new  feature " + str(message.text))

@bot.command("info")
def info(chat,message):
    chat.send("👨‍💻dev by @ilsindacodiLignano")
    chat.send("💡for suggest write #suggerimento + your suggest")
    chat.send("this bot actualy support add")
@bot.command("start")#command for log-in on your bot
def start(chat,message):
    with open('log-in.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f:
            chat.send("sei già loggato")
        else:
            log=open("log-in.txt","a")
            log_in=log.write("\n"+str(message.sender.id))
            log.close()
            chat.send("loggato con successo")
@bot.message_contains("pubblicità") #spam add
def pubblicita(chat,message):
    if message.sender.id == your telegram_id:
        ida=1
        num_lines = sum(1 for line in open('log-in.txt'))
        while num_lines>ida:
            open_file=open('log-in.txt','r')
            file_lines=open_file.readlines()
            file = file_lines[ida].strip()  # First Line
            if file is None:
                pass
            else:
                bot.chat(file).send(message.text)
            ida=ida+1

@bot.command("img")#recive new meme
def play(chat,message):
    """get an immage"""
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f:
            chat.send("sei stato bannato")
        else:
            d=open("arrivo.txt","r")
            f=d.readline()
            f=int(f)
            d.close()
            x=random.randint(1,f)
            chat.send_photo("random"+str(x)+".jpg",caption="@programmer_memebot",syntax="html")
@bot.process_message #send meme for user
def main(chat, message):
    if message.photo:
        message.photo.save("PINO"+".png") #last photo in backup
        x=open("accettato.txt","w+") #save sender id
        f=x.write(str(message.sender.id))
        x.close()
        chat.send("send",reply_to=message.id)
        md5 = hashlib.md5() #calcolate md5 of file
        with open("PINO.png", "rb") as thefile:
            buf = thefile.read()
            md5.update(buf)
        with open('database.txt') as file:
            contents = file.read()
            if md5.hexdigest() in contents: verify is md5 is on database
                chat.send("è gia nel database",reply_to=message.id) #is on database 
            else:
                btns = botogram.Buttons() #create botton 
                btns[0].callback("✔️", "conferma")
                btns[1].callback("❎","nega")
                btns[2].callback("🚫","ban")
                bot.chat(your channel).send_photo("PINO.png",caption=("@"+str(message.sender.username)),syntax="html",attach=btns,notify=True)


@bot.callback("conferma") #immagi is ok
def conferma(query, chat, message):
    message.photo.save(message.photo.file_id+".png") #save immagine
    btns = botogram.Buttons()
    btns[0].callback("✔️", "conferma")
    md5 = hashlib.md5()
    with open(str(message.photo.file_id)+".png", "rb") as thefile:
        buf = thefile.read()
        md5.update(buf)
    x=open("database.txt","a") 
    f=x.write(str(md5.hexdigest())+"\n")#write md5 on database
    x.close()
    d=open("arrivo.txt","r")
    f=d.readline()
    f=int(f)
    d.close()
    aggiunta=f+1
    bot.chat(your channel).set_description("ci sono " + str(aggiunta)+ " memi ") #change description
    g=open("arrivo.txt","w")
    k=g.write(str(aggiunta))
    new="random"+str(aggiunta)+".jpg" #rename file
    os.rename(str(message.photo.file_id)+".png",new)
    g.close()
    message.delete()
    h=open("accettato.txt","r")
    j=h.readline()
    j=int(j)
    bot.chat(j).send("il tuo meme è stato accettato") #thanks sender users
    h.close()

@bot.callback("ban") #ban user who send a malicius img
def ban(query,message,chat):
    btns= botogram.Buttons()
    btns[2].callback("🚫","ban")
    h=open("accettato.txt","r")
    j=h.readline()
    h.close()
    with open("ban.txt","a") as bannare:
        bannare.write(j+"\n")
        bannare.close()

@bot.callback("nega") #dont accept user immagine
def nega(query, chat, message):
    btns = botogram.Buttons()
    btns[0].callback("❎", "nega")
    query.notify("meme negato ",alert=True)
    message.delete()
    h=open("accettato.txt","r")
    j=h.readline()
    j=int(j)
    bot.chat(j).send("bro hai postato cringe bro ")
    h.close()

@bot.command("notifiche") #ability hour post
def notifiche(chat,message,bot):
    """subscribe to get every 6o minuts a random immagine"""
    with open('notifiche.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f:
            chat.send("stai già ricevendo notifiche usa /UNnotifiche per non riceverne più")
        else:
            x=open("notifiche.txt","a")
            f=x.write("\n"+str(message.sender.id))
            x.close()
            chat.send("notifiche attivate")
@bot.command("UNnotifiche") #disable hour post
def UNnotifiche(chat,message,bot):
    """UNsubscribe to get every 60 minuts a random immagine"""
    with open("notifiche.txt", "r") as f:
        lines = f.readlines()
    with open("notifiche.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(message.sender.id):
                f.write(line)
                chat.send("notifiche disattivate")
@bot.timer(3600) #hour post send
def cleangiorno(bot):
    d=open("arrivo.txt","r")
    f=d.readline()
    f=int(f)
    d.close()
    x=random.randint(1,f)
    foto_giorno="random"+str(x)+".jpg"
    ida=1
    num_lines = sum(1 for line in open('notifiche.txt'))
    while num_lines>ida:
        open_file=open('notifiche.txt','r')
        file_lines=open_file.readlines()
        file = file_lines[ida].strip()  # First Line
        if file is None:
            pass
        else:
            bot.chat(file).send_photo(foto_giorno,caption="meme del giorno inviato ⏰")
        ida=ida+1

if __name__ == "__main__":
    bot.run()
