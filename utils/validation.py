import streamlit as st
from typing import Optional


def validate_number(value, field_name: str) -> Optional[float]:
    """
    Valida que el valor ingresado sea numérico y no nulo.

    Args:
        value: Valor ingresado por el usuario
        field_name: Nombre del campo para mensajes de error

    Returns:
        float válido o None si hay error
    """
    if value is None:
        st.error(f"El campo '{field_name}' es obligatorio.")
        return None

    try:
        value = float(value)
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
