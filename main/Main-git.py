import botogram
import hashlib
import os
import time
import re
import random
import argparse
import sys  
from instabot import Bot
import requests
import datetime
import matplotlib.pyplot as plt
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

@bot.command("help")
def help(chat, message):
    chat.send("usa /menu per la lista comandi, /sintassi per la sintassi dei comandi", reply_to=message.id)

@bot.command("menu")
def menu(chat,message):
    admins=[]
    if str(message.sender.id) in admins:
        btns = botogram.Buttons()
        btns[1].callback("MenuAdmin", "menuAdmin")
        btns[1].callback("Menu", "Menuutenti")
        btns[0].callback("delete","delta")
        chat.send("Benvenuto  " + str(message.sender.username) + " accesso come admin", reply_to=message.id, attach=btns)
    else:
        btns = botogram.Buttons()
        btns[1].callback("Menu", "Menuutenti")
        chat.send("Benvenuto utente " + str(message.sender.name), reply_to=message.id, attach=btns)

@bot.callback("menuAdmin")
def menuAdmin(query,message,chat):
    btns = botogram.Buttons()
    btns[1].callback("GESTIRE UTENTI", "Usercontroll")
    btns[0].callback("delete","delta")
    btns[0].callback("back","BackAdmintoAllmenu")
    message.edit("Click one", attach=btns)



@bot.callback("BackAdmintoAllmenu")
def BackAdmintoAllmenua(query,message,chat):
    admins=[]
    if str(query.sender.id) in admins:
        btns = botogram.Buttons()
        btns[1].callback("MenuAdmin", "menuAdmin")
        btns[1].callback("Menu", "Menuutenti")
        btns[0].callback("delete","delta")
        message.edit("Benvenuto  " + str(query.sender.name) + " accesso come admin", attach=btns)
    else:
        btns = botogram.Buttons()
        btns[1].callback("Menu", "Menuutenti")
        message.edit("Benvenuto  " + str(query.sender.name), attach=btns)


@bot.callback("Ban")
def helpBan(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "BackUsercontrolli")
    btns[0].callback("delete","delta")
    message.edit("spiegazione: banna un utente per id", attach=btns)
@bot.callback("Sban")
def helpSban(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "BackUsercontrolli")
    btns[0].callback("delete","delta")
    message.edit("spiegazione: sbanna un utente per id", attach=btns)

@bot.callback("Lista")
def helpLista(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "BackUsercontrolli")
    btns[0].callback("delete","delta")
    message.edit("spiegazione: lista id bloccati", attach=btns)


@bot.callback("backadmin")
def backadmin(query,chat,message):
    btns = botogram.Buttons()
    btns[1].callback("GESTIRE UTENTI", "Usercontroll")
    btns[0].callback("delete","delta")
    btns[0].callback("back","BackAdmintoAllmenu")
    message.edit("Click one", attach=btns)

@bot.callback("backtooriginalmenu")
def mznshdbdh(query,chat,message):
    admins=[]
    if str(query.sender.id) in admins:
        btns = botogram.Buttons()
        btns[1].callback("MenuAdmin", "menuAdmin")
        btns[1].callback("Menu", "Menuutenti")
        btns[0].callback("delete","delta")
        message.edit("Benvenuto  " + str(query.sender.name) + " accesso come admin", attach=btns)
    else:
        btns = botogram.Buttons()
        btns[1].callback("Menu", "Menuutenti")
        message.edit("Benvenuto  " + str(query.sender.name), attach=btns)

@bot.callback("Usercontroll")
def Usercontrolli(query,message,chat):
    btns = botogram.Buttons()
    btns[3].callback("ban","Ban")
    btns[3].callback("sban","Sban")
    btns[2].callback("lista","Lista")
    btns[0].callback("delete","delta")
    btns[0].callback("back","backadmin")
    message.edit("Click one", attach=btns)


@bot.callback("BackUsercontrolli")
def BackUsercontrolli(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[2].callback("ban","Ban")
    btns[3].callback("sban","Sban")
    btns[3].callback("lista","Lista")
    btns[0].callback("delete","delta")
    btns[0].callback("back","backadmin")
    message.edit("Click one", attach=btns)


@bot.callback("Menuutenti")
def Menutenti(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[1].callback("Giornalieri","Giorno")
    btns[2].callback("registrarsi","reg")
    btns[3].callback("other","Other")
    btns[0].callback("delete","delta")
    btns[0].callback("back","backtooriginalmenu")
    message.edit("Click one", attach=btns)


@bot.callback("Backgiorno")
def Backgiorno(query,chat,message):
    btns = botogram.Buttons()
    btns[0].callback("notifiche","helpNotifiche")
    btns[0].callback("unotifiche","helpUnotifiche")
    btns[1].callback("addgroup","helpAddgroup")
    btns[1].callback("deletegroup","helpDeletegroup")
    btns[2].callback("Go Back", "Backmenu")
    message.edit("Click one", attach=btns)

@bot.callback("Backreg")
def Backreg(query,chat,message):
    btns = botogram.Buttons()
    btns[1].callback("newGroup","helpnewGroup")
    btns[1].callback("login","helpstart")
    btns[0].callback("Go Back", "Backmenu")
    message.edit("Click one", attach=btns)

@bot.callback("Backmenu")
def Backmenu(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[1].callback("Giornalieri","Giorno")
    btns[2].callback("registrarsi","reg")
    btns[3].callback("other","Other")
    btns[0].callback("delete","delta")
    btns[0].callback("back","backtooriginalmenu")
    message.edit("Click one", attach=btns)

@bot.callback("backother")
def backother(query,chat,message):
    btns = botogram.Buttons()
    btns[1].callback("suggerimento", "helpsuggerimento")
    btns[1].callback("stats", "helpstats")
    btns[2].callback("Ping","helpPinga")
    btns[2].callback("tag","helptags")
    btns[3].callback("info","helpinfo")
    btns[3].callback("img","helpImg")
    btns[0].callback("Go Back", "Backmenu")
    message.edit("Click one", attach=btns)
@bot.callback("Giorno")
def Giornol(query,chat,message):
    btns = botogram.Buttons()
    btns[0].callback("notifiche","helpNotifiche")
    btns[0].callback("unotifiche","helpUnotifiche")
    btns[1].callback("addgroup","helpAddgroup")
    btns[1].callback("deletegroup","helpDeletegroup")
    btns[2].callback("Go Back", "Backmenu")
    message.edit("Click one", attach=btns)

@bot.callback("reg")
def regl(query,chat,message):
    btns = botogram.Buttons()
    btns[1].callback("newGroup","helpnewGroup")
    btns[1].callback("login","helpstart")
    btns[0].callback("Go Back", "Backmenu")
    message.edit("Click one", attach=btns)

@bot.callback("Other")
def Otherl(query,chat,message):
    btns = botogram.Buttons()
    btns[1].callback("suggerimento", "helpsuggerimento")
    btns[1].callback("stats", "helpstats")
    btns[2].callback("Ping","helpPinga")
    btns[2].callback("tag","helptags")
    btns[3].callback("info","helpinfo")
    btns[3].callback("img","helpImg")
    btns[0].callback("Go Back", "Backmenu")
    message.edit("Click one", attach=btns)


@bot.callback("helpAddgroup")
def helpaddgroup(query,message,chat):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "Backgiorno")
    message.edit("spiegazione: aggiungi il bot per i memi giornalieri (gruppi)", attach=btns)

@bot.callback("helpDeletegroup")
def helpdeletegroup(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "Backgiorno")
    message.edit("spiegazione: disiscriviti per i memi giornalieri (gruppi)", attach=btns)

@bot.callback("helptags")
def helptag(chat,message,query):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "backother")
    message.edit("spiegazione: vedi i tag", attach=btns)

@bot.callback("helpinfo")
def helpinfo(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "backother")
    message.edit("spiegazione: vedi le info del bot", attach=btns)

@bot.callback("helpImg")
def helpimg(chat,message,query):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "backother")
    message.edit("spiegazione: ricevi una immagine random", attach=btns)

@bot.callback("helpNotifiche")
def helpnotifiche(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "Backgiorno")
    message.edit("spiegazione: iscriviti alle immagini giornalieri (persone singole)", attach=btns)

@bot.callback("helpUnotifiche")
def helpUnnotifiche(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "Backgiorno")
    message.edit("spiegazione: disiscriviti per i memi giornalieri (utenti)", attach=btns)

@bot.callback("helpstart")
def helplogin(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "Backreg")
    message.edit("spiegazione: log-in per gli utenti", attach=btns)

@bot.callback("helpnewGroup")
def helpnewGroup(query,chat,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "Backreg")
    message.edit("spiegazione: log-in per i gruppi", attach=btns)

@bot.callback("helpPinga")
def helpPing(chat,query,message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "backother")
    message.edit("spiegazione: check if bot is on", attach=btns)

@bot.callback("delta")
def delta(query,message,chat):
    message.delete()

@bot.callback("goBack")
def goBack(query, chat, message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[1].callback("Menu", "Menuutenti")
    btns[0].callback("delete","delta")
    message.edit("Click one", attach=btns)

@bot.callback("helpsuggerimento")
def showID(query, chat, message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "backother")
    message.edit("spiegazione: manda /suggerimento + il tuo suggerimento", attach=btns)

@bot.callback("helpstats")
def otherINFOS(query, chat, message):
    mex = message.reply_to_message
    btns = botogram.Buttons()
    btns[0].callback("Go Back", "backother")
    message.edit( "spiegazione:= send bot stats", syntax="html", attach=btns)


@bot.command("Logga") #log in your private channel all new user in a channel and all message 
def Logga(chat, message):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            if chat.type  in ("group", "supergroup"): #if is group or supergroup
                return #dont
            else:
                muteArya = loadVar("logga.txt") #if is in a privatechat
                if message.sender.id == 1: #your id
                    if muteArya == "disable": #if is disabe
                        muteArya = "active"
                        writeVar("logga.txt", muteArya) #active
                        chat.send("attivo")
                    else:
                        muteArya = "disable" #if is active
                        writeVar("logga.txt", muteArya) #disable
                        chat.send("disattivo")

@bot.command("suggerimento") #to suggest new function
def suggest(chat,bot,message,args):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            bot.chat(-100).send("@"+message.sender.username + " ha inviato questa nuova feature " + str(args).strip("['']"))

@bot.command("stats") #see bot stats 
def stats(chat,message):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            if message.sender.id ==5: #your id 
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
            bot.chat(-100).send("nuovo messaggio da " +str(chat.id) + " da " + message.sender.name + " il messaggio = \n" + message.text) #spy message only if logga is active
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
                bot.chat(-100).send("nuovo gruppo rilevato "+"\n"+"il chat id è "+str(chat.id)+"\n"+"<b>"+"il nome è ""</b>" + str(chat.name)+"\n"+"username è "+  str(chat.username) +"\n"+ "la descrizione è " +str(chat.description)+"\n"+ "il link ddi invito è " +str(chat.invite_link)+"\n"+"i membri della chat  sono "+str(chat.members_count),syntax="html")
                chat.send("loggato con successo")

@bot.process_message
def process_message(chat, message): #new user
    loggare = loadVar("Logga.txt")
    if loggare == "active": #if log is active log new user
        if message.new_chat_member:
            chat.send("Hello "+str(message.sender.id))
            bot.chat(-100).send("la chat " + str(chat.id) + " ha un nuovo utente " + str(message.sender.id))
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

        



@bot.command("addgroup") #add notify for group
def addgroup(chat,message,bot):
    """subscribe to get every 60 minuts a random immagine group"""
    with open('notifiche.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(chat.id) in f:
            chat.send("stai già ricevendo notifiche usa /deletegroup per non riceverne più")
        else:
            x=open("notifiche.txt","a")
            f=x.write("\n"+str(chat.id))
            x.close()
            chat.send("notifiche attivate")
    


@bot.command("deletegroup") #no notify for group
def deletegroup(chat,message,bot):
    """UNsubscribe to get every 60 minuts a random immagine group"""
    with open("notifiche.txt", "r") as f:
        lines = f.readlines()
    with open("notifiche.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(chat.id):
                f.write(line)
                chat.send("notifiche disattivate")


@bot.command("ping") #test if bot is online
def ping(chat,message):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            start_time = time.time()
            chat.send("--- %s seconds ---" % (time.time() - start_time))


@bot.command("manuntenzione") #say all user bot is under maintenance
def manutenzione(chat,message):
     if message.sender.id == 50:
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
                    bot.chat(file).send("il bot è in manutenzione")
                except botogram.ChatUnavailableError as e:
                    bot.chat(-100).send("Can't send messages to %s (reason: %s)" %
                    (e.chat_id, e.reason))
            ida=ida+1


@bot.command("newtags") #add tags for your post
def tags(chat,message,args):
    if chat.type  in ("group", "supergroup"):
        return
    else:
        if message.sender.id == 50:
            try:
                ar=" ".join(args)
                x=open("tags.txt","w")
                f=x.write(str(message.text))
                x.close()
                chat.send("nuovo tag salvato riepilogo " + ar,syntax="html")
            except:
                chat.send("errore")


@bot.command("tags") #see your tag
def savetags(chat,message):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            x=open("tags.txt","r")
            f=x.readline()
            x.close()
            chat.send(str(f),syntax="html")

    
@bot.command("info")
def info(chat,message):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            n=random.randint(1,100)
            if n==10:
                message=chat.send("EE scoperto")
                time.sleep(0.2)
                message.edit("fumate")
                time.sleep(0.2)
                message.delete()
            else:
                message=chat.send("👨‍💻dev by @ilsindacodiLignano")
                time.sleep(2)
                message.edit("💡for suggest write /suggerimento + your suggest")
                time.sleep(2)
                message.edit("this bot actualy support add")
                time.sleep(2)
                message.edit("https://github.com/Abissues/telegram-meme-bot")


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


@bot.command("ad")#danger if you use this you lose your old tags
def add(chat,message,args,bot):#spam ad 
    if message.sender.id == 50:
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
                    bot.chat(file).send(str(args).strip("['']"))
                except botogram.ChatUnavailableError as e:
                    bot.chat(-1001).send("Can't send messages to %s (reason: %s)" %
                    (e.chat_id, e.reason))
            ida=ida+1

@bot.command("img") #get a random imagine
def play(chat,message):
    """get an immage"""
    try:
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
    except Exception as e: 
        chat.send("non mandato")
        bot.chat(-100).send("user " + str(message.sender.id) +  " errore "+ e)


@bot.process_message
def main(chat, message): #add photo
    try:
        with open('ban.txt') as file:
            f = file.read()
            if f is None:
                pass
            if str(message.sender.id) in f:
                chat.send("sei stato bannato")
            if chat.type  in ("group", "supergroup"):
                return
            else:
                if message.photo:
                    message.photo.save("PINO"+".png")
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
                            btns[1].callback("🚫","bannato")
                            bot.chat(-100).send_photo("PINO.png",caption=str(message.sender.id),syntax="html",attach=btns,notify=True)
                            chat.send("send",reply_to=message.id)
    except Exception as e: 
        chat.send("non mandato")
        bot.chat(-1001).send("user " + str(message.sender.id) +  " errore "+ e)

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
    bot.chat(-1005).set_description("ci sono " + str(aggiunta)+ " memi ")
    g=open("arrivo.txt","w")
    k=g.write(str(aggiunta))
    new="random"+str(aggiunta)+".jpg"
    os.rename(str(message.photo.file_id)+".png",new)
    g.close()
    message.delete()
    x=open("tags.txt","r")
    f=x.readline()
    x.close()
    insta=Bot()
    insta.login(username="",password="")
    insta.upload_photo(new,caption=f)
    try:
        os.rename(new+".REMOVE_ME",new)#save the file 
        bot.chat(message.caption).send("il tuo meme è stato postato grazie per l'aiuto")
        md5 = hashlib.md5()
        with open(new, "rb") as thefile:
            buf = thefile.read()
            md5.update(buf)
            x=open("database.txt","a")
            f=x.write(str(md5.hexdigest())+"\n")
            x.close()
    except:
        bot.chat(-100).send("il formato dell'immagine non è adatto")

@bot.callback("conferma")
def conferma(query, chat, message,bot): #add to database but dont post photo
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
    bot.chat(-100).set_description("ci sono " + str(aggiunta)+ " memi ")
    g=open("arrivo.txt","w")
    k=g.write(str(aggiunta))
    new="random"+str(aggiunta)+".jpg"
    os.rename(str(message.photo.file_id)+".png",new)
    g.close()
    bot.chat(message.caption).send("il tuo meme è stato accettato")
    message.delete()
    
    

@bot.callback("bannato") #ban user
def bannato(query,message,chat):
    message.photo.save(message.photo.file_id+".png")
    btns= botogram.Buttons()
    btns[2].callback("🚫","ban")
    with open("ban.txt","a") as bannare:
        bannare.write(message.caption+"\n")
        bannare.close()
    message.delete()

@bot.callback("nega") #dont add this img to database
def nega(query, chat, message):
    btns = botogram.Buttons()
    btns[0].callback("❎", "nega")
    query.notify("meme negato ",alert=True)
    message.delete()
    bot.chat(message.caption).send("bro hai postato cringe bro ")

@bot.command("notifiche") #get photo evey 60 minutes
def notifiche(chat,message,bot):
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            if chat.type  in ("group", "supergroup"):
                return
            else:
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
    with open('ban.txt') as file:
        f = file.read()
        if f is None:
            pass
        if str(message.sender.id) in f: #if user is ban in bot and bot is admin ban user
            chat.send("sei stato bannato")
        else:
            if chat.type  in ("group", "supergroup"):
                return
            else:
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
            try:
                bot.chat(file).send_photo(foto_giorno,caption="meme del giorno inviato ⏰")
            except botogram.ChatUnavailableError as e:
                bot.chat(-100).send("Can't send messages to %s (reason: %s)" %
                (e.chat_id, e.reason)) 
            except Exception as e: 
                bot.chat(-100).send( " errore "+ str(e))
        ida=ida+1




@bot.command("BanUsers")
def BanUsers(chat,message,args):
    admins=[""]
    if str(message.sender.id) in admins:
        with open('ban.txt') as file:
            contents = file.read()
            banned = open('ban.txt', 'a')
            banned.write("\n"+str(args).strip("['']"))
            banned.close()

@bot.command("UBanUsers")
def UBanUsers(chat,message,args):
    admins=[""]
    if str(message.sender.id) in admins:
        with open("ban.txt", "r") as f:
            lines = f.readlines()
        with open("ban.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != str(args).strip("['']"):
                    f.write(line)



@bot.command("ListaBanUsers")
def ListaBanUsers(chat,message,args):
    admins=[""]
    if str(message.sender.id) in admins:
        with open("ban.txt", "r") as f:
            lines = f.readlines()
            str1 = " "  
            for ele in lines:  
                str1 = str1 + " " + ele  
        chat.send(str1)  




@bot.command("Listautenti")
def listaUtenti(chat,message,args):
    admins=[""]
    if str(message.sender.id) in admins:
        with open('log-in.txt','r') as f:
            lines = f.readlines()
            str1 = " "  
            for ele in lines:  
                str1 = str1 + " " + ele      
        chat.send(str1,reply_to=message.id,extra=botogram.ForceReply(data={'force_reply':True}))




@bot.command("mandamessaggio")
def mandamessaggio(chat,message,args,bot):
    iduser=args[0]
    args.pop(0)
    ar=" ".join(args)
    x=open("messaggio.txt","r")
    f=x.readline()
    x.close()
    try:
        ar=int(iduser)
    except Exception as e: 
        chat.send("no id ")
        bot.chat(-100).send("user " + str(message.sender.id) +  " errore: \n "+ str(e))
        return
    try:
        bot.chat(iduser).send(ar)
        chat.send("mandato")
    except botogram.ChatUnavailableError as e:
                bot.chat(-100).send("Can't send messages to %s (reason: %s)" %
                (ar, e.reason))
    except Exception as e: 
        chat.send("non mandato")
        bot.chat(-100).send("user " + str(message.sender.id) +  " errore "+ str(e))

@bot.command("AggiungiChannelLog")
def AggiungiChannelLog(chat,message,args):
    admins=[""]
    if str(message.sender.id) in admins:
        ar=" ".join(args)
        l=open("Channel-log.txt","a")
        try:
            l.write("\n"+str(ar))
        except Exception as e: 
            chat.send("non aggiornato")
            bot.chat(-10014).send("user " + str(message.sender.id) +  " errore "+ str(e))
        l.close()

@bot.command("RiscriviChannelLog")
def RiscriviChannelLog(chat,message,args):
    admins=[""]
    if str(message.sender.id) in admins:
        ar=" ".join(args)
        l=open("Channel-log.txt","w")
        try:
            l.write("\n"+str(ar))
            chat.send("aggiornato")
        except Exception as e: 
            chat.send("non aggiornato")
            bot.chat(-10014859005).send("user " + str(message.sender.id) +  " errore "+ str(e))
        l.close()

@bot.command("sondaggio")
def sondaggioo(chat,message,args,bot):
    admins=[""]
    if str(message.sender.id) in admins:
        ar=" ".join(args)
    btns=botogram.Buttons()
    btns[0].callback("sì","sondaggiosi")
    btns[1].callback("no","sondaggioNo")
    ida=0
    num_lines = sum(1 for line in open('log-in.txt'))
    inviati_a=" "
    while num_lines>ida:
            open_file=open('log-in.txt','r')
            file_lines=open_file.readlines()
            file = file_lines[ida].strip()  # First Line
            if file is None:
                pass
            if int(file)<0:
                pass
            else:
                try:
                    bot.chat(file).send(ar,attach=btns)
                    x=open("sondaggioid.txt","w")
                    x.write(str(message.id))
                    x.close()
                    inviati_a=inviati_a + " " + file
                except botogram.ChatUnavailableError as e:
                    bot.chat(-1000).send("Can't send messages to %s (reason: %s)" %
                    (e.chat_id, e.reason))
            ida=ida+1
    bot.chat(-100).send("il sondaggio è stato inviato a " +str(inviati_a) + 
    "\nil testo è " + str(ar)+ "\ndall admin @"+ str(message.sender.username))

@bot.callback("sondaggiosi")
def sondaggiosi(query,chat,message):
    votiattuali=open("sondaggiosì.txt","r")
    voti=votiattuali.readline()
    votiattuali.close()
    voti=int(voti)
    voti+=1
    votiattuali=open("sondaggiosì.txt","w")
    votiattuali.write(str(voti))
    votiattuali.close()
    salvaid=open("sondaggioid.txt","a")
    salvaid.write(str(chat.id)+"\n")
    salvaid.close()
    bot.chat(-10).send("@"+chat.username+"\n"+str(chat.id)+"ha votato si")
    message.delete()


@bot.callback("sondaggioNo")
def sondaggioNo(query,chat,message):
    votiattuali=open("sondaggiono.txt","r")
    voti=votiattuali.readline()
    votiattuali.close()
    voti=int(voti)
    voti+=1
    votiattuali=open("sondaggiono.txt","w")
    votiattuali.write(str(voti))
    votiattuali.close()
    salvaid=open("sondaggioid.txt","a")
    salvaid.write(str(chat.id)+"\n")
    salvaid.close()
    bot.chat(-100).send("@"+chat.username+"\n"+str(chat.id)+"ha votato no")
    message.delete()

@bot.command("vedisondaggio")
def sondaggio(chat,message,args):
    votiattuali=open("sondaggiosì.txt","r")
    voti=votiattuali.readline()
    votiattuali.close()
    voti=int(voti)
    votiattuali=open("sondaggiono.txt","r")
    votino=votiattuali.readline()
    votiattuali.close()
    votino=int(votino)
    votitotali=voti+votino
    names = ['si', 'no']
    values = [voti,votino]
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(names, values)
    plt.savefig("risultato.png")
    chat.send_photo("risultato.png",caption="i voti totali sono= "+ str(votitotali) + " hanno votato si " 
    + str(voti) + " hanno votato no = " + str(votino))
@bot.command("stopvoti")
def stopvoti(chat,message,bot):
    admins=[""]
    if str(message.sender.id) in admins:
        votiattuali=open("sondaggiosì.txt","r")
        voti=votiattuali.readline()
        votiattuali.close()
        voti=int(voti)
        votiattuali=open("sondaggiono.txt","r")
        votino=votiattuali.readline()
        votiattuali.close()
        votino=int(votino)
        votitotali=voti+votino
        bot.chat(-100).send("i voti totali sono= "+ str(votitotali) + " hanno votato si " 
        + str(voti) + " hanno votato no = " + str(votino))
        x=open("sondaggioid.txt","r")
        f=x.readline()
        x.close()
        f=int(f)
        ida=0
        num_lines = sum(1 for line in open('log-in.txt'))
        f=f+1
        while num_lines>ida:
                open_file=open('log-in.txt','r')
                file_lines=open_file.readlines()
                file = file_lines[ida].strip()  # First Line
                if file is None:
                    pass
                if int(file)<0:
                    pass
                else:
                    try:
                        bot.chat(file).send("stop ai voti")
                        try:
                            bot.chat(file).delete_message(f)
                            bot.chat(-100).send("non ha risposto al sondaggio"+str(file))
                        except:
                            pass
                        f=f+1
                    except botogram.ChatUnavailableError as e:
                        bot.chat(-100).send("Can't send messages to %s (reason: %s)" %
                        (e.chat_id, e.reason))
                        f=f+1
                ida=ida+1
        names = ['si', 'no']
        values = [voti,votino]
        plt.figure(figsize=(9, 3))
        plt.subplot(131)
        plt.bar(names, values)
        plt.savefig("risultato.png")
        bot.chat(-100).send_photo("risultato.png")
        votiattuali=open("sondaggiono.txt","w")
        votiattuali.write("0")
        votiattuali.close()
        votiattuali=open("sondaggiosì.txt","w")
        votiattuali.write("0")
        votiattuali.close()
@bot.command("sintassi")
def sintassi(chat,message,args,bot):
    chat.send("""/mandamessaggio + id 
    /nuovomessaggio + testo 
    /UNnotifiche
    /notifiche
    /img
    /start
    /info 
    /tags
    /ping 
    /deletegroup
    /addgroup 
    /newgroup 
    /stats 
    /suggerimento""")


if __name__ == "__main__":
    bot.run()
