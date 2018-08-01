# Exploring arcade library
# http://arcade.academy/quick_index.html

import arcade

arcade.open_window(800,600,"Text Example")
arcade.set_background_color(arcade.color.RED)
arcade.start_render()
text = arcade.create_text("Text example", arcade.color.GREEN, 14, bold =True)
arcade.render_text(text, 250, 300, 30)

arcade.draw_text("Text Example", 250, 300, arcade.color.BLACK, 10)

arcade.finish_render()
arcade.quick_run(5)

import arcade

arcade.open_window(800,600,"Arcs Example")
arcade.set_background_color(arcade.color.RED)
arcade.start_render()
arcade.draw_arc_filled(100,200, 50,50,arcade.color.YELLOW,0,270,45)
arcade.draw_arc_outline(200,200, 50,50,arcade.color.YELLOW,45,315)
arcade.draw_arc_filled(150, 144, 15, 36, arcade.color.BOTTLE_GREEN, 90, 360, 45)
arcade.draw_arc_filled(150, 154, 15, 36, (255, 0, 0, 127), 90, 360, 45)
arcade.draw_arc_outline(150, 81, 15, 36, arcade.color.BRIGHT_MAROON, 90, 360)
transparent_color = (255, 0, 0, 127)
arcade.draw_arc_outline(150, 71, 15, 36, transparent_color, 90, 360)
arcade.render_text(text, 250, 300, 30)
arcade.finish_render()
arcade.quick_run(5)



import arcade

arcade.open_window(800,600,"Some shapes Example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_circle_filled(100,100,50,arcade.color.BLACK_OLIVE)
arcade.draw_circle_outline(500,500,100,arcade.color.RED)
arcade.draw_ellipse_filled(200,200,100,50,arcade.color.BROWN,100)
arcade.draw_ellipse_outline(540, 273, 15, 36, arcade.color.AMBER, 3)

arcade.draw_parabola_filled(150, 150, 400, 50, arcade.color.BOTTLE_GREEN)

arcade.draw_point(60, 495, arcade.color.RED, 10)
point_list = ((165, 495), (165, 480), (165, 465), (195, 495), (195, 480), (195, 465))
arcade.draw_points(point_list, arcade.color.ZAFFRE, 10)

point_list = ((150, 240), (165, 240), (180, 255), (180, 285), (165, 300), (150, 300))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

arcade.finish_render()
arcade.quick_run(2)

import arcade

arcade.open_window(800,600,"Line example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_line(270, 495, 300, 450, arcade.color.WOOD_BROWN, 30)

point_list = ((510, 450), (570, 450), (510, 480), (570, 480), (510, 510), (570, 510))
arcade.draw_line_strip(point_list, arcade.color.TROPICAL_RAIN_FOREST, 3)

point_list = ((390, 450), (450, 450), (390, 480), (450, 480), (390, 510), (450, 510))
arcade.draw_lines(point_list, arcade.color.BLUE, 3)

arcade.finish_render()
arcade.quick_run(3)



import arcade

arcade.open_window(800,600,"Rect example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(10, 200, 300, 10, arcade.color.BLACK)
arcade.draw_rectangle_filled(390, 150, 45, 105, arcade.color.BLUSH)

arcade.draw_triangle_filled(500, 500, 400, 300, 600, 300, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(500, 200, 100, 100, arcade.color.BLACK)

arcade.finish_render()
arcade.quick_run(3)



import arcade

arcade.open_window(800,600,"Drawing Example")
arcade.set_background_color(arcade.color.WHITE)
my_list = arcade.ShapeElementList()
my_shape = arcade.create_ellipse_outline(50, 50, 20, 20, arcade.color.RED, 45)
my_list.append(my_shape)
my_shape = arcade.create_ellipse_filled(50, 50, 20, 20, arcade.color.RED, 2, 45)
my_list.append(my_shape)
my_shape = arcade.create_rectangle_filled(250, 50, 20, 20, arcade.color.RED, 45)
my_list.append(my_shape)
my_shape = arcade.create_rectangle_outline(450, 50, 20, 20, (127, 0, 27, 127), 2, 45)
my_list.append(my_shape)
my_shape = arcade.create_lines_with_colors(([0, 400], [700, 400]), ((127, 0, 27, 127), arcade.color.GREEN), 2)
my_list.append(my_shape)
my_list.move(5, 5)
arcade.start_render()
my_list.draw()
arcade.finish_render()
arcade.quick_run(3)


import arcade

window = arcade.Window(200, 100, resizable=True)
window.set_update_rate(1/20)
window.set_mouse_visible(True)
window.on_mouse_motion(0, 0, 0, 0)
window.on_mouse_press(0, 0, 0, 0)
window.on_mouse_release(0, 0, 0, 0)
window.on_key_press(0, 0)
window.on_key_release(0, 0)
window.on_mouse_drag(0, 0, 1, 1, 1, 0)
window.on_mouse_scroll(1, 1, 1, 1)
window.on_draw()
window.on_resize(500, 500)
window.set_size(500, 500)
window.update(1/20)
window.set_visible(True)
window.close()