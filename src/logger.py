from typing import Tuple
from datetime import datetime


class Logger:
    def __init__(self, *,path):
        self.logs_path = path

    def log(self, iteration: int, sleep_time: int, inventory_bool: bool, look_around_bool: bool,
            jump_bool: bool, move_bool: bool, moved_mouse_num: int,
            looked_at_point: Tuple[int, int], pressed_key: Tuple[str, int]):
        self.log_entry = {
            "iteration": iteration,
            "sleep_time": sleep_time,
            "inventory_bool": inventory_bool,
            "look_around_bool": look_around_bool,
            "jump_bool": jump_bool,
            "move_bool": move_bool,
            "moved_mouse_num": moved_mouse_num,
            "looked_at_point": looked_at_point,
            "pressed_key": pressed_key
        }


    def __compile(self, log_entry: dict, use_colors: bool = True) -> str:
        """Retrieve and format a single log entry for display."""
        template = (
            "Iteration number {iteration}, lasts for {sleep_time} seconds:\n"
            "    Inventory : {inventory_bool}, moves : {moved_mouse_num}\n"
            "    Jumped    : {jump_bool}\n"
            "    Moved     : {move_bool}, direction : {pressed_key[0]}, duration : {pressed_key[1]}\n"
            "    Turned    : {look_around_bool}, coordinates : {looked_at_point}"
        )

        if not use_colors:
            return template.format(
                iteration=log_entry["iteration"],
                sleep_time=log_entry["sleep_time"],
                inventory_bool=log_entry["inventory_bool"],
                moved_mouse_num=log_entry["moved_mouse_num"],
                jump_bool=log_entry["jump_bool"],
                move_bool=log_entry["move_bool"],
                pressed_key=log_entry["pressed_key"],
                look_around_bool=log_entry["look_around_bool"],
                looked_at_point=log_entry["looked_at_point"]
            )

        def colorize(text: str, color_code: str) -> str:
            return f"\033[{color_code}m{text}\033[0m"

        color_map = {
            "title": "95",       # Magenta
            "tuple": "94",       # Blue
            "header": "96",      # Cyan
            "pressed_key": "93", # Yellow
            "number": "90",      # Grey
            "bool_true": "92",   # Green
            "bool_false": "91",  # Red
        }

        return (
            f"{colorize('Iteration number', color_map['title'])} {colorize(str(log_entry['iteration']), color_map['number'])}, "
            f"{colorize('lasts for', color_map['title'])} {colorize(str(log_entry['sleep_time']), color_map['number'])} {colorize('seconds', color_map['title'])}:\n"
            f"    {colorize('Inventory', color_map['header'])} : "
            f"{colorize(str(log_entry['inventory_bool']), color_map['bool_true'] if log_entry['inventory_bool'] else color_map['bool_false'])}, "
            f"{colorize('moves', color_map['header'])} : {colorize(str(log_entry['moved_mouse_num']), color_map['number'])}\n"
            f"    {colorize('Jumped', color_map['header'])}    : "
            f"{colorize(str(log_entry['jump_bool']), color_map['bool_true'] if log_entry['jump_bool'] else color_map['bool_false'])}\n"
            f"    {colorize('Moved', color_map['header'])}     : "
            f"{colorize(str(log_entry['move_bool']), color_map['bool_true'] if log_entry['move_bool'] else color_map['bool_false'])}, "
            f"{colorize('direction', color_map['header'])} : {colorize(log_entry['pressed_key'][0], color_map['pressed_key'])}, "
            f"{colorize('duration', color_map['header'])} : {colorize(str(log_entry['pressed_key'][1]), color_map['number'])}\n"
            f"    {colorize('Turned', color_map['header'])}    : "
            f"{colorize(str(log_entry['look_around_bool']), color_map['bool_true'] if log_entry['look_around_bool'] else color_map['bool_false'])}, "
            f"{colorize('coordinates', color_map['header'])} : {colorize(str(log_entry['looked_at_point']), color_map['tuple'])}"
        )

    def __get_formatted_datetime(self):
        current_datetime = datetime.now()  # Use 'datetime' directly here
        formatted_datetime = current_datetime.strftime("%a %d, %B %Y | %H:%M:%S")
        return formatted_datetime
    

    def printLogs(self, use_colors: bool = True):
        print(self.__compile(self.log_entry, use_colors))


    def writeLogs(self, ):
        with open(self.logs_path, "a") as f:
            f.write(f"[{self.__get_formatted_datetime()}]\n")
            f.write(self.__compile(self.log_entry, use_colors=False))
            f.write("\n\n")


def logArgs(args):
    if args.colors: 
        def colorize(text: str, color_code: str) -> str:
            return f"\033[{color_code}m{text}\033[0m"
    else:
        def colorize(text: str, color_code: str) -> str:
            return text

    color_map = {
        "title": "95",       # Magenta
        "tuple": "94",       # Blue
        "header": "96",      # Cyan
        "pressed_key": "93", # Yellow
        "number": "90",      # Grey
        "bool_true": "92",   # Green
        "bool_false": "91",  # Red
    }

    string = f"""{colorize('keyboard duration range:', color_map['header'])} {colorize(str(args.keyboard_duration_range), color_map['tuple'])}
{colorize('mouse duration range:', color_map['header'])} {colorize(str(args.mouse_duration_range), color_map['tuple'])}
{colorize('jump probability:', color_map['header'])} {colorize(str(args.jump_probability), color_map['number'])}
{colorize('inventory probability:', color_map['header'])} {colorize(str(args.inventory_probability), color_map['number'])}
{colorize('move probability:', color_map['header'])} {colorize(str(args.move_probability), color_map['number'])}
{colorize('turn probability:', color_map['header'])} {colorize(str(args.turn_probability), color_map['number'])}
{colorize('chance increment:', color_map['header'])} {colorize(str(args.chance_increment), color_map['number'])}
{colorize('sleep range:', color_map['header'])} {colorize(str(args.sleep_range), color_map['tuple'])}
{colorize('log:', color_map['header'])} {colorize(str(args.log), color_map['bool_true'] if args.log else color_map['bool_false'])}
{colorize('colors:', color_map['header'])} {colorize(str(args.colors), color_map['bool_true'] if args.colors else color_map['bool_false'])}
{colorize('autoreel:', color_map['header'])} {colorize(str(args.autoreel), color_map['bool_true'] if args.autoreel else color_map['bool_false'])}
{colorize('sample rate:', color_map['header'])} {colorize(str(args.sample_rate), color_map['number'])}
{colorize('chunk size:', color_map['header'])} {colorize(str(args.chunk_size), color_map['number'])}
{colorize('threshold:', color_map['header'])} {colorize(str(args.threshold), color_map['number'])}

"""
    return string