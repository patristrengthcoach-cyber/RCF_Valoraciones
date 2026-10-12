# VALORACIÓN CANTERA — Racing Club Ferrol

Dashboard de la cantera (antropometría, pliegues, placas de fuerza VALD y control de crecimiento PHV).

## Estructura

- `dashboard.html` — el dashboard (HTML/CSS/JS autocontenido, con los datos embebidos). Pestañas: **Valoración general**, **Pliegues** y **PHV**.
- `app.py` — envoltorio de Streamlit que sirve `dashboard.html`.
- `requirements.txt` — dependencias para Streamlit Community Cloud.

## Ejecutar en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Actualizar la app web

1. Sustituye `dashboard.html` del repositorio por el nuevo (mismo nombre, en la raíz, junto a `app.py`).
2. `git add dashboard.html app.py && git commit -m "Actualiza dashboard" && git push`
3. Streamlit Community Cloud se redespliega solo en 1-2 minutos. Si sigues viendo la versión antigua:
   - en la app: menú ⋮ → *Reboot app* (o *Clear cache*),
   - en el navegador: recarga forzada (Ctrl+Shift+R / Cmd+Shift+R) o una ventana privada.
4. Cómo saber que es la versión nueva: arriba debe haber tres pestañas (Valoración general · Pliegues · PHV).

Los datos están embebidos en `dashboard.html` (bloque `<script id="dataset" type="application/json">`): para refrescarlos hay que regenerar ese HTML y volver a subirlo.
