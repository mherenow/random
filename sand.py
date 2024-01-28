import tkinter as tk
import numpy as np

class GridApp:
    def __init__(self, master, rows, columns, cell_size=50, background_color="white", outline_width=1):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.background_color = background_color
        self.outline_width = outline_width

        self.grid_data = np.zeros((rows, columns), dtype = int)

        self.white_cells = set()

        self.canvas = tk.Canvas(master, width=self.columns*self.cell_size, height=self.rows*self.cell_size, bg=self.background_color)
        self.canvas.pack()

        self.draw_grid()

        self.canvas.bind("<Button-1>", self.on_click)

        self.sand_fall()

    def draw_grid(self):
        self.canvas.delete("rect")

        for row in range(self.rows):
            for col in range(self.columns):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                fill_color = "white" if self.grid_data[row, col] == 1 else "black"
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=fill_color, width=self.outline_width, tags = "rect")

    def sand_fall(self):
        new_white_cells = set()
        all_white_cells = self.white_cells.copy()

        # Add newly added white cells from the click event
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid_data[row, col] == 1 and (row, col) not in all_white_cells:
                    all_white_cells.add((row, col))

        for row, col in all_white_cells:
            if row == self.rows - 1 or (row + 1, col) in all_white_cells:
                new_white_cells.add((row, col))
            else:
                new_white_cells.add((row + 1, col))
                self.grid_data[row, col] = 0
                self.grid_data[row + 1, col] = 1

        self.white_cells = new_white_cells
        self.draw_grid()
        self.canvas.after(100, self.sand_fall)

    def on_click(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size

        if self.grid_data[row, col] == 0:
            self.grid_data[row, col] = 1
        
        self.draw_grid()


def main():
    rows = 40
    columns = 40
    cell_size = 20
    background_color = "lightgray"
    outline_width = 1

    root = tk.Tk()
    app = GridApp(root, rows, columns, cell_size, background_color, outline_width)
    
    root.mainloop()

if __name__ == "__main__":
    main()
