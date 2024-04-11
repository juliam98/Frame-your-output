import os 
import pandas as pd

term_columns, term_lines = os.get_terminal_size()

border_styles=pd.DataFrame(
    {
        "thin":['\u2500','\u2500','\u2502','\u2502','\u2510','\u250C','\u2518','\u2514'],
        "rounded":['\u2500','\u2500','\u2502','\u2502','\u256E','\u256D','\u256F','\u2570'],
        "block":['\u2580','\u2584','\u258C','\u2590','\u259C','\u259B','\u259F','\u2599'],
        "double":['\u2550','\u2550','\u2551','\u2551','\u2557','\u2554','\u255D','\u255A'],
        "double1":['\u2550','\u2550','\u2560','\u2551','\u2557','\u2554','\u255D','\u255A']
    },
    index=('top_char', 'bottom_char', 'l_side_character', 'r_side_character', 't_r_corner', 't_l_corner', 'b_r_corner', 'b_l_corner')
)

# print(border_styles, end="\n\n")

# Example string
atlas_names = [
    'Julia',
    'made this fun little code', 
    'to help you yassify your terminal output',
    'slay forever',
    'xoxo'
]

def FramedTermOutput(printlist:list, border_style:str='thin'):
    """
    Precious outputs deserve to be framed.

    - `printlist`: a list which is the output you would like to frame.
    - `border_style` (default: `thin`): the style of frame you'd like to use. 
        - Available options include `thin`, `rounded`, `block`, `double`, `double1`.
    """
    term_columns = os.get_terminal_size()[0]
    print(border_styles[border_style]['t_l_corner'],border_styles[border_style]['top_char']*(term_columns-2),border_styles[border_style]['t_r_corner'], sep="")

    for a in printlist:
        str_len=term_columns-len(a)-2
        print(border_styles[border_style]['l_side_character'], a, " "*str_len, border_styles[border_style]['r_side_character'], sep="")

    print(border_styles[border_style]['b_l_corner'],border_styles[border_style]['bottom_char']*(term_columns-2),border_styles[border_style]['b_r_corner'], sep="")

FramedTermOutput(atlas_names, border_style='block')