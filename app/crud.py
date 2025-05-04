
from sqlalchemy.orm import Session
from . import models, schemas
from .models import Usuario
from .models import Cliente

from datetime import datetime
# --------- CATEGORIA PRODUCTO ---------
def create_categoria(db: Session, categoria: schemas.CategoriaProductoCreate):
    db_categoria = models.CategoriaProducto(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def get_categorias(db: Session):
    return db.query(models.CategoriaProducto).all()
# --------- USUARIOS ---------
def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuarios(db: Session):
    return db.query(models.Usuario).all()

def get_usuario_by_id(db: Session, id_usuario: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()

def obtener_usuario(db: Session):
    return db.query(models.Usuario).all()

def update_usuario(db: Session, usuario_id: int, usuario_data):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        for key, value in usuario_data.dict().items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario


# --------- PRODUCTOS ---------
def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def get_productos(db: Session):
    return db.query(models.Producto).all()

def obtener_productos(db: Session):
    return db.query(models.Producto).all()



# --------- CLIENTES ---------
def crear_cliente(db: Session, cliente: schemas.ClienteCreate):
    nuevo_cliente = models.Cliente(
        nombre_cliente=cliente.nombre_cliente,
        identificacion = cliente.identificacion,
        correo_cliente=cliente.correo_cliente,
        telefono_cliente=cliente.telefono_cliente,
        direccion_cliente=cliente.direccion_cliente
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def get_clientes(db: Session, clientes_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id_cliente == clientes_id).first()
def get_all_clientes(db: Session):
    return get_clientes(db)

def obtener_clientes(db: Session):
    return db.query(models.Cliente).all()

def update_cliente(db: Session, clientes_id: int, cliente_data):
    db_cliente = get_clientes(db, clientes_id)
    if db_cliente:
        for key, value in cliente_data.dict().items():
            setattr(db_cliente, key, value)
        db.commit()
        db.refresh(db_cliente)
    return db_cliente



# --------- PROVEEDORES ---------
def create_proveedor(db: Session, proveedor: schemas.ProveedorCreate):
    db_proveedor = models.Proveedor(**proveedor.dict())
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def get_proveedores(db: Session):
    return db.query(models.Proveedor).all()


# --------- VENTAS ---------

def crear_venta(db: Session, venta: schemas.VentaCreate):
    db_venta = models.Venta(**venta.dict())

    if not db_venta.fecha_venta:
        db_venta.fecha_venta = datetime.now()

    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta



