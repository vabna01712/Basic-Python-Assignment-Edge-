

---

# Simple Calculator

A graphical user interface (GUI) calculator built using Python and the Tkinter library. This calculator allows basic arithmetic operations like addition, subtraction, multiplication, and division.

## Features

- **Basic Operations**: Perform addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **User-Friendly Interface**: Easy-to-use layout with labeled buttons.
- **Error Handling**: Displays `Error` if invalid input or calculations are performed.
- **All Clear (AC)**: Quickly reset the calculator for a fresh calculation.

## How to Use

1. **Input Numbers and Operators**:
   - Click the numeric and operator buttons (`+`, `-`, `*`, `/`) to input values into the display.
2. **Get Results**:
   - Press the `=` button to evaluate the expression.
3. **Clear the Display**:
   - Use the `AC` button to clear the display and start over.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone or download this repository.
3. Install the Tkinter library if it is not already included in your Python distribution (Tkinter comes pre-installed with most Python installations).

## Running the Calculator

1. Navigate to the directory where the `calculator.py` file is located.
2. Run the program using the following command:

   ```bash
   python calculator.py
   ```

3. The calculator window will appear. Start using it by clicking the buttons.

## Code Overview

The program is structured as follows:

- **Entry Widget**: Displays user input and results.
- **Buttons**: Each button is linked to an event handler that processes clicks and performs the appropriate action.
- **Event Handling**: The `handle_button_click` function handles button interactions, including input, evaluation, and clearing the display.

## Customization

You can easily customize the calculator's appearance and functionality:
- Change button labels or add new ones in the `button_labels` list.
- Modify fonts and button sizes in the `font`, `width`, and `height` parameters.
- Extend functionality by editing the `handle_button_click` function to support additional operations.

## Example Screenshot

*![image](https://github.com/user-attachments/assets/d24eb6ab-6fb9-4cf4-993b-a596c0b23869)
*

---

