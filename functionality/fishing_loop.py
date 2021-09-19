import utils.global_variables as gv
from functionality.fishing_actions import *
from functionality.image_recognition import image_recognition_result
from wrappers.logging_wrapper import info, debug
from utils.config import dict, random_timeout
from time import time


def fishing_loop():
    debug('starting new loop')
    gv.last_results.add(call_appropriate_fishing_action())
    if(gv.last_results.is_full_of('0')):
        if(dict['repairing']['enable'].get() == 1):
            should_repair_in = -1 * (int(time()) - gv.last_repair_time - dict['repairing']['every'].get())
            debug("Repair in: " + str(should_repair_in))
            if(should_repair_in < 0):
                gv.last_repair_time = int(time())
                info("Repairing")
                repairing()
    if (gv.continue_fishing):
        gv.root.after(int(random_timeout(dict['fishing']['timeouts']['loop'])*1000), fishing_loop)



def call_appropriate_fishing_action():
    result_from_model = image_recognition_result(dict['fishing']['x'].get(), dict['fishing']['y'].get(),
                                         dict['fishing']['width'].get(), dict['fishing']['height'].get())

    if(gv.last_results.get_last_value() != result_from_model): # double checking that it is a correct match
        return result_from_model
    if result_from_model == '0': # 0 - model does not match any data (not fish captured yet)
        info("Waiting for fish...")
        return '0'
    elif result_from_model == '1': # 1 - model noticed a fish(left click to initiate fishing)
        info("Found a fish!")
        fish_notice()
        return '1'
    elif result_from_model == '2': #2 - model matched the green icon (reeling a fish in)
        info("Reeling a fish")
        reel_fish()
        return '2'
    elif result_from_model == '3': #3 - model matched the orange/red icon (wait x sec)
        info("Pause fishing")
        pause()
        return '3'
    elif result_from_model == '4': #4 - model did not match anything (left click, wait x sec)
        info("Cast fishing rod")
        cast()
        return '4'
