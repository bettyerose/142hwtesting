"""
CMSC 14200, Spring 2023
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
import os
import sys
from typing import List, Tuple

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # pylint: disable=wrong-import-position


class BitEdit:
    """
    Class for a GUI-based bitmap editor
    """

    window : int
    border : int
    grid : List[List[bool]]
    surface : pygame.surface.Surface
    clock : pygame.time.Clock

    def __init__(self, window: int = 600, border: int = 10,
                 cells_side: int = 32):
        """
        Constructor

        Parameters:
            window : int : height of window
            border : int : number of pixels to use as border around elements
            cells_side : int : number of cells on a side of a square bitmap grid
        """
        self.window = window
        self.border = border
        self.grid = [[False] * cells_side for i in range(cells_side)]
    
        # Initialize Pygame
        pygame.init()
        # Set window title
        pygame.display.set_caption("BitEdit")
        # Set window size
        self.surface = pygame.display.set_mode((window + border + cells_side,
                                                window))
        self.clock = pygame.time.Clock()

        self.event_loop()

    def draw_window(self) -> None:
        """
        Draws the contents of the window

        Parameters: none beyond self

        Returns: nothing
        """
        cells_side = len(self.grid)

        # Background
        self.surface.fill((128, 128, 128))

        square = (self.window - 2 * self.border) // cells_side
        mini_left = 2 * self.border + square * cells_side
        mini_top = (self.window - cells_side) // 2

        rect = (mini_left, mini_top, cells_side, cells_side)
        pygame.draw.rect(self.surface, color=(255, 255, 255),
                         rect=rect)

        black_tool_center = (mini_left + cells_side // 2,
                             self.border + cells_side // 2)
        white_tool_center = (mini_left + cells_side // 2,
                             self.border + 3 * (cells_side // 2))
        fill_tool_center = (mini_left + cells_side // 2,
                             2 * self.border + 5 * (cells_side // 2))

        pygame.draw.circle(self.surface, color=(0, 0, 0),
                           center=black_tool_center, radius=cells_side // 2)
        pygame.draw.circle(self.surface, color=(225, 0, 0),
                           center=black_tool_center, radius=cells_side // 2, width = 2)
        pygame.draw.circle(self.surface, color=(255, 255, 255),
                           center=white_tool_center, radius=cells_side // 2)
        pygame.draw.circle(self.surface, color=(0, 0, 0),
                           center=white_tool_center, radius=cells_side // 2,
                           width=2)
        pygame.draw.circle(self.surface, color=(0, 0, 0),
                           center=fill_tool_center, radius=cells_side // 2)
        pygame.draw.circle(self.surface, color=(255, 255, 255),
                           center=fill_tool_center, radius=cells_side // 4,
                           width=2)

        for row in range(cells_side):
            for col in range(cells_side):
                rect = (self.border + col * square,
                        self.border + row * square,
                        square, square)
                if self.grid[row][col]:
                    fill = (0, 0, 0)
                    border = False
                    mrect = (mini_left + col, mini_top + row, 1, 1)
                    pygame.draw.rect(self.surface, color=(0, 0, 0),
                                     rect=mrect)
                else:
                    fill = (255, 255, 255)
                    border = True
                pygame.draw.rect(self.surface, color=fill,
                                 rect=rect)
                if border:
                    pygame.draw.rect(self.surface, color=(0, 0, 0),
                                     rect=rect, width=1)

    def event_loop(self) -> None:
        """
        Handles user interactions

        Parameters: none beyond self

        Returns: nothing
        """
        cells_side = len(self.grid)
        square = (self.window - 2 * self.border) // cells_side
        mini_left = 2 * self.border + square * cells_side
        mini_top = (self.window - cells_side) // 2
        blk_tool = (mini_left + cells_side // 2,
                             self.border + cells_side // 2)
        wt_tool = (mini_left + cells_side // 2,
                             self.border + 3 * (cells_side // 2))

        while True:
            # Process Pygame events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #changing the tool
                if event.type == pygame.MOUSEBUTTONDOWN or pygame.MOUSEBUTTONUP or pygame.MOUSEMOTION:
                    rsquared = cells_side * cells_side // 4
                    mouseloc = pygame.mouse.get_pos()
                    xo, yo = mouseloc
                    xb, yb = blk_tool
                    xw, yw = wt_tool
                    if (xo - xb)(yo - yb) <= rsquared:
                        pygame.draw.circle(self.surface, color=(225, 0, 0),
                           center= blk_tool, radius=cells_side // 2, width = 4)
                        pygame.draw.circle(self.surface, color=(0, 0, 0),
                           center= wt_tool, radius=cells_side // 2, width = 2)
                        pygame.draw.circle(self.surface, color=(255, 255, 255),
                           center= wt_tool, radius=cells_side // 2, width = 4)   
                    if (xo - xw)(yo - yw) <= rsquared:
                        pygame.draw.circle(self.surface, color=(225, 0, 0),
                           center= wt_tool, radius=cells_side // 2, width = 4)
                        pygame.draw.circle(self.surface, color=(0, 0, 0),
                           center= blk_tool, radius=cells_side // 2, width = 2)
                        pygame.draw.circle(self.surface, color=(255, 255, 255),
                           center= blk_tool, radius=cells_side // 2, width = 4)   
                # Handle any other event types here
            # Update the display
            self.draw_window()
            pygame.display.update()
            self.clock.tick(24)

    def current_tool(self) -> None:
        """
        Keeps track of the currently selected tool

        Parameters: none beyond self

        Returns: nothing
        """

        b = True

        while b:
            if pygame.event.peek(MOUSEBUTTONDOWN) or pygame.event.peek(MOUSEBUTTONUP) or pygame.event.peek(MOUSEMOTION):
                if 
            






if __name__ == "__main__":
    BitEdit()
