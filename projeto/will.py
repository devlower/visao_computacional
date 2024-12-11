import cv2
import numpy as np

def overlay_2d_figure(frame, figure_coords, color=(0, 255, 0), thickness=2, shape='square'):
    """
    Draws a simple 2D figure (rectangle, line, etc.) on the video frame.

    :param frame: The camera frame (image) where the figure will be drawn.
    :param figure_coords: Coordinates defining the figure.
    :param color: Color of the figure (default is blue).
    :param thickness: Line thickness of the figure.
    :param shape: Shape of the figure ('square', 'triangle', 'circle').
    """
    if shape == 'square':
        for i in range(len(figure_coords)):
            cv2.line(
                frame,
                figure_coords[i],
                figure_coords[(i + 1) % len(figure_coords)],
                color,
                thickness
            )
    elif shape == 'triangle':
        for i in range(len(figure_coords)):
            cv2.line(
                frame,
                figure_coords[i],
                figure_coords[(i + 1) % len(figure_coords)],
                color,
                thickness
            )
    elif shape == 'circle':
        center = figure_coords[0]
        radius = int(np.linalg.norm(np.array(figure_coords[0]) - np.array(figure_coords[1])))
        cv2.circle(frame, center, radius, color, thickness)

def move_figure(figure_coords, dx, dy):
    """
    Moves the figure by a specified offset.

    :param figure_coords: List of (x, y) coordinates defining the figure.
    :param dx: Offset in the x-direction.
    :param dy: Offset in the y-direction.
    :return: Updated list of coordinates.
    """
    return [(x + dx, y + dy) for x, y in figure_coords]

def switch_color(current_color):
    """
    Switches between blue and red colors.

    :param current_color: Current color in (B, G, R).
    :return: New color (B, G, R).
    """
    return (0, 0, 255) if current_color == (255, 0, 0) else (255, 0, 0)

def switch_shape(current_shape):
    """
    Switches between square, triangle, and circle.

    :param current_shape: Current shape ('square', 'triangle', 'circle').
    :return: New shape.
    """
    shapes = ['square', 'triangle', 'circle']
    next_shape = shapes[(shapes.index(current_shape) + 1) % len(shapes)]
    return next_shape

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    # Define a simple 2D square (as a list of points)
    square_coords = [(200, 150), (400, 150), (400, 350), (200, 350)]
    triangle_coords = [(300, 100), (450, 300), (150, 300)]
    circle_coords = [(300, 250), (350, 250)]  # (center, radius)
    
    # Movement variables
    dx, dy = 5, 5  # Speed of movement in x and y directions
    current_color = (255, 0, 0)  # Start with blue
    current_shape = 'square'  # Start with square
    
    while True:
        # Capture each frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Move the shape
        if current_shape == 'square':
            square_coords = move_figure(square_coords, dx, dy)
            figure_coords = square_coords
        elif current_shape == 'triangle':
            triangle_coords = move_figure(triangle_coords, dx, dy)
            figure_coords = triangle_coords
        elif current_shape == 'circle':
            circle_coords = move_figure(circle_coords, dx, dy)
            figure_coords = circle_coords

        # Check boundaries and reverse direction if needed
        frame_height, frame_width, _ = frame.shape
        if any(x < 0 or x > frame_width for x, y in figure_coords):
            dx = -dx
        if any(y < 0 or y > frame_height for x, y in figure_coords):
            dy = -dy

        # Overlay the 2D figure with the current shape and color
        overlay_2d_figure(frame, figure_coords, color=current_color, shape=current_shape)

        # Display the frame
        cv2.imshow("Augmented Reality - 2D Figure", frame)

        # Switch color and shape with key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            current_color = switch_color(current_color)
        elif key == ord('s'):
            current_shape = switch_shape(current_shape)

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
