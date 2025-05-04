from pydantic import BaseModel
from typing import List
from typing import Optional
from datetime import datetime

# --------- USUARIO ---------
class UsuarioBase(BaseModel):
    nombre_usuario: str
    usuario: str
    contraseña_usuario: str
    correo_usuario: str

class UsuarioCreate(UsuarioBase):
    contraseña_usuario: str 

class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True  

class UsuarioUpdate(BaseModel):
    nombre_usuario: str
    usuario: str
    correo_usuario: str
    contraseña_usuario: Optional[str] = None  

class Usuario(UsuarioBase):
    id_usuario: int

# --------- CATEGORIA PRODUCTO ---------
class CategoriaProducto(BaseModel):
    nombre_categoria: str
    descripcion_categoria: Optional[str] = None

class CategoriaProductoCreate(CategoriaProducto):
    pass

class CategoriaProductoResponse(CategoriaProducto):
    id_categoria: int

    class Config:
        from_attributes = True

# --------- CLIENTE ---------
class ClienteBase(BaseModel):
    nombre_cliente: str
    identificacion: str
    correo_cliente: Optional[str] = None
    telefono_cliente: Optional[str] = None
    direccion_cliente: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id_cliente: int

    class Config:
        from_attributes = True

class ClienteUpdate(BaseModel):
    nombre_cliente: str
    identificacion: str
    correo_cliente: str
    telefono_cliente: str
    

class Usuario(UsuarioBase):
    id_usuario: int


# --------- PROVEEDOR ---------
class ProveedorBase(BaseModel):
    nombre_proveedor: str
    telefono_proveedor: Optional[str] = None
    correo_proveedor: Optional[str] = None
    id_categoria: int

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorResponse(ProveedorBase):
    id_proveedor: int

    class Config:
        from_attributes = True

# --------- PRODUCTO ---------
class ProductoBase(BaseModel):
    nombre_producto: str
    descripcion_producto: Optional[str] = None
    stock_producto: int
    precio_producto: float
    id_proveedor: int

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id_producto: int

    class Config:
        from_attributes = True

#-------------- VENTAS -----------------
class VentaCreate(BaseModel):
    id_producto: int
    id_cliente: int
    id_usuario: int
    precio: float

    
class Venta(VentaCreate):
    id_venta: int

    class Config:
        orm_mode = True