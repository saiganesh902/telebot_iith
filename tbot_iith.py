from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5272052081:AAGEHel53VrZQ_a73XeBPLS1N0bVN-MvpxA", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("""Select the issue:-
    /Lan - For Lan issues
    /WiFi - For WiFi issues""")
def ticket_h(update: Update, context: CallbackContext):
    update.message.reply_text("Raise a ticket here => support.comp.iith.ac.in")
def Lan_h(update: Update, context: CallbackContext):
    update.message.reply_text("""Lan issues:
    /Port -> for all socket related issues
    /Cable -> for cable related issues
    /Driver_l -> to check if the drivers are proper""")
def Wifi_h(update: Update, context: CallbackContext):
    update.message.reply_text("""WiFi issues:
    /Connect -> Unable to connect to WiFi
    /Speed -> Slow internet connection
    /After_update_problems -> Complications with WiFi after Update
    /Disappear -> WiFi icon or Network disappears
    /Driver_w -> WiFi driver issues""")
def socket(update: Update, context: CallbackContext):
    update.message.reply_text("""
 >Connect a blue network cable from the wall port to your computer network port
 >Make sure your computer is powered on
 >Follow the steps below for your computer type.""")
    update.message.reply_text("""For windows /windows_port""")
    update.message.reply_text("""For apple /apple_port""")
def windows_p(update: Update, context: CallbackContext):
    update.message.reply_text("""
 On a Windows computer:
>Go to the back of your computer
>Look for a solid orange or green light next to the blue network cable
>It will be lit if the network port is active
 The Ethernet connection should have a green indicator and say Connected""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def apple_p(update: Update, context: CallbackContext):
    update.message.reply_text("""
 On an Apple computer:
>Click the Apple menu
>Click System Preferences
>Click Network
 The Ethernet connection should have a green indicator and say Connected""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def Cable_l(update: Update, context: CallbackContext):
    update.message.reply_text("""
>Plug an Ethernet cable into your computer.
>Plug the other end of the Ethernet cable into one of your hub's Ethernet ports.
>You've set up an Ethernet connection between your hub and your computer – and can now enjoy fast, reliable internet.""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
def driver_l(update: Update, context: CallbackContext):
    update.message.reply_text("""
>Restart the Computer
>Use the Network Troubleshooter
>Reinstall the Ethernet drivers automatically and if not working try manually
>Reset the network adaptor
>Reset the Winsock
PS:- Check after each step; So that there may not be the need of further steps.""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def connection_w(update: Update, context: CallbackContext):
    update.message.reply_text("""
>If you have a problem connecting to Wi-Fi,
the issue may be with just that device or with all devices. 
>If it’s a single device, reset the network connection on the device by turning it off and back on. 
>It’s better to restart the router by powering it off for several seconds if the problem is with multiple devices.
>Make sure all the lights on the router are normal and you update any firmware. 
>Check to see if there’s an authentication issue too. If the problem is the router, you may need to replace it.""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def speed(update: Update, context: CallbackContext):
    update.message.reply_text("""
>Depending on your router, you will need to change channels or move the antennas around.
>If your speed is still slow after testing your speed online then rise a ticket""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def problems(update: Update, context: CallbackContext):
    update.message.reply_text("""
>Sometimes an update can cause Wi-Fi issues because the system failed,
to add total support needed for a seamless wireless connection. 
>This is often self-limiting as the system fixes the problem.
>You can speed up the process by right-clicking your Wi-Fi icon and clicking on “troubleshoot problems” for Windows. 
>You could also uninstall the update.""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def disappear(update: Update, context: CallbackContext):
    update.message.reply_text("""
>The Wi-FI network icon is there to inform you of your internet status. 
>If it disappears, you won’t be able to see any available Wi-Fi networks or connect to them. 
>A simple PC restart could get the icon showing again.
>Oftentimes, you just have to re-authenticate the connection in the event there are Wi-Fi issues. 
>If you don’t see your Wi-Fi network on the list, the issue is likely the router, and you should reset it.""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
def driver_w(update: Update, context: CallbackContext):
    update.message.reply_text("""
>Press Windows + R and type 'devmgmt.msc' and press enter.
>Click on 'Network Adapters' and then right click on 'Wi-Fi Controller'.
>Now, select 'Update drivers'.
>Now, click on 'Search automatically for updated driver software'.
>Once the drivers are installed, reboot the system.""")
    update.message.reply_text("""Still can't solve raise a ticket here => /ticket""")
    update.message.reply_text("""To go back => /start""")
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Port', socket))
updater.dispatcher.add_handler(CommandHandler('windows_port',windows_p))
updater.dispatcher.add_handler(CommandHandler('apple_port',apple_p))
updater.dispatcher.add_handler(CommandHandler('Cable_l',Cable_l))
updater.dispatcher.add_handler(CommandHandler('driver_l',driver_l))
updater.dispatcher.add_handler(CommandHandler('connect',connection_w))
updater.dispatcher.add_handler(CommandHandler('Speed',speed))
updater.dispatcher.add_handler(CommandHandler('After_update_problems',problems))
updater.dispatcher.add_handler(CommandHandler('Disappear',disappear))
updater.dispatcher.add_handler(CommandHandler('Driver_w',driver_w))
updater.dispatcher.add_handler(CommandHandler('Lan', Lan_h))
updater.dispatcher.add_handler(CommandHandler('WiFi', Wifi_h))
updater.dispatcher.add_handler(CommandHandler('ticket', ticket_h))
updater.start_polling()
