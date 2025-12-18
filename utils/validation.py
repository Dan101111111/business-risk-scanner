import streamlit as st
from typing import Optional


def validate_number(value: str | None, field_name: str) -> Optional[float]:
    """
    Valida que el valor ingresado sea numérico y no nulo.
    Acepta strings con comas y espacios (ej: "100,000" o "100 000").

    Args:
        value: Valor ingresado por el usuario (string con posibles comas/espacios)
        field_name: Nombre del campo para mensajes de error

    Returns:
        float válido o None si hay error
    """
    if value is None or value == "":
        st.error(f"El campo '{field_name}' es obligatorio.")
        return None

    try:
        # Limpiar comas y espacios antes de convertir
        cleaned_value = str(value).replace(",", "").replace(" ", "").strip()
        if cleaned_value == "":
            st.error(f"El campo '{field_name}' es obligatorio.")
            return None
        value = float(cleaned_value)
    except ValueError:
        st.error(f"El campo '{field_name}' debe ser numérico.")
        return None

    return value


def validate_positive(value: float, field_name: str) -> Optional[float]:
    """
    Verifica que el valor no sea negativo.
    """
    if value < 0:
        st.error(f"El campo '{field_name}' no puede ser negativo.")
        return None
    return value
