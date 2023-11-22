import argparse
from imagen import Imagen


def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
    parser.add_argument("--biblioteca", choices=["PIL","Matplotlib","OpenCV"], required=True, help="Biblioteca para procesamiento de imagenes")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.biblioteca == 'PIL':
        imagen  = Imagen(args.imagen,args.biblioteca)
        load_image = imagen.load_imagen_pil()
    elif args.biblioteca == 'Matplotlib':
        imagen  = Imagen(args.imagen,args.biblioteca)
        load_image = imagen.load_imagen_opencv()
    elif args.biblioteca == 'OpenCV':
        imagen  = Imagen(args.imagen,args.biblioteca)
        load_image = imagen.load_imagen_opencv()
    else:
        print("Biblioteca no valida. Selecciona PIL, Matplotlib o OpenCV.")
        return

    try:
        imagen.show_imagen(load_image)
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    main()
