import matplotlib
matplotlib.use('Agg')  
from django.shortcuts import render
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def leer_datos_ventas(file_path):
    with open(file_path) as file:
        data_json = json.load(file)
    return pd.DataFrame(data_json)


def preparar_datos_ventas(data):
    data["fecha"] = pd.to_datetime(data["fecha"])
    data["mes_num"] = np.arange(len(data))
    return data


def entrenar_modelo_ventas(data):
    X = data["mes_num"].values.reshape(-1, 1)
    y = data["ventas"].values
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo


def predecir_ventas_futuras(modelo, data, meses=24):
    meses_futuros = np.arange(len(data), len(data) + meses).reshape(-1, 1)
    ventas_futuras = modelo.predict(meses_futuros)
    futuras_fechas = pd.date_range(
        start=data["fecha"].max() + pd.DateOffset(months=1), periods=meses, freq="ME"
    )
    return pd.DataFrame({"fecha": futuras_fechas, "ventas": ventas_futuras})


def crear_grafica_ventas_anuales(data_completa, data_analizada):
    data_completa["año"] = data_completa["fecha"].dt.year
    ventas_anuales = data_completa.groupby("año")["ventas"].sum().reset_index()

    ultimo_año_analizado = data_analizada["fecha"].dt.year.max()

    ventas_analizadas = ventas_anuales[ventas_anuales["año"] <= ultimo_año_analizado]
    ventas_predichas = ventas_anuales[ventas_anuales["año"] > ultimo_año_analizado]

    plt.figure(figsize=(10, 6))

    bars_analizados = plt.bar(
        ventas_analizadas["año"], ventas_analizadas["ventas"], color="blue", width=0.6
    )

    bars_predichos = plt.bar(
        ventas_predichas["año"], ventas_predichas["ventas"], color="green", width=0.6
    )

    plt.axvline(
        x=ultimo_año_analizado,
        color="red",
        linestyle="--",
        label="Inicio Predicción",
    )

    plt.xlabel("Año")
    plt.ylabel("Ventas (Q)")
    plt.title("Ventas anuales y predicciones futuras")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    for bar in bars_analizados:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            ha="center",
            va="bottom",
        )

    for bar in bars_predichos:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            ha="center",
            va="bottom",
        )

    plt.savefig("static/images/ventas_predicciones.png")


def analizar_producto_mas_vendido(data_json):
    productos_data = []
    for entry in data_json:
        for producto in entry["productos"]:
            productos_data.append(
                {
                    "fecha": entry["fecha"],
                    "nombre": producto["nombre"],
                    "cantidad": producto["cantidad"],
                }
            )
    productos_df = pd.DataFrame(productos_data)
    productos_df["fecha"] = pd.to_datetime(productos_df["fecha"])
    productos_df["año"] = productos_df["fecha"].dt.year
    productos_anuales = (
        productos_df.groupby(["año", "nombre"])["cantidad"].sum().reset_index()
    )
    producto_mas_vendido = productos_anuales.sort_values(
        by="cantidad", ascending=False
    ).iloc[0]
    return producto_mas_vendido, productos_anuales


def predecir_ventas_producto(modelo, producto_mas_vendido, productos_anuales):
    nombre = producto_mas_vendido["nombre"]
    nombre_data = productos_anuales[productos_anuales["nombre"] == nombre]
    X_nombre = nombre_data["año"].values.reshape(-1, 1)
    y_nombre = nombre_data["cantidad"].values
    modelo_nombre = LinearRegression()
    modelo_nombre.fit(X_nombre, y_nombre)
    años_futuros_nombre = np.array([2024, 2025]).reshape(-1, 1)
    ventas_futuras_nombre = modelo_nombre.predict(años_futuros_nombre)
    return pd.DataFrame(
        {
            "año": [2024, 2025],
            "nombre": nombre,
            "cantidad": ventas_futuras_nombre,
        }
    )


def crear_grafica_pastel_producto(predicciones_nombre, nombre):
    plt.figure(figsize=(8, 8))

    def func(pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    plt.pie(
        predicciones_nombre["cantidad"],
        labels=predicciones_nombre["año"],
        autopct=lambda pct: func(pct, predicciones_nombre["cantidad"]),
        startangle=140,
        colors=["#ff9999", "#66b3ff"],
    )
    plt.title(f"Predicciones del Producto Más Vendido: {nombre}")
    plt.tight_layout()
    plt.savefig("static/images/producto_mas_vendido_predicciones.png")


def dashboard(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        data = pd.read_csv(file)
        data["fecha"] = pd.to_datetime(data["fecha"])
        data["mes_num"] = np.arange(len(data))

        data["productos"] = data["productos"].apply(json.loads)
    else:
        data = leer_datos_ventas("data/ventas.json")
        data = preparar_datos_ventas(data)

    modelo = entrenar_modelo_ventas(data)
    predicciones = predecir_ventas_futuras(modelo, data)

    data_completa = pd.concat([data[["fecha", "ventas"]], predicciones])
    crear_grafica_ventas_anuales(data_completa, data)

    data_json = data.to_dict("records")
    producto_mas_vendido, productos_anuales = analizar_producto_mas_vendido(data_json)
    predicciones_nombre = predecir_ventas_producto(
        modelo, producto_mas_vendido, productos_anuales
    )

    crear_grafica_pastel_producto(predicciones_nombre, producto_mas_vendido["nombre"])

    return render(
        request,
        "dashboard/home.html",
        {
            "predicciones": predicciones.to_dict("records"),
            "producto_mas_vendido": predicciones_nombre.to_dict("records"),
        },
    )
