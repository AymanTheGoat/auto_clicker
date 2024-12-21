from master_class import Master
from random import randint, uniform, random
from time import sleep
from utilities import parse_args, Logger
from pathlib import Path



try:
    if __name__ == "__main__":
        args = parse_args()

        KEYBOARD_DURATION_RANGE = args.keyboard_duration_range
        MOUSE_DURATION_RANGE = args.mouse_duration_range
        JUMP_PROBABILITY = args.jump_probability
        INVENTORY_PROBABILITY = args.inventory_probability
        MOVE_PROBABILITY = args.move_probability
        TURN_PROBABILITY = args.turn_probability
        CHANCE_INCREMENT = args.chance_increment
        SLEEP_RANGE = args.sleep_range
        LOG = args.log
        COLORS = args.colors

        # ## Tuple of (min, max) between mouse/keyboard down/up events
        # KEYBOARD_DURATION_RANGE = (0.1, 0.175)
        # MOUSE_DURATION_RANGE = (0.1, 0.200)

        # ## Proabability to trigger jump 0.1 = 10%
        # JUMP_PROBABILITY = 0.1
        # INVENTORY_PROBABILITY = 0.1
        # MOVE_PROBABILITY = 0.1
        # TURN_PROBABILITY = 0.1
        
        # ## Number to add to probabilities when not triggered
        # CHANCE_INCREMENT = 0.05

        # ## Tuple of (min, max) between every iteration
        # SLEEP_RANGE = (7, 11)

        # LOG = False
        # COLORS = True


        ########### Initialization ###########
        if LOG:
            logs_path = Path.home() / "Documents" / "logs.txt"
            print(f"Logs will be saved to: {logs_path}")
            logger = Logger(path=logs_path)
        
        master = Master(keyboard_duration=KEYBOARD_DURATION_RANGE, mouse_duration=MOUSE_DURATION_RANGE)
        keySequence = master.generateKeySequence()
        index = 0
        iteration = 0

        actions = {
            'jump': JUMP_PROBABILITY,
            'inventory': INVENTORY_PROBABILITY,
            'move': MOVE_PROBABILITY,
            'turn': TURN_PROBABILITY
        }

        while True:
            ############### BEGIN ###############
            sleepTime = round(uniform(*SLEEP_RANGE), 2)
            inventoryBool = False       # for logging purposes
            lookAroundBool = False      # for logging purposes
            jumpBool = False            # for logging purposes
            moveBool = False            # for logging purposes
            movedMouseNum = 0           # for logging purposes
            lookedAtPointTuple = (0, 0) # for logging purposes
            pressedKeyTuple = ("", 0)   # for logging purposes

            ################ Inventory ################
            if random() < actions['inventory']:
                movedMouseNum = master.openInventory()
                actions['inventory'] = MOVE_PROBABILITY
                inventoryBool = True
            else:
                actions['inventory'] += CHANCE_INCREMENT


            ################ Jump ################
            if random() < actions['jump']:
                master.jump()
                actions['jump'] = JUMP_PROBABILITY
                jumpBool = True
            else:
                actions['jump'] += CHANCE_INCREMENT


            ############# Look Around #############
            if random() < actions['turn']:
                lookedAtPointTuple = (randint(-40, 40), randint(-30, 30))
                master.moveAndReturn(*lookedAtPointTuple)
                actions['turn'] = TURN_PROBABILITY
                lookAroundBool = True
            else:
                actions['turn'] += CHANCE_INCREMENT
            

            ################ Move ################ 
            if random() < actions['move']:
                pressedKeyTuple = (keySequence[index], round(master.keyboard.pressKey(keySequence[index]), 2))
                index = (index + 1) % len(keySequence)
                actions['move'] = MOVE_PROBABILITY
                moveBool = True
            else:
                actions['move'] += CHANCE_INCREMENT


            ############### Logging ###############
            if LOG:
                logger.log(
                    iteration=iteration,
                    sleep_time=sleepTime,
                    inventory_bool=inventoryBool,
                    look_around_bool=lookAroundBool,
                    jump_bool=jumpBool,
                    move_bool=moveBool,
                    moved_mouse_num=movedMouseNum,
                    looked_at_point=lookedAtPointTuple,
                    pressed_key=pressedKeyTuple
                )
                logger.printLogs(COLORS)
                logger.writeLogs()


            ############### END ###############
            master.fish()
            iteration += 1
            sleep(sleepTime) 

except KeyboardInterrupt:
    print("\n\033[95mGoodbye!\033[0m")
    sleep(1.5)
    exit(0)