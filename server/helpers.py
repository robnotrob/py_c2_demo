
def parse_hex_for_signal(hex_input, signal_byte, start_pos, stop_pos):
    
    if hex_input[start_pos:stop_pos] == signal_byte:
        return True
    
    return False