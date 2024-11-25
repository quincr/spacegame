import glfw
from OpenGL.GL import *
from settings import resolution

glfw.init()

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

window = glfw.create_window(resolution[0], resolution[1], 'space game', None, None)
if not window:
    glfw.terminate()
    quit()

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClearColor(0.1, 0.2, 0.3, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
