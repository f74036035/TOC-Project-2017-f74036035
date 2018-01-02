import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

from transitions.extensions import GraphMachine as Machine


API_TOKEN = '450660612:AAHWWvRfMN2KY4n_e26tz31zL1MX2nRGWLQ'
WEBHOOK_URL = 'https://bd615d7f.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)

machine = TocMachine(
    states=[
        'init',
        'start',
        'order',
        'tea',
        'add',
        'coffee',
        'pay',
        'end'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'order',
            'conditions': 'is_going_to_order'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'end',
            'conditions': 'is_going_to_leave'
        },
        {
            'trigger': 'advance',
            'source': 'order',
            'dest': 'tea',
            'conditions': 'is_going_to_tea'
        },
        {
            'trigger': 'advance',
            'source': 'order',
            'dest': 'coffee',
            'conditions': 'is_going_to_coffee'
        },
        {
            'trigger': 'advance',
            'source': 'tea',
            'dest': 'add',
            'conditions': 'is_going_to_greentea'
        },
        {
            'trigger': 'advance',
            'source': 'tea',
            'dest': 'add',
            'conditions': 'is_going_to_blacktea'
        },
        {
            'trigger': 'advance',
            'source': 'tea',
            'dest': 'add',
            'conditions': 'is_going_to_milktea'
        },
        {
            'trigger': 'advance',
            'source': 'tea',
            'dest': 'pay',
            'conditions': 'is_going_to_matcha'
        },
        {
            'trigger': 'advance',
            'source': 'add',
            'dest': 'pay',
            'conditions': 'is_going_to_add'
        },
        {
            'trigger': 'advance',
            'source': 'add',
            'dest': 'pay',
            'conditions': 'is_going_to_noadd'
        },
        {
            'trigger': 'advance',
            'source': 'coffee',
            'dest': 'pay',
            'conditions': 'is_going_to_blackcoffee'
        },
        {
            'trigger': 'advance',
            'source': 'coffee',
            'dest': 'pay',
            'conditions': 'is_going_to_latte'
        },
        {
            'trigger': 'advance',
            'source': 'coffee',
            'dest': 'pay',
            'conditions': 'is_going_to_cappuccino'
        },
        {
            'trigger': 'advance',
            'source': 'pay',
            'dest': 'order',
            'conditions': 'is_going_to_order2'
        },
        {
            'trigger': 'advance',
            'source': 'pay',
            'dest': 'order',
            'conditions': 'is_going_to_reorder'
        },
        {
            'trigger': 'advance',
            'source': 'pay',
            'dest': 'end',
            'conditions': 'is_going_to_end'
        },
        {
            'trigger': 'go_back',
            'source': [
                'end'
            ],
            'dest': 'init'
        },
    ],
    initial='init',
    auto_transitions=False,
    show_conditions=True,
)

# draw the whole graph ...
machine.get_graph().draw('my_state_diagram.png', prog='dot')
# ... or just the region of interest
# (previous state, active state and all reachable states)
#machine.get_graph(show_roi=True).draw('my_state_diagram.png', prog='dot')

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
