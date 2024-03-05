from OpenGL.GL import *


class Mesh(object):

    def __init__(self, filename):
        self.vertices = []
        self.triangles = []
        self.load_model(filename)

    # Se hace la lctura del archivo
    def load_model(self, filename):
        with open(filename) as f:
            # Se lee cada una de las líneas
            line = f.readline()
            # Mientras que tengamos una linea seguimos procesando
            while line:
                # Se separa la línea en tokens
                line_tokens = line.split()
                # Si el primer token es 'v' se agregan los vértices
                if line_tokens[0] == 'v':
                    self.vertices.append([float(x) for x in line_tokens[1:]])
                elif line_tokens[0] == 'f':
                    self.triangles.append([int(x.split('/')[0]) - 1 for x in line_tokens[1:]])
                line = f.readline()
            print(f'Loaded {len(self.vertices)} {len(self.triangles)}')

    def draw_mesh(self):
        for t in range(0, len(self.triangles)):
            if self.triangles[t][0] > 1528 or self.triangles[t][1] > 1528 or self.triangles[t][2] > 1528:
                print(f'Triangle {t}')
            else:
                glBegin(GL_LINE_LOOP)
                glVertex3fv(self.vertices[self.triangles[t][0]])
                glVertex3fv(self.vertices[self.triangles[t][1]])
                glVertex3fv(self.vertices[self.triangles[t][2]])
                glEnd()
