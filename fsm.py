from transitions.extensions import GraphMachine
import telegram
bot = telegram.Bot(token='450660612:AAHWWvRfMN2KY4n_e26tz31zL1MX2nRGWLQ')
my_id = 382468305

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
        self.total = 0
        self.temp = 0

    def is_going_to_start(self, update):
        text = update.message.text
        return text.lower() == '/start'

    def is_going_to_order(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_tea(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_coffee(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_greentea(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            print("choose greentea")
            update.message.reply_text("You ordered green tea. It's 25 NTD.")
            self.temp = 25
            self.total += self.temp
            bot.send_photo(chat_id = my_id, photo = open('img/green tea.jpg', 'rb'))
        return text.lower() == '1'
    def is_going_to_blacktea(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            print("choose blacktea")
            update.message.reply_text("You ordered black tea. It's 25 NTD.")
            self.temp = 25
            self.total += self.temp
            bot.send_photo(chat_id = my_id, photo = open('img/black tea.jpg', 'rb'))
        return text.lower() == '2'
    def is_going_to_milktea(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            print("choose milktea")
            update.message.reply_text("You ordered milk tea. It's 30 NTD.")
            self.temp = 30
            bot.send_photo(chat_id = my_id, photo = open('img/milk tea.jpg', 'rb'))
        return text.lower() == '3'
    def is_going_to_matcha(self, update):
        text = update.message.text
        if(text.lower() == '4'):
            print("choose matcha")
            update.message.reply_text("You ordered matcha. It's 40 NTD.")
            self.temp = 40
            bot.send_photo(chat_id = my_id, photo = open('img/matcha.jpg', 'rb'))
        return text.lower() == '4'

    def is_going_to_add(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            print("choose add")
            update.message.reply_text("You added bubble. It's 5 NTD for additional.")
            self.temp += 5
            self.total += self.temp
        return text.lower() == '1'
    def is_going_to_noadd(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            print("choose add")
            update.message.reply_text("You didn't added bubble. No additional cost.")
            self.total += self.temp
        return text.lower() == '2'

    def is_going_to_blackcoffee(self, update):
        text = update.message.text
        if(text.lower() == '1'):
            print("choose black coffee")
            update.message.reply_text("You ordered black coffee. It's 50 NTD.")
            self.temp = 50
            self.total += self.temp
            bot.send_photo(chat_id = my_id, photo = open('img/black coffee.jpg', 'rb'))
        return text.lower() == '1'
    def is_going_to_latte(self, update):
        text = update.message.text
        if(text.lower() == '2'):
            print("choose latte")
            update.message.reply_text("You ordered latte. It's 55 NTD.")
            self.temp = 55
            self.total += self.temp
            bot.send_photo(chat_id = my_id, photo = open('img/latte.jpg', 'rb'))
        return text.lower() == '2'
    def is_going_to_cappuccino(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            print("choose cappuccino")
            update.message.reply_text("You ordered cappuccino. It's 55 NTD.")
            self.temp = 55
            self.total += self.temp
            bot.send_photo(chat_id = my_id, photo = open('img/cappuccino.jpg', 'rb'))
        return text.lower() == '3'

    def is_going_to_order2(self, update):
        print("order another drink")
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_reorder(self, update):
        text = update.message.text
        if(text.lower() == '3'):
            self.total -= self.temp
        return text.lower() == '3'

    def is_going_to_leave(self, update):
        text = update.message.text
        return text.lower() == '2'

    def is_going_to_end(self, update):
        text = update.message.text
        return text.lower() == '1'

    def on_enter_start(self, update):
        print('Entering [start]')
        update.message.reply_text("Welcome to F74036035's Cafe!!!")
        #bot.send_photo(chat_id = my_id, photo = open('img/cafe.jpg', 'rb'))
        update.message.reply_text("May I help you?")
        update.message.reply_text("1)order\n2)leave")
    def on_exit_start(self, update):
        print('Leaving [start]')

    def on_enter_order(self, update):
        print('Entering [order]')
        update.message.reply_text("Which kind of drink would you like?\n1)tea\n2)coffee")
    def on_exit_order(self, update):
        print('Leaving [order]')

	#tea
    def on_enter_tea(self, update):
        print('Entering [tea]')
        update.message.reply_text("What would you like to order?\n1) $25 green tea\n2) $25 black tea\n3) $30 milk tea\n4) $40 matcha")
    def on_exit_tea(self, update):
        print('Leaving [tea]')

	#add
    def on_enter_add(self, update):
        print('Entering [add]')
        update.message.reply_text("Would you like to add some bubbles for 5 NTD?\n1) $5 add bubbles\n2) $0 no thanks")
    def on_exit_add(self, update):
        print('Leaving [add]')

	#coffee
    def on_enter_coffee(self, update):
        update.message.reply_text("What would you like to order?\n1) $50 black coffee\n2) $55 latte\n3) $55 cappuccino")
        print('Entering [coffee]')
    def on_exit_coffee(self, update):
        print('Leaving [coffee]')


    def on_enter_pay(self, update):
        print('Entering [pay]')
        update.message.reply_text("Pay, order another drink, or abandon previous and reorder.\n1)pay\n2)order\n3)reorder")
    def on_exit_pay(self, update):
        print('Leaving [pay]')

    def on_enter_end(self, update):
        print('Entering [end]')
        bot.send_message(chat_id = my_id, text = "You paid " + str(self.total) + " NTD.")
        update.message.reply_text("Bye! Looking forward to serving you again!")
        self.total = 0
        update.message.reply_text("Leaving F74036035's cafe...")
        self.go_back(update)
    def on_exit_end(self, update):
        print('Leaving [end]')









