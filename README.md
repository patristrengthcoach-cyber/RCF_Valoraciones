# RCF Rendimiento — Dashboard Juvenil A

Panel de perfiles individuales (antropometría + placas de fuerza VALD) para la categoría Juvenil A.

## Estructura

- `dashboard.html` — el dashboard en sí (HTML/CSS/JS autocontenido, con los datos embebidos).
- `app.py` — envoltorio en Streamlit que sirve `dashboard.html`.
- `requirements.txt` — dependencias para Streamlit Community Cloud.

## Ejecutar en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Actualizar los datos

El dataset está embebido dentro de `dashboard.html` (bloque `<script id="dataset" type="application/json">`).
Para refrescar los datos, hay que regenerar ese HTML y volver a subirlo a este repo — el `app.py` no necesita tocarse.
