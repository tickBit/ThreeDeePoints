# Simple 3D point class
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def project(self):
        
        # Simple perspective projection
        factor = 200 / (self.z + 4)
        x_proj = int(self.x * factor + 400)
        y_proj = int(self.y * factor + 300)
        return (x_proj, y_proj)
    
    def project_with_xn_yn_zn(self, xn, yn, zn):
        # Adjust the projection based on new coordinates
        factor = 200 / (zn + 4)
        x_proj = int(xn * factor + 400)
        y_proj = int(yn * factor + 300)
        return (x_proj, y_proj)
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
