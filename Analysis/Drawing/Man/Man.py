import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Draw the face
x = 300
y = 500
radius = 70
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Draw the right eye
x = 325
y = 525
radius = 10
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 275
y = 525
radius = 10
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the nose
x1 = 300
y1 = 505
x2 = 285
y2 = 480
x3 = 315
y3 = 480
arcade.draw_triangle_filled(x1,y1,x2,y2,x3,y3,arcade.color.BLUE)


# Draw Cap
x1 = 280
y1 = 520
x2 = 320
arcade.draw_parabola_filled(x1,y1,x2,40, arcade.color.BLACK)

# Draw the left ears
x1 = 220
y1 = 575
x2 = 235
y2 = 520
x3 = 245
y3 = 540
arcade.draw_triangle_filled(x1,y1,x2,y2,x3,y3,arcade.color.GRAY)

# Draw the right ears
x1 = 375
y1 = 575
x2 = 355
y2 = 542
x3 = 365
y3 = 522
arcade.draw_triangle_filled(x1,y1,x2,y2,x3,y3,arcade.color.GRAY)

# Draw the smile
x = 300
y = 500
width = 50
height = 50
start_angle = 210
end_angle = 330
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 5)

# Draw Neck
x = 300
y = 417
arcade.draw_rectangle_filled(x, y, 30, 30, arcade.color.BLUE)

# Draw Body
x = 300
y = 310
arcade.draw_rectangle_filled(x, y, 150, 200, arcade.color.RED)

# Draw Left hand
x = 150
y = 390
arcade.draw_rectangle_filled(x, y, 150, 40, arcade.color.PURPLE_HEART)

# Draw Right hand
x = 450
y = 390
arcade.draw_rectangle_filled(x, y, 150, 40, arcade.color.PURPLE_HEART)

# Draw Left hand
x = 60
y = 390
arcade.draw_rectangle_filled(x, y, 30, 20, arcade.color.PAKISTAN_GREEN)

# Draw Right hand
x = 540
y = 390
arcade.draw_rectangle_filled(x, y, 30, 20, arcade.color.PAKISTAN_GREEN)

# Draw Left finger
x = 45
y = 360
arcade.draw_parabola_filled(x,y,60,30,arcade.color.BLACK,90)

# Draw right finger
x = 545
y = 360
arcade.draw_parabola_filled(x,y,560,30,arcade.color.BLACK,270)


# Draw Left Leg
x = 250
y = 130
arcade.draw_rectangle_filled(x, y, 50, 160, arcade.color.PURPLE_HEART)

# Draw Right Leg
x = 350
y = 130
arcade.draw_rectangle_filled(x, y, 50, 160, arcade.color.PURPLE_HEART)

# Draw Left sock
x = 250
y = 40
arcade.draw_rectangle_filled(x, y, 20, 20, arcade.color.BROWN)

# Draw Right sock
x = 350
y = 40
arcade.draw_rectangle_filled(x, y, 20, 20, arcade.color.BROWN)

# DRAW Left Shoes
x = 235
y = 20
arcade.draw_ellipse_filled(x,y, 85, 25, arcade.color.BLACK)

# DRAW Right Shoes
x = 365
y = 20
arcade.draw_ellipse_filled(x,y, 85, 25, arcade.color.BLACK)

# DRAW shirt
x1 = 310
y1 = 210
x2 = 310
y2 = 410
arcade.draw_line(x1, y1, x2, y2,arcade.color.BLACK, 2)

# DRAW button 1
x = 300
y = 260
arcade.draw_circle_filled(x,y, 5, arcade.color.BLACK, 5 )

# DRAW button 2
x = 300
y = 310
arcade.draw_circle_filled(x,y, 5, arcade.color.BLACK, 5 )

# DRAW button 3
x = 300
y = 360
arcade.draw_circle_filled(x,y, 5, arcade.color.BLACK, 5 )


# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()