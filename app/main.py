
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError
from app.schemas import UsuarioUpdate  
from app.models import Usuario
from . import models, schemas, crud
from .database import SessionLocal, engine
from typing import List  # ¡Importación necesaria!



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- RUTAS--------

@app.post("/usuarios/", response_model=schemas.UsuarioResponse)
def crear_usuario(usuario: schemas.UsuarioCreate):
    db = SessionLocal()
    # Aquí iría tu lógica para crear el usuario
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    db.close()
    return db_usuario

@app.get("/usuarios/", response_model=List[schemas.UsuarioResponse])
def listar_usuarios():
    db = SessionLocal()
    usuarios = db.query(models.Usuario).all()
    db.close()
    return usuarios

@app.get("/usuarios/")
def get_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuario(db)

@app.put("/usuarios/{id_usuario}")
def actualizar_usuario(id_usuario: int, datos_actualizados: UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        usuario_db = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not usuario_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Actualizar los campos
        usuario_db.nombre_usuario = datos_actualizados.nombre_usuario
        usuario_db.usuario = datos_actualizados.usuario
        usuario_db.correo_usuario = datos_actualizados.correo_usuario
        
        if datos_actualizados.contraseña_usuario:
            usuario_db.contraseña_usuario = datos_actualizados.contraseña_usuario

        db.commit()
        db.refresh(usuario_db)
        return {"mensaje": "Usuario actualizado con éxito", "usuario": usuario_db}
    
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad: " + str(e.orig))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(e)}")

@app.get("/usuarios/{id_usuario}")
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@app.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Eliminar el usuario de la base de datos
    db.delete(usuario)
    db.commit()

    return {"mensaje": "Usuario eliminado con éxito"}

# Categorias ---------------------------------------------------------------
@app.post("/categorias/", response_model=schemas.CategoriaProductoResponse)
def crear_categoria(categoria: schemas.CategoriaProductoCreate, db: Session = Depends(get_db)):
    db_categoria = models.CategoriaProducto(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@app.get("/categorias/", response_model=list[schemas.CategoriaProducto])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.get_categorias(db=db)

# Clientes ---------------------------------------------------------------------------------
@app.post("/clientes/", response_model=schemas.ClienteBase)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.crear_cliente(db=db, cliente=cliente)
@app.get("/clientes/")
def listar_clientes(db: Session = Depends(get_db)):
    return crud.get_all_clientes(db=db)

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return crud.get_clientes(db=db, clientes_id=cliente_id)
@app.get("/clientes/", response_model=list[schemas.ClienteBase])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db=db)


@app.get("/clientes/")
def get_clientes(db: Session = Depends(get_db)):
    return crud.obtener_clientes(db)



@app.put("/clientes/{id_cliente}")
def actualizar_usuario(id_cliente: int, datos_actualizados: UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        cliente_db = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
        if not cliente_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Actualizar los campos
        cliente_db.nombre_usuario = datos_actualizados.nombre_usuario
        cliente_db.usuario = datos_actualizados.usuario
        cliente_db.correo_usuario = datos_actualizados.correo_usuario
        
        if datos_actualizados.contraseña_usuario:
            cliente_db.contraseña_usuario = datos_actualizados.contraseña_usuario

        db.commit()
        db.refresh(cliente_db)
        return {"mensaje": "Usuario actualizado con éxito", "usuario": cliente_db}
    
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error de integridad: " + str(e.orig))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(e)}")

@app.get("/usuarios/{id_usuario}")
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@app.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Eliminar el usuario de la base de datos
    db.delete(usuario)
    db.commit()


# Proveedores-----------------------------------------------------------------------------------
@app.post("/proveedores/", response_model=schemas.ProveedorBase)
def crear_proveedor(proveedor: schemas.ProveedorCreate, db: Session = Depends(get_db)):
    return crud.create_proveedor(db=db, proveedor=proveedor)

@app.get("/proveedores/", response_model=list[schemas.ProveedorBase])
def listar_proveedores(db: Session = Depends(get_db)):
    return crud.get_proveedores(db=db)

# Productos ---------------------------------------------------------------------------------
@app.post("/productos/", response_model=schemas.ProductoBase)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db=db, producto=producto)

@app.get("/productos/", response_model=list[schemas.ProductoBase])
def listar_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db=db)

@app.get("/productos/")
def get_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)
# Ventas-----------------------------------------------------------------------------------


@app.post("/ventas/", response_model=schemas.Venta)
def crear_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    return crud.crear_venta(db=db, venta=venta)
