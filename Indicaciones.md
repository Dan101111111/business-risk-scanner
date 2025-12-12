# 📌 Flujo de Trabajo con Git – Business Risk Scanner

Este documento define las reglas oficiales de trabajo colaborativo para el proyecto.

---

## 🔧 RAMA PRINCIPAL (main)

- Representa el código estable y aprobado.
- Nadie debe hacer commits ni pushes directos hacia `main`.
- Solo se actualiza mediante un Pull Request final desde `dev`.

---

## 🧪 RAMA DE DESARROLLO (dev)

- Es la rama donde se integran todas las funcionalidades del equipo.
- Cada nueva función debe llegar a `dev` mediante Pull Requests.
- Nada debe ir directo de una rama personal → `main`.

---

## 👤 RAMAS PERSONALES / FEATURE

Cada integrante debe trabajar en **su propia rama personal**, creada a partir de `dev`.

**Ejemplos de nombres de ramas:**
```
feature/ratios-daniel
feature/ui-bruno
feature/zscore-igor
```

**Reglas:**
- Las ramas personales **siempre deben basarse en `dev`**, nunca en `main`.
- Los desarrollos se hacen exclusivamente dentro de la rama personal.
- Los commits locales deben subirse con:

```bash
git add .
git commit -m "Descripción del cambio"
git push origin feature/mi-rama
```

---

## 🔀 PULL REQUESTS (PR)

- Todo PR debe dirigirse **únicamente a `dev`**, nunca a `main`.
- Cada PR debe:
  - Tener un nombre descriptivo.
  - Solicitar revisión a uno o más miembros del equipo.
  - Resolver conflictos antes del merge.

---

## 🎯 INTEGRACIÓN FINAL

Cuando todas las funcionalidades estén completas y probadas en `dev`:

1. Se revisa la rama `dev` como equipo.
2. Se aprueba un único Pull Request de `dev` → `main`.
3. `main` se actualiza como versión final del proyecto.

---

## 📝 Comandos Recomendados

### Crear tu rama desde `dev`

```bash
git checkout dev
git pull origin dev
git checkout -b feature/mi-funcionalidad
```

### Trabajar en tu rama

```bash
git add .
git commit -m "Descripción del cambio"
git push origin feature/mi-funcionalidad
```

### Mantener tu rama actualizada con `dev`

```bash
git checkout dev
git pull origin dev
git checkout feature/mi-funcionalidad
git merge dev
```

---

## ✔ Estado Actual del Proyecto

- ✅ Rama `main` limpia e intacta.
- ✅ Rama `dev` contiene el módulo completo de ratios financieros y pruebas unitarias.
- ✅ 13 funciones implementadas.
- ✅ 43 tests unitarios pasando.
- ✅ README.md actualizado y documentación integrada.

---

## 🤝 Nota Final

Sigamos este flujo para mantener el código ordenado, evitar conflictos y garantizar que `main` siempre represente una versión estable del proyecto.

**¿Dudas o sugerencias?** No duden en comunicarlas al equipo.

---

**Última actualización:** Diciembre 2025  
**Responsable:** Daniel
