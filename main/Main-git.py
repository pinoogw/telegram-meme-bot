import botogram
import hashlib
import os
import time
import re
import random
import argparse
import sys  
from instabot import Bot

bot = botogram.create("your token")


def loadList(file, type):
    if type == "int":
        with open(file, "r") as file:
            list = [int(line.rstrip("\n")) for line in file]
    else:
        with open(file, "r") as file:
            list = [line.rstrip("\n") for line in file]
    return list

def writeList(file, list):
    with open(file, "w+") as file:
        for item in list:
            file.write(str(item) + "\n")

def loadVar(file):
    with open(file, "r") as file:
        var = str(file.read()).rstrip("\n")
    return var

def writeVar(file, var):
    with open(file, "w+") as file:
        file.write(var)

#this 4 fuction are for use logga command made by pippognetow


@bot.command("Logga") #log in your private channel all new user in a channel and all message 
def Logga(chat, message):
    if chat.type  in ("group", "supergroup"): #if is group or supergroup
        return #dont
    else:
        muteArya = loadVar("logga.txt") #if is in a privatechat
        if message.sender.id == id: #your id
            if muteArya == "disable": #if is disabe
                muteArya = "active"
                writeVar("logga.txt", muteArya) #active
                chat.send("attivo")
            else:
                muteArya = "disable" #if is active
                writeVar("logga.txt", muteArya) #disable
                chat.send("disattivo")

@bot.message_contains("#suggerimento") #to suggest new function
def suggest(chat,bot,message):
    bot.chat(idchannel).send("@"+message.sender.username + " ha inviato questa nuova feature " + str(message.text))

@bot.command("stats") #see bot stats
def stats(chat,message):
    if message.sender.id ==id: #your id 
        x=open("arrivo.txt","r")
        f=x.readline()
        x.close()
        num_lines = sum(1 for line in open('log-in.txt'))
        chat.send("il bot ha " + str(f)+ " memi "+"ha " + str(num_lines)+ " utenti") #number meme and number user
    else:
        x=open("arrivo.txt","r")
        f=x.readline()
        x.close()
        chat.send("il bot ha " + str(f)+  " memi ") #if is not you only number of meme 
@bot.process_message
def gruppi_furbetti(chat,message): #make sure in group are login
    if chat.type  in ("group", "supergroup"):
        loggare = loadVar("Logga.txt")
        if loggare == "active":
            bot.chat(idchannel).send("nuovo messaggio da " +str(chat.id) + " da " + message.sender.name + "il messaggio = \n" + message.text) #spy message only if logga is active
        with open('log-in.txt') as file:
            f = file.read()
            if f is None:
                pass
            if str(chat.id) in f:
                pass
            else:
                chat.send("attenzione usare il comando /newgroup per registrarsi")



@bot.command("newgroup")
def newgroup(chat,message,bot): #add group
    if message.sender not in chat.admins: #only if is admin
        message.reply("accesso negato perchè non sei admin!")
        return
    else:
        with open('log-in.txt') as file:
            f = file.read()
            if f is None:
                pass
            if str(chat.id) in f:
                chat.send("sei già loggato") #you already log
            else: #login
                log=open("log-in.txt","a")
                log_in=log.write("\n"+str(chat.id))
                log.close()
                bot.chat(idchannel).send("nuovo gruppo rilevato "+"\n"+"il chat id è "+str(chat.id)+"\n"+"<b>"+"il nome è ""</b>" + str(chat.name)+"\n"+"username è "+  str(chat.username) +"\n"+ "la descrizione è " +str(chat.description)+"\n"+ "il link ddi invito è " +str(chat.invite_link)+"\n"+"i membri della chat  sono "+str(chat.members_count),syntax="html")
                chat.send("loggato con successo")
@bot.process_message
def process_message(chat, message): #new user
    loggare = loadVar("Logga.txt")
    if loggare == "active": #if log is active log new user
        if message.new_chat_member:
            chat.send("Hello "+str(message.sender.id))
            bot.chat(-idchannel).send("la chat " + str(chat.id) + " ha un nuovo utente " + str(message.sender.id))
            with open('ban.txt') as file:
                f = file.read()
                if f is None:
                    pass
                if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
                    chat.send("utente pericoloso rilevato")
                    try:
                        chat.ban(message.sender.id)
                    except:
                        chat.send("non posso bannare fammi admin per bannare gli utenti malevoli")
        else:
            if message.new_chat_member:
                chat.send("Hello "+str(message.sender.id))
                with open('ban.txt') as file:
                    f = file.read()
                    if f is None:
                        pass
                    if str(message.sender.id) in f:
                        chat.send("utente pericoloso rilevato")
                        try:
                            chat.ban(message.sender.id)
                        except:
                            chat.send("non posso bannare fammi admin per bannare gli utenti malevoli")

        
@bot.command("group")
def group(chat,message,bot):
    chat.send("il chat id è " + str(chat.id)) #get chatid of group


@bot.command("addgroup") #add notify for group
def addgroup(chat,message,bot):
    x=open("notifiche.txt","a")
    f=x.write("\n"+str(chat.id))
    x.close()
    chat.send("notifiche attivate")


@bot.command("deletegroup") #no notify for group
def deletegroup(chat,message,bot):
    """UNsubscribe to get every 60 minuts a random immagine"""
    with open("notifiche.txt", "r") as f:
        lines = f.readlines()
    with open("notifiche.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(chat.id):
                f.write(line)
                chat.send("notifiche disattivate")


@bot.command("ping") #test if bot is online
def ping(chat,message):
    start_time = time.time()
    chat.send("--- %s seconds ---" % (time.time() - start_time))


@bot.command("manutenzione") #say all user bot is under maintenance
def manutenzione(chat,message):
     if message.sender.id == id: #your id
        ida=0
        num_lines = sum(1 for line in open('log-in.txt'))
        while num_lines>ida:
            open_file=open('log-in.txt','r')
            file_lines=open_file.readlines()
            file = file_lines[ida].strip()  # First Line
            if file is None:
                pass
            else:
                bot.chat(file).send("il bot è in manutenzione")
            ida=ida+1


@bot.process_message #add tags for your post
def tags(chat,message):
    if chat.type  in ("group", "supergroup"):
        return
    else:
        if message.sender.id == id:#your id
            try:
                if message.text:
                    x=open("tags.txt","w")
                    f=x.write(str(message.text))
                    x.close()
                    chat.send("nuovo tag salvato riepilogo " + str(message.text),syntax="html")
                    chat.send("if you use pubblicita and for that you lose your old post use fuction search of telegram")

            except:
                chat.send("errore")


@bot.command("tags") #see your tag
def savetags(chat,message):
    if message.sender.id == id:#your id
        x=open("tags.txt","r")
        f=x.readline()
        x.close()
        chat.send(str(f),syntax="html")


@bot.command("eliminaphoto") #delete all your ig photo
def eliminaphoto(chat,message):
    if message.sender.id==id:#your id
        btns = botogram.Buttons()
        btns[0].callback("✔️", "elimina")
        btns[1].callback("❎","nonelimina")
        chat.send("sei prorio sicuro di voler eliminare tutti i post",attach=btns)


@bot.callback("elimina") #delete botton
def elimina(query, chat, message):
    insta=Bot()
    insta.login(username="your username",password="yor password")
    medias = insta.get_total_user_medias(insta.user_id)
    insta.delete_medias(medias)
    query.notify("eliminato",alert=True)
    message.delete()


@bot.callback("nonelimina")#dont delete photo
def nonelimina(query, chat, message):
    query.notify("non eliminato",alert=True)
    message.delete()
@bot.command("info")
def info(chat,message):
    chat.send("👨‍💻dev by @ilsindacodiLignano")
    chat.send("💡for suggest write #suggerimento + your suggest")
    chat.send("this bot actualy support add")
    chat.send("https://github.com/Abissues/telegram-meme-bot")


@bot.command("start") #login
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


@bot.message_contains("pubblicità")#danger if you use this you lose your old tags
def pubblicita(chat,message):#spam ad 
    if message.sender.id == id:#your id
        ida=0
        num_lines = sum(1 for line in open('log-in.txt'))
        while num_lines>ida:
            open_file=open('log-in.txt','r')
            file_lines=open_file.readlines()
            file = file_lines[ida].strip()  # First Line
            if file is None:
                pass
            else:
                try:
                    bot.chat(file).send(message.text)
                except botogram.ChatUnavailableError as e:
                    bot.chat(idchannel).send("Can't send messages to %s (reason: %s)" %
                    (e.chat_id, e.reason))
            ida=ida+1

@bot.command("img") #get a random imagine
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


@bot.process_message
def main(chat, message): #add photo
    if message.photo:
        message.photo.save("PINO"+".png")
        x=open("accettato.txt","w+")
        f=x.write(str(message.sender.id))
        x.close()
        chat.send("send",reply_to=message.id)
        md5 = hashlib.md5()
        with open("PINO.png", "rb") as thefile:
            buf = thefile.read()
            md5.update(buf)
        with open('database.txt') as file:
            contents = file.read()
            if md5.hexdigest() in contents:
                chat.send("è gia nel database",reply_to=message.id)
            else:
                btns = botogram.Buttons()
                btns[0].callback("✔️", "conferma")
                btns[1].callback("❎","nega")
                btns[1].callback("post","posta")
                btns[1].callback("🚫","ban")
                bot.chat(idchannel).send_photo("PINO.png",caption=("@"+str(message.sender.username)),syntax="html",attach=btns,notify=True)

@bot.callback("posta") #post your photo
def posta(query, chat, message):
    message.photo.save(message.photo.file_id+".png")
    btns = botogram.Buttons()
    btns[0].callback("✔️", "conferma")
    d=open("arrivo.txt","r")
    f=d.readline()
    f=int(f)
    d.close()
    aggiunta=f+1
    bot.chat(idchannel).set_description("ci sono " + str(aggiunta)+ " memi ")
    g=open("arrivo.txt","w")
    k=g.write(str(aggiunta))
    new="random"+str(aggiunta)+".jpg"
    os.rename(str(message.photo.file_id)+".png",new)
    g.close()
    message.delete()
    h=open("accettato.txt","r")
    j=h.readline()
    j=int(j)
    h.close()
    x=open("tags.txt","r")
    f=x.readline()
    x.close()
    insta=Bot()
    insta.login(username="username",password="password")
    insta.upload_photo(new,caption=f)
    try:
        os.rename(new+".REMOVE_ME",new)#save the file 
        bot.chat(j).send("il tuo meme è stato postato grazie per l'aiuto")
        md5 = hashlib.md5()
        with open(new, "rb") as thefile:
            buf = thefile.read()
            md5.update(buf)
            x=open("database.txt","a")
            f=x.write(str(md5.hexdigest())+"\n")
            x.close()
    except:
        bot.chat(idchannel).send("il formato dell'immagine non è adatto")


def conferma(query, chat, message): #add to database but dont post photo
    message.photo.save(message.photo.file_id+".png")
    btns = botogram.Buttons()
    btns[0].callback("✔️", "conferma")
    md5 = hashlib.md5()
    with open(str(message.photo.file_id)+".png", "rb") as thefile:
        buf = thefile.read()
        md5.update(buf)
    x=open("database.txt","a")
    f=x.write(str(md5.hexdigest())+"\n")
    x.close()
    d=open("arrivo.txt","r")
    f=d.readline()
    f=int(f)
    d.close()
    aggiunta=f+1
    bot.chat(idchannel).set_description("ci sono " + str(aggiunta)+ " memi ")
    g=open("arrivo.txt","w")
    k=g.write(str(aggiunta))
    new="random"+str(aggiunta)+".jpg"
    os.rename(str(message.photo.file_id)+".png",new)
    g.close()
    message.delete()
    h=open("accettato.txt","r")
    j=h.readline()
    j=int(j)
    bot.chat(j).send("il tuo meme è stato accettato")
    h.close()
    

@bot.callback("ban") #ban user
def ban(query,message,chat):
    message.photo.save(message.photo.file_id+".png")
    btns= botogram.Buttons()
    btns[2].callback("🚫","ban")
    h=open("accettato.txt","r")
    j=h.readline()
    h.close()
    with open("ban.txt","a") as bannare:
        bannare.write(j+"\n")
        bannare.close()
    message.delete()

@bot.callback("nega") #dont add this img to database
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

@bot.command("notifiche") #get photo evey 60 minutes
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


@bot.command("UNnotifiche") #stop get photo every hour
def UNnotifiche(chat,message,bot):
    """UNsubscribe to get every 60 minuts a random immagine"""
    with open("notifiche.txt", "r") as f:
        lines = f.readlines()
    with open("notifiche.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(message.sender.id):
                f.write(line)
                chat.send("notifiche disattivate")


@bot.timer(3600) #spam every hour a photo
def cleangiorno(bot):
    d=open("arrivo.txt","r")
    f=d.readline()
    f=int(f)
    d.close()
    x=random.randint(1,f)
    foto_giorno="random"+str(x)+".jpg"
    ida=0
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
