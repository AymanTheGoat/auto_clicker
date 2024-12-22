import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Control the script's behavior.")

    # Duration ranges for keyboard and mouse events
    parser.add_argument(
        '--keyboard_duration_range', 
        type=lambda s: tuple(map(float, s.split(','))), 
        default=(0.1, 0.175), 
        help="Tuple of (min, max) between mouse/keyboard down/up events for keyboard (default: (0.1, 0.175))"
    )
    
    parser.add_argument(
        '--mouse_duration_range', 
        type=lambda s: tuple(map(float, s.split(','))), 
        default=(0.1, 0.200), 
        help="Tuple of (min, max) between mouse/keyboard down/up events for mouse (default: (0.1, 0.200))"
    )

    # Probabilities
    parser.add_argument(
        '--jump_probability', 
        type=float, 
        default=0.05, 
        help="Probability to trigger jump (default: 0.1)"
    )
    
    parser.add_argument(
        '--inventory_probability', 
        type=float, 
        default=0.02, 
        help="Probability to trigger inventory (default: 0.1)"
    )
    
    parser.add_argument(
        '--move_probability', 
        type=float, 
        default=0.05, 
        help="Probability to trigger move (default: 0.1)"
    )
    
    parser.add_argument(
        '--turn_probability', 
        type=float, 
        default=0.1, 
        help="Probability to trigger turn (default: 0.1)"
    )

    # Increment value for when an event is not triggered
    parser.add_argument(
        '--chance_increment', 
        type=float, 
        default=0.02, 
        help="Value to add to probabilities when not triggered (default: 0.05)"
    )

    # Sleep range between iterations
    parser.add_argument(
        '--sleep_range', 
        type=lambda s: tuple(map(float, s.split(','))), 
        default=(0.1, 0.9), 
        help="Tuple of (min, max) between every action (default: (7, 11))"
    )

    # Logging option
    parser.add_argument(
        '--log', 
        action='store_false', 
        default=True, 
        help="Enable logging (default: False)"
    )

    # Colors option
    parser.add_argument(
        '--colors', 
        action='store_false', 
        default=True, 
        help="Enable colors (ANSI escape sequences) (default: False)"
    )
    
    parser.add_argument(
        '--autoreel',
        action='store_false', 
        default=True,
        help="Enable autoreel (default: False)"
    )
    
    # Audio options
    parser.add_argument(
        '--chunk_size', 
        type=int, 
        default=8192, 
        help="Chunk size for audio recording (default: 8192)"
    )

    parser.add_argument(
        '--sample_rate', 
        type=int, 
        default=44100, 
        help="Sample rate for audio recording (default: 44100)"
    )

    parser.add_argument(
        '--threshold', 
        type=float,
        default=0.12,
        help="Threshold for sound detection (default: 0.12)"
    )
    
    return parser.parse_args()

