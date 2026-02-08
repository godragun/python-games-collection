import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def gui_calculator():
    try:
        import tkinter as tk
        from tkinter import font
    except ImportError:
        print("Tkinter is required for this calculator")
        print("On most systems, it comes with Python")
        print("If missing, install with:")
        print("sudo apt-get install python3-tk  # Ubuntu/Debian")
        print("brew install python-tk           # macOS")
        return
    
    class Calculator:
        def __init__(self, root):
            self.root = root
            self.root.title("Calculator")
            self.root.geometry("300x400")
            self.root.resizable(False, False)
            
            self.current_input = ""
            self.result_var = tk.StringVar(value="0")
            self.create_widgets()
        
        def create_widgets(self):
            # Display
            display_frame = tk.Frame(self.root, height=80, bg='#f0f0f0')
            display_frame.pack(fill=tk.X, padx=10, pady=10)
            
            result_label = tk.Label(
                display_frame,
                textvariable=self.result_var,
                font=font.Font(size=24),
                anchor='e',
                bg='#f0f0f0',
                fg='#333'
            )
            result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Buttons
            buttons_frame = tk.Frame(self.root)
            buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            buttons = [
                ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
                ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
                ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
                ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
                ('C', 4, 0), ('CE', 4, 1), ('(', 4, 2), (')', 4, 3)
            ]
            
            for (text, row, col) in buttons:
                if text == '=':
                    btn = tk.Button(
                        buttons_frame,
                        text=text,
                        font=font.Font(size=14, weight='bold'),
                        bg='#4CAF50',
                        fg='white',
                        command=lambda t=text: self.on_button_click(t)
                    )
                elif text in ['C', 'CE']:
                    btn = tk.Button(
                        buttons_frame,
                        text=text,
                        font=font.Font(size=14),
                        bg='#f44336',
                        fg='white',
                        command=lambda t=text: self.on_button_click(t)
                    )
                elif text in ['+', '-', '*', '/', '(', ')']:
                    btn = tk.Button(
                        buttons_frame,
                        text=text,
                        font=font.Font(size=14),
                        bg='#2196F3',
                        fg='white',
                        command=lambda t=text: self.on_button_click(t)
                    )
                else:
                    btn = tk.Button(
                        buttons_frame,
                        text=text,
                        font=font.Font(size=14),
                        bg='#e0e0e0',
                        command=lambda t=text: self.on_button_click(t)
                    )
                
                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            
            # Configure grid weights
            for i in range(5):
                buttons_frame.rowconfigure(i, weight=1)
            for i in range(4):
                buttons_frame.columnconfigure(i, weight=1)
        
        def on_button_click(self, char):
            if char == '=':
                try:
                    result = eval(self.current_input)
                    self.current_input = str(result)
                    self.result_var.set(result)
                except:
                    self.result_var.set("Error")
                    self.current_input = ""
            elif char == 'C':
                self.current_input = ""
                self.result_var.set("0")
            elif char == 'CE':
                if self.current_input:
                    self.current_input = self.current_input[:-1]
                    self.result_var.set(self.current_input if self.current_input else "0")
            else:
                self.current_input += str(char)
                self.result_var.set(self.current_input)
    
    print("➗ GUI Calculator")
    print("=" * 40)
    print("Opening calculator window...")
    
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

# 43. 🧱 Tetris Game

if __name__ == "__main__":
    gui_calculator()
