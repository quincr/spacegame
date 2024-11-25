from __future__ import annotations

from OpenGL.GL import *

class ShaderProgram():
    def __init__(self: ShaderProgram, vertex_shader_path: str, fragment_shader_path: str) -> None:
        vertex_shader = glCreateShader(GL_VERTEX_SHADER)
        with open(vertex_shader_path, 'r') as vertex_shader_file:
            glShaderSource(vertex_shader, vertex_shader_file.read())

        glCompileShader(vertex_shader)
        if not glGetShaderiv(vertex_shader, GL_COMPILE_STATUS):
            raise Exception(glGetShaderInfoLog(vertex_shader).decode())

        fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
        with open(fragment_shader_path, 'r') as fragment_shader_file:
            glShaderSource(fragment_shader, fragment_shader_file.read())

        glCompileShader(fragment_shader)
        if not glGetShaderiv(fragment_shader, GL_COMPILE_STATUS):
            raise Exception(glGetShaderInfoLog(fragment_shader).decode())

        shader_program = glCreateProgram()
        glAttachShader(shader_program, vertex_shader)
        glAttachShader(shader_program, fragment_shader)
        glLinkProgram(shader_program)

        if not glGetProgramiv(shader_program, GL_LINK_STATUS):
            raise Exception(glGetProgramInfoLog(shader_program).decode())

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        self._prog = shader_program

    def Use(self: ShaderProgram) -> None:
        glUseProgram(self._prog)

    def Destroy(self: ShaderProgram) -> None:
        glDeleteProgram(self._prog)
        del self
