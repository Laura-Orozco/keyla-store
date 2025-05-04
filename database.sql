CREATE DATABASE keyla_store_;


-- Tabla de Usuarios
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de Categorías
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    direccion VARCHAR(255)
);

-- Tabla de Proveedores
CREATE TABLE proveedores (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Tabla de Productos
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    id_categoria INT,
    id_proveedor INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);

-- Tabla de Ventas
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
----------- poblacion
-- Usuarios
INSERT INTO usuarios (nombre, email, contraseña) VALUES 
('Admin', 'admin@keyla.com', 'admin123'),
('Keyla', 'keyla@tienda.com', 'keylapass');

-- Categorías
INSERT INTO categorias (nombre) VALUES 
('Ropa femenina'),
('Accesorios'),
('Calzado');

-- Clientes
INSERT INTO clientes (nombre, email, direccion) VALUES 
('Laura Gómez', 'laura@gmail.com', 'Calle 123'),
('Andrés Martínez', 'andres@gmail.com', 'Carrera 45');

-- Proveedores
INSERT INTO proveedores (nombre, contacto) VALUES 
('Moda S.A.', 'moda@proveedor.com'),
('Accesorios Ya', 'accesorios@ya.com');

-- Productos
INSERT INTO productos (nombre, precio, stock, id_categoria, id_proveedor) VALUES 
('Blusa floral', 59.99, 10, 1, 1),
('Aretes dorados', 25.00, 20, 2, 2),
('Sandalias negras', 89.50, 15, 3, 1);

-- Ventas
INSERT INTO ventas (id_cliente, total) VALUES 
(1, 59.99),
(2, 114.50);
