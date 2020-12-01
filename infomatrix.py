import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("gs1")
    args = parser.parse_args()

    gtin = args.gs1[3:16]
    nro_serie = args.gs1[18:28]
    fecha_vto = args.gs1[30:36]
    nro_lote = args.gs1[38:]

    print(
        f"""
    - scan OK!: {args.gs1}
    {60*'-'}
    - GTIN: {gtin}
    - Nro. Serie: {nro_serie}
    - Fecha Vto.: {fecha_vto[4:6]}/{fecha_vto[2:4]}/20{fecha_vto[0:2]}
    - Nro. Lote: {nro_lote}
    """
    )


if __name__ == "__main__":
    main()
