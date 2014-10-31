
#
# CURRENTLY UNUSABLE
#

from mouse_click import MouseMove, go_click
import time

def main():
    mouse_moves = [ 1,
                    MouseMove('next level', (1098, 187), 1, 0.5),
                    MouseMove('next level', (1098, 187), 1, 0.5),
                    MouseMove('attack boss', (1022, 622), 850, 0.5),
                    MouseMove('pre level', (947, 187), 1, 0.5),
                    # MouseMove('pre level', (947, 187), 1, 2),
                    [
                        5,
                        MouseMove('attack', (1022, 622), 800, 0),
                        [
                            1,
                            MouseMove('upgrade 1, skill 1', (297, 349), 1, 0),
                            MouseMove('upgrade 1, skill 2', ((538-297)*1/6+297, 349), 1, 0),
                            MouseMove('upgrade 1, skill 3', ((538-297)*2/6+297, 349), 1, 0),
                            MouseMove('upgrade 1, skill 4', ((538-297)*3/6+297, 349), 1, 0),
                            MouseMove('upgrade 1, skill 5', ((538-297)*4/6+297, 349), 1, 0),
                            MouseMove('upgrade 1, skill 6', ((538-297)*5/6+297, 349), 1, 0),
                            MouseMove('upgrade 1, skill 7', (538, 349), 1, 0),

                            MouseMove('upgrade 2, skill 1', (297, 467), 1, 0),
                            MouseMove('upgrade 2, skill 2', ((538-297)*1/6+297, 467), 1, 0),
                            MouseMove('upgrade 2, skill 3', ((538-297)*2/6+297, 467), 1, 0),
                            MouseMove('upgrade 2, skill 4', ((538-297)*3/6+297, 467), 1, 0),
                            MouseMove('upgrade 2, skill 5', ((538-297)*4/6+297, 467), 1, 0),
                            MouseMove('upgrade 2, skill 6', ((538-297)*5/6+297, 467), 1, 0),
                            MouseMove('upgrade 2, skill 7', (538, 467), 1, 0),

                            MouseMove('upgrade 3, skill 1', (297, 582), 1, 0),
                            MouseMove('upgrade 3, skill 2', ((538-297)*1/6+297, 582), 1, 0),
                            MouseMove('upgrade 3, skill 3', ((538-297)*2/6+297, 582), 1, 0),
                            MouseMove('upgrade 3, skill 4', ((538-297)*3/6+297, 582), 1, 0),
                            MouseMove('upgrade 3, skill 5', ((538-297)*4/6+297, 582), 1, 0),
                            MouseMove('upgrade 3, skill 6', ((538-297)*5/6+297, 582), 1, 0),
                            MouseMove('upgrade 3, skill 7', (538, 582), 1, 0),
                    
                            MouseMove('upgrade 4, skill 1', (297, 702), 1, 0),
                            MouseMove('upgrade 4, skill 2', ((538-297)*1/6+297, 702), 1, 0),
                            MouseMove('upgrade 4, skill 3', ((538-297)*2/6+297, 702), 1, 0),
                            MouseMove('upgrade 4, skill 4', ((538-297)*3/6+297, 702), 1, 0),
                            MouseMove('upgrade 4, skill 5', ((538-297)*4/6+297, 702), 1, 0),
                            MouseMove('upgrade 4, skill 6', ((538-297)*5/6+297, 702), 1, 0),
                            MouseMove('upgrade 4, skill 7', (538, 702), 1, 0),

                            MouseMove('upgrade 5, skill 1', (297, 819), 1, 0),
                            MouseMove('upgrade 5, skill 2', ((538-297)*1/6+297, 819), 1, 0),
                            MouseMove('upgrade 5, skill 3', ((538-297)*2/6+297, 819), 1, 0),
                            MouseMove('upgrade 5, skill 4', ((538-297)*3/6+297, 819), 1, 0),
                            MouseMove('upgrade 5, skill 5', ((538-297)*4/6+297, 819), 1, 0),
                            MouseMove('upgrade 5, skill 6', ((538-297)*5/6+297, 819), 1, 0),
                            MouseMove('upgrade 5, skill 7', (538, 819), 1, 0),

                            [
                                5,
                                MouseMove('upgrade 5', (173, 819), 1, 0),
                                MouseMove('upgrade 4', (173, 702), 1, 0),
                                MouseMove('upgrade 3', (173, 582), 1, 0),
                                MouseMove('upgrade 2', (173, 467), 1, 0),
                                MouseMove('upgrade 1', (173, 349), 1, 0),
                            ],
                        ],
                        MouseMove('upgrade 1, skill 1 sleep', (297, 349), 1, 5),

                    ],
                ]
    while True:
        time.sleep(3)
        go_click(mouse_moves)
        
if __name__ == '__main__':
    main()
